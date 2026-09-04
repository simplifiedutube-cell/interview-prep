import { requireAuth } from "../lib/auth.js";
import {
  db, ensureSchema, BUMP_REV, READ_REV,
  UPSERT_GRADE, UPSERT_DAY, UPSERT_GRADE_SEED, UPSERT_DAY_SEED,
} from "../lib/db.js";

const MAX_ROWS = 6000;          // a full restore is ~2200; this is abuse protection
const SKEW_AHEAD = 5 * 60e3;    // tolerate 5 min of clock drift into the future
const SKEW_BEHIND = 400 * 864e5;

/* Clamp rather than reject or overwrite.

   Stamping server-side would reorder offline edits — a tick made on the phone at
   09:00 and synced at 18:00 would outrank a laptop edit made at 12:00. Trusting
   the client outright lets one skewed clock win every conflict for ever. Clamping
   keeps offline ordering honest while bounding what a wrong clock can do.

   Tradeoff, stated: a device running days BEHIND will lose ties it might deserve.
   That is recoverable by re-ticking; a lost write is not. */
const stamp = (v, now) => {
  const n = Number(v);
  if (!Number.isFinite(n) || n <= 0) return now;
  return Math.max(now - SKEW_BEHIND, Math.min(n, now + SKEW_AHEAD));
};

const GRADE_KEY = /^t\d{2}\.[0-9a-z]{1,10}$/;      // idFor(): track + "." + djb2 base36
const DAY_KEY = /^\d{4}-\d{2}-\d{2}$/;

export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") return res.status(405).json({ error: "method not allowed" });

  /* SameSite=Lax already blocks cross-site POSTs; this is the belt to that brace. */
  const origin = req.headers.origin;
  if (origin) {
    try {
      if (new URL(origin).host !== req.headers.host) {
        return res.status(403).json({ error: "origin" });
      }
    } catch { return res.status(403).json({ error: "origin" }); }
  }
  if (!(await requireAuth(req, res))) return;

  try {
    await ensureSchema();
    const now = Date.now();
    const body = typeof req.body === "string" ? JSON.parse(req.body) : req.body || {};
    const grades = Array.isArray(body.grades) ? body.grades : [];
    const days = Array.isArray(body.days) ? body.days : [];
    /* "seed" is the first push from a device that has never synced. It may only
       RAISE a grade and never writes a tombstone, so two devices that each hold
       real progress merge to the union instead of the loser being erased. */
    const seed = body.mode === "seed";

    if (grades.length + days.length > MAX_ROWS) {
      return res.status(413).json({ error: "too-many-rows", max: MAX_ROWS });
    }

    const stmts = [{ sql: BUMP_REV, args: [] }];
    for (const row of grades) {
      if (!Array.isArray(row) || row.length < 2) continue;
      const [id, state, ts] = row;
      if (typeof id !== "string" || !GRADE_KEY.test(id)) return res.status(400).json({ error: "bad-key" });
      const v = Number(state) | 0;
      if (v < 0 || v > 2) return res.status(400).json({ error: "bad-value" });
      if (seed && v === 0) continue;
      stmts.push({ sql: seed ? UPSERT_GRADE_SEED : UPSERT_GRADE, args: [id, v, stamp(ts, now)] });
    }
    for (const row of days) {
      if (!Array.isArray(row) || row.length < 3) continue;
      const [day, id, done, ts] = row;
      if (typeof day !== "string" || !DAY_KEY.test(day)) return res.status(400).json({ error: "bad-day" });
      if (typeof id !== "string" || !GRADE_KEY.test(id)) return res.status(400).json({ error: "bad-key" });
      const v = Number(done) ? 1 : 0;
      if (seed && v === 0) continue;
      stmts.push({ sql: seed ? UPSERT_DAY_SEED : UPSERT_DAY, args: [day, id, v, stamp(ts, now)] });
    }

    stmts.push({ sql: READ_REV, args: [] });
    const out = await db().batch(stmts, "write");
    return res.status(200).json({
      rev: Number(out[out.length - 1].rows[0].n),
      written: stmts.length - 2,
      serverNow: now,
    });
  } catch (e) {
    /* These endpoints sit behind the auth gate, so the real reason is safe to
       return — and "db" on its own sends you hunting with no information. */
    console.error("push", e);
    return res.status(500).json({ error: "db", detail: String((e && e.message) || e) });
  }
}
