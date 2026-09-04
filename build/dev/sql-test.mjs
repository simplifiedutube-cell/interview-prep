/* Exercise the real SQL from lib/db.js against real SQLite (node:sqlite).
   Turso is libSQL — a SQLite fork — so the upsert semantics, the conflict
   predicate and the rev counter behave identically here. */
import { DatabaseSync } from "node:sqlite";
import { readFileSync } from "node:fs";

const src = readFileSync(new URL("../../lib/db.js", import.meta.url), "utf8");
const grab = (name) => {
  const m = src.match(new RegExp("export const " + name + " = `([\\s\\S]*?)`"));
  if (!m) throw new Error("could not extract " + name);
  return m[1];
};
const schema = [...src.matchAll(/`(CREATE TABLE IF NOT EXISTS[\s\S]*?|CREATE INDEX IF NOT EXISTS[^`]*|INSERT OR IGNORE[^`]*)`/g)]
  .map((m) => m[1]);
const UPSERT_GRADE = grab("UPSERT_GRADE");
const UPSERT_DAY = grab("UPSERT_DAY");

const db = new DatabaseSync(":memory:");
for (const s of schema) db.exec(s);

const L = [];
const log = (ok, m) => L.push((ok ? "PASS  " : "FAIL  ") + m);
const bump = () => db.exec("UPDATE meta SET n = n + 1 WHERE k='rev'");
const rev = () => db.prepare("SELECT n FROM meta WHERE k='rev'").get().n;
const put = (id, v, t) => db.prepare(UPSERT_GRADE).run(id, v, t);
const get = (id) => db.prepare("SELECT state, updated_at, rev FROM grades WHERE item_id=?").get(id);
const since = (r) => db.prepare("SELECT item_id, state FROM grades WHERE rev > ?").all(r);

log(schema.length === 7, `extracted ${schema.length} schema statements (want 7)`);
log(rev() === 0, `rev starts at 0 (got ${rev()})`);

// --- basic write + rev
bump(); put("t01.aaa", 2, 1000);
log(get("t01.aaa").state === 2 && Number(get("t01.aaa").rev) === 1, "insert stores state and rev");

// --- LAST WRITE WINS
bump(); put("t01.aaa", 1, 2000);
log(get("t01.aaa").state === 1, "newer timestamp overwrites (2 -> 1)");
bump(); put("t01.aaa", 2, 1500);
log(get("t01.aaa").state === 1, "OLDER timestamp is rejected (stays 1)");

// --- equal timestamps tie-break to the higher grade
bump(); put("t01.bbb", 1, 5000);
bump(); put("t01.bbb", 2, 5000);
log(get("t01.bbb").state === 2, "equal timestamps: higher grade wins");
bump(); put("t01.bbb", 0, 5000);
log(get("t01.bbb").state === 2, "equal timestamps: lower grade does not win");

// --- TOMBSTONE: clearing is a row, not a delete
bump(); put("t01.aaa", 0, 9000);
const tomb = get("t01.aaa");
log(tomb && tomb.state === 0, "un-tick writes a tombstone row, not a delete");
log(db.prepare("SELECT COUNT(*) c FROM grades").get().c === 2, "tombstone row still counted");

// --- IDEMPOTENCY: replaying a winning op changes nothing and does not advance rev
const before = rev();
bump(); put("t01.aaa", 0, 9000);
const rowRev = Number(get("t01.aaa").rev);
log(rowRev < rev(), "replayed identical op did NOT take the new rev");
log(since(before).length === 0, "replayed op yields no rows to other devices");

// --- CURSOR: rev is monotonic and independent of the timestamp
bump();
put("t02.ccc", 2, 1);            // ancient timestamp, brand new row
const r = since(before);
log(r.some((x) => x.item_id === "t02.ccc"),
    "a row with an OLD timestamp is still delivered by the rev cursor");
log(!r.some((x) => x.item_id === "t01.bbb"), "already-seen rows are not re-delivered");

// --- SEED mode: may only raise, never lower, never tombstone
const SEED_GRADE = UPSERT_GRADE.replace(
  /WHERE excluded\.updated_at >[\s\S]*$/, "WHERE excluded.state > grades.state");
bump(); db.prepare(SEED_GRADE).run("t01.bbb", 1, 99999);
log(get("t01.bbb").state === 2, "seed cannot LOWER an existing grade (2 stays 2)");
bump(); db.prepare(SEED_GRADE).run("t03.ddd", 2, 1);
log(get("t03.ddd").state === 2, "seed inserts a new row");

// --- day ticks
bump();
db.prepare(UPSERT_DAY).run("2026-09-04", "t00.xyz", 1, 1000);
log(db.prepare("SELECT done FROM day_ticks WHERE day=? AND item_id=?").get("2026-09-04", "t00.xyz").done === 1,
    "day tick inserts");
bump(); db.prepare(UPSERT_DAY).run("2026-09-04", "t00.xyz", 0, 2000);
log(db.prepare("SELECT done FROM day_ticks WHERE day=? AND item_id=?").get("2026-09-04", "t00.xyz").done === 0,
    "day un-tick writes a 0 tombstone");

console.log(L.join("\n"));
const fails = L.filter((l) => l.startsWith("FAIL")).length;
console.log(`\n${L.length - fails} passed, ${fails} failed`);
process.exit(fails ? 1 : 0);
