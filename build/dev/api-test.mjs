/* End-to-end test of the real api/*.js handlers.

   A node:sqlite adapter is injected in place of the Turso client, so the handlers
   run their genuine SQL, auth and validation paths without a live database. */
import { DatabaseSync } from "node:sqlite";

const sql = new DatabaseSync(":memory:");
const norm = (r) => ({ ...r });

/* Minimal stand-in for the libSQL client surface the handlers actually use. */
globalThis.__PREP_DB__ = {
  async execute(q) {
    const st = sql.prepare(q.sql);
    const read = /^\s*select/i.test(q.sql);
    return read ? { rows: st.all(...(q.args || [])).map(norm) } : (st.run(...(q.args || [])), { rows: [] });
  },
  async batch(stmts) {
    const out = [];
    sql.exec("BEGIN");
    try {
      for (const s of stmts) {
        const q = typeof s === "string" ? { sql: s, args: [] } : s;
        out.push(await this.execute(q));
      }
      sql.exec("COMMIT");
    } catch (e) { sql.exec("ROLLBACK"); throw e; }
    return out;
  },
};

process.env.AUTH_SECRET = "test-secret-value-at-least-24-chars";
process.env.APP_PASSPHRASE = "correct horse battery staple";

const login = (await import("../../api/login.js")).default;
const pull = (await import("../../api/pull.js")).default;
const push = (await import("../../api/push.js")).default;

const L = [];
const log = (ok, m) => L.push((ok ? "PASS  " : "FAIL  ") + m);

function mk(opts = {}) {
  const res = {
    _s: 200, _j: null, _h: {},
    status(c) { this._s = c; return this; },
    json(o) { this._j = o; return this; },
    setHeader(k, v) { this._h[k.toLowerCase()] = v; },
  };
  const req = {
    method: opts.method || "GET",
    headers: Object.assign({ host: "x.test" }, opts.headers || {}),
    query: opts.query || {},
    body: opts.body,
  };
  return [req, res];
}
const cookieOf = (res) => String(res._h["set-cookie"] || "").split(";")[0];

// ---------- auth ----------
let [q, r] = mk({ method: "POST", body: { passphrase: "wrong" } });
await login(q, r);
log(r._s === 401, `wrong passphrase -> 401 (got ${r._s})`);

[q, r] = mk({ method: "GET" });
await login(q, r);
log(r._s === 405, `GET /api/login -> 405 (got ${r._s})`);

[q, r] = mk({ method: "POST", body: { passphrase: "correct horse battery staple" } });
await login(q, r);
const AUTH = cookieOf(r);
log(r._s === 200 && AUTH.startsWith("prep_auth="), `correct passphrase -> 200 + cookie`);
log(/HttpOnly/i.test(res_h(r)) && /SameSite=Lax/i.test(res_h(r)), "cookie is HttpOnly + SameSite=Lax");
function res_h(x) { return String(x._h["set-cookie"] || ""); }

[q, r] = mk({ method: "GET", query: { since: "0" } });
await pull(q, r);
log(r._s === 401, `pull without a cookie -> 401 (got ${r._s})`);

[q, r] = mk({ method: "POST", body: { grades: [["t01.aaa", 2, Date.now()]] } });
await push(q, r);
log(r._s === 401, `push without a cookie -> 401 (got ${r._s})`);

const AUTHED = { cookie: AUTH, host: "x.test" };

// ---------- push / pull round trip ----------
const now = Date.now();
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.aaa", 2, now]], days: [["2026-09-04", "t00.bbb", 1, now]] } });
await push(q, r);
log(r._s === 200 && r._j.rev === 1, `push -> 200, rev ${r._j && r._j.rev} (want 1)`);

[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: "0" } });
await pull(q, r);
log(r._s === 200 && r._j.grades.length === 1 && r._j.days.length === 1, "pull since=0 returns both rows");
log(r._j.grades[0][0] === "t01.aaa" && r._j.grades[0][1] === 2, "grade round-tripped intact");

[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: String(r._j.rev) } });
await pull(q, r);
log(r._j.grades.length === 0 && r._j.days.length === 0, "pull at the current cursor returns nothing");

// ---------- idempotent replay ----------
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.aaa", 2, now]] } });
await push(q, r);
const revAfterReplay = r._j.rev;
[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: "1" } });
await pull(q, r);
log(r._j.grades.length === 0, "replaying a winning op delivers nothing to other devices");

// ---------- tombstone ----------
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.aaa", 0, now + 10]] } });
await push(q, r);
[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: String(revAfterReplay) } });
await pull(q, r);
log(r._j.grades.some((g) => g[0] === "t01.aaa" && g[1] === 0), "un-tick is delivered as a 0 row, not an absence");

