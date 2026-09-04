/* Turso (libSQL) client + idempotent schema bootstrap.

   The /web entrypoint is fetch-only with zero native dependencies, which is what
   makes it safe on Vercel — the default entrypoint pulls native bindings that are
   fragile in serverless images. */
import { createClient } from "@libsql/client/web";

let _client = null;
let _schemaReady = null;

export function db() {
  /* Test seam: build/dev/api-test.mjs injects a node:sqlite-backed adapter here so
     the handlers can be exercised end to end without a live Turso database. Unset
     in production, where this branch never runs. */
  if (globalThis.__PREP_DB__) return globalThis.__PREP_DB__;
  if (_client) return _client;
  const url = process.env.TURSO_DATABASE_URL;
  const authToken = process.env.TURSO_AUTH_TOKEN;
  if (!url) throw new Error("TURSO_DATABASE_URL is not set — add the Turso integration in Vercel");
  _client = createClient({ url, authToken });
  return _client;
}

/* ---------------------------------------------------------------------------
   TWO CLOCKS, ON PURPOSE.

   `updated_at` is the client's wall clock (clamped) and decides CONFLICTS:
   whoever edited an item most recently wins it.

   `rev` is a server-assigned counter and drives the PULL CURSOR. It must not be
   the timestamp. A device that ticks something offline at 09:00 and syncs at
   18:00 writes a row whose updated_at is 09:00 — in the past. Any other device
   whose cursor had already passed 09:00 would never see that row again. Using a
   monotonic server counter makes "everything I have not seen yet" exact,
   regardless of when the edit was actually made or by which clock.

   `state = 0` / `done = 0` rows are TOMBSTONES and are never deleted. Without
   them, un-ticking on one device could not propagate: the other device would
   simply re-push its stale value on the next sync.
   --------------------------------------------------------------------------- */
const SCHEMA = [
  `CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, n INTEGER NOT NULL)`,
  `INSERT OR IGNORE INTO meta (k, n) VALUES ('rev', 0)`,
  `CREATE TABLE IF NOT EXISTS grades (
     item_id    TEXT PRIMARY KEY,
     state      INTEGER NOT NULL,
     updated_at INTEGER NOT NULL,
     rev        INTEGER NOT NULL
   )`,
  `CREATE TABLE IF NOT EXISTS day_ticks (
     day        TEXT NOT NULL,
     item_id    TEXT NOT NULL,
     done       INTEGER NOT NULL,
     updated_at INTEGER NOT NULL,
     rev        INTEGER NOT NULL,
     PRIMARY KEY (day, item_id)
   )`,
  `CREATE INDEX IF NOT EXISTS grades_rev    ON grades(rev)`,
  `CREATE INDEX IF NOT EXISTS day_ticks_rev ON day_ticks(rev)`,
  `CREATE TABLE IF NOT EXISTS login_fail (
     ip TEXT PRIMARY KEY, n INTEGER NOT NULL, first INTEGER NOT NULL
   )`,
];

export function ensureSchema() {
  if (!_schemaReady) {
    _schemaReady = db().batch(SCHEMA, "write").catch((e) => {
      _schemaReady = null;                 // let the next request retry
      throw e;
    });
  }
  return _schemaReady;
}

export const BUMP_REV = "UPDATE meta SET n = n + 1 WHERE k = 'rev'";
export const READ_REV = "SELECT n FROM meta WHERE k = 'rev'";

/* Last-write-wins, resolved in SQL so two devices racing the same item converge
   without a read-modify-write round trip. Equal timestamps tie-break to the
   higher grade — the same benefit-of-the-doubt the v2→v3 migration chose.

   A consequence worth naming: re-sending an op that already won changes nothing
   and does not bump `rev`. That idempotency is what makes a retry after a failed
   or unacknowledged push safe. */
export const UPSERT_GRADE = `
  INSERT INTO grades (item_id, state, updated_at, rev)
  VALUES (?, ?, ?, (SELECT n FROM meta WHERE k='rev'))
  ON CONFLICT(item_id) DO UPDATE SET
    state = excluded.state, updated_at = excluded.updated_at, rev = excluded.rev
  WHERE excluded.updated_at >  grades.updated_at
     OR (excluded.updated_at = grades.updated_at AND excluded.state > grades.state)`;

export const UPSERT_DAY = `
  INSERT INTO day_ticks (day, item_id, done, updated_at, rev)
  VALUES (?, ?, ?, ?, (SELECT n FROM meta WHERE k='rev'))
  ON CONFLICT(day, item_id) DO UPDATE SET
    done = excluded.done, updated_at = excluded.updated_at, rev = excluded.rev
  WHERE excluded.updated_at >  day_ticks.updated_at
     OR (excluded.updated_at = day_ticks.updated_at AND excluded.done > day_ticks.done)`;

/* SEED variants: the first push from a device that has never synced.

   Plain last-write-wins is wrong for that push. Two devices each holding real
   progress, neither yet synced: whichever syncs SECOND stamps a later clock on
   every row and would erase the first one's work. The seed predicate can only
   RAISE a value, so the result is the union of both devices — which is what a
   person means by "merge my two devices". Zero values never reach here. */
export const UPSERT_GRADE_SEED = `
  INSERT INTO grades (item_id, state, updated_at, rev)
  VALUES (?, ?, ?, (SELECT n FROM meta WHERE k='rev'))
  ON CONFLICT(item_id) DO UPDATE SET
    state = excluded.state, updated_at = excluded.updated_at, rev = excluded.rev
  WHERE excluded.state > grades.state`;

export const UPSERT_DAY_SEED = `
  INSERT INTO day_ticks (day, item_id, done, updated_at, rev)
  VALUES (?, ?, ?, ?, (SELECT n FROM meta WHERE k='rev'))
  ON CONFLICT(day, item_id) DO UPDATE SET
    done = excluded.done, updated_at = excluded.updated_at, rev = excluded.rev
  WHERE excluded.done > day_ticks.done`;