// ---------- clock clamp ----------
/* Assert the stored timestamp directly: a device three days fast must not be able
   to win every conflict for the next three days. */
const far = Date.now() + 9e12;
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.ccc", 2, far]] } });
await push(q, r);
const stored = sql.prepare("SELECT updated_at FROM grades WHERE item_id='t01.ccc'").get().updated_at;
log(Number(stored) < Date.now() + 6 * 60e3,
    `far-future timestamp clamped to ~now+5min (stored ${Number(stored) - Date.now()}ms ahead, sent ${far - Date.now()}ms)`);
/* And the accepted cost of clamping, asserted rather than left implicit: a write
   made INSIDE the 5-minute ceiling still loses to the skewed one. The damage is
   bounded to 5 minutes instead of the 3 days the device's clock claimed — and a
   stale device losing a tie is recoverable by re-ticking, whereas a lost write
   is not. */
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.ccc", 1, Date.now() + 1000]] } });
await push(q, r);
[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: "0" } });
await pull(q, r);
const ccc = r._j.grades.find((g) => g[0] === "t01.ccc");
log(ccc && ccc[1] === 2,
    "a write inside the 5-min ceiling still loses to the clamped one (the bounded, documented cost)");

// ---------- seed mode ----------
[q, r] = mk({ method: "POST", headers: AUTHED, body: { mode: "seed", grades: [["t01.ddd", 2, now]] } });
await push(q, r);
[q, r] = mk({ method: "POST", headers: AUTHED, body: { mode: "seed", grades: [["t01.ddd", 1, now + 99999]] } });
await push(q, r);
[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: "0" } });
await pull(q, r);
log(r._j.grades.find((g) => g[0] === "t01.ddd")[1] === 2, "seed mode cannot LOWER a grade, even with a newer timestamp");

[q, r] = mk({ method: "POST", headers: AUTHED, body: { mode: "seed", grades: [["t01.eee", 0, now]] } });
await push(q, r);
[q, r] = mk({ method: "GET", headers: AUTHED, query: { since: "0" } });
await pull(q, r);
log(!r._j.grades.some((g) => g[0] === "t01.eee"), "seed mode never writes a tombstone");

// ---------- validation ----------
[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["../etc/passwd", 1, now]] } });
await push(q, r);
log(r._s === 400, `malformed item id -> 400 (got ${r._s})`);

[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: [["t01.aaa", 7, now]] } });
await push(q, r);
log(r._s === 400, `out-of-range state -> 400 (got ${r._s})`);

[q, r] = mk({ method: "POST", headers: AUTHED, body: { days: [["not-a-date", "t00.aaa", 1, now]] } });
await push(q, r);
log(r._s === 400, `malformed day -> 400 (got ${r._s})`);

[q, r] = mk({ method: "POST", headers: AUTHED, body: { grades: Array.from({ length: 7000 }, (_, i) => ["t01.x" + i, 1, now]) } });
await push(q, r);
log(r._s === 413, `7000 rows -> 413 (got ${r._s})`);

[q, r] = mk({ method: "POST", headers: Object.assign({ origin: "https://evil.test" }, AUTHED), body: { grades: [] } });
await push(q, r);
log(r._s === 403, `cross-origin push -> 403 (got ${r._s})`);

// ---------- login must NOT depend on the database ----------
/* The regression: db() used to be called outside the try block, so an
   unconfigured Turso integration crashed the function with
   FUNCTION_INVOCATION_FAILED and the login page could only say "Sign-in failed."
   Rate limiting is a nice-to-have; signing in is not. */
const realDb = globalThis.__PREP_DB__;
/* Remove the injected client entirely and leave TURSO_DATABASE_URL unset, so the
   real db() throws on its very first call — exactly what an unconfigured Turso
   integration does in production. Stubbing a throwing client is not equivalent:
   ensureSchema() memoises, so a stub would sail past on an already-resolved
   promise and the test would prove nothing. */
delete globalThis.__PREP_DB__;
delete process.env.TURSO_DATABASE_URL;
[q, r] = mk({ method: "POST", body: { passphrase: "correct horse battery staple" } });
await login(q, r);
log(r._s === 200 && cookieOf(r).startsWith("prep_auth="),
    `login still succeeds with the database unavailable -> ${r._s}`);
log(r._j && r._j.rateLimited === false, "response reports that rate limiting is degraded");

[q, r] = mk({ method: "POST", body: { passphrase: "nope" } });
await login(q, r);
log(r._s === 401, `wrong passphrase with no database -> ${r._s} (want 401, not a crash)`);
globalThis.__PREP_DB__ = realDb;

console.log(L.join("\n"));
const fails = L.filter((l) => l.startsWith("FAIL")).length;
console.log(`\n${L.length - fails} passed, ${fails} failed`);
process.exit(fails ? 1 : 0);
