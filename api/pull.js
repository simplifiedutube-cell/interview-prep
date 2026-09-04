import { requireAuth } from "../lib/auth.js";
import { db, ensureSchema, READ_REV } from "../lib/db.js";

/* GET /api/pull?since=<rev>
   Everything changed after revision `since`. since=0 returns everything, which is
   what a fresh device asks for.

   The rows and the new cursor are read in ONE transaction. Read them separately
   and a concurrent push lands in between: you would advance your cursor past rows
   you never received and lose them permanently and silently. */
export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "GET") return res.status(405).json({ error: "method not allowed" });
  if (!(await requireAuth(req, res))) return;

  try {
    await ensureSchema();
    const since = Math.max(0, Number(req.query.since) || 0);

    const [g, d, m] = await db().batch([
      { sql: "SELECT item_id, state FROM grades WHERE rev > ?", args: [since] },
      { sql: "SELECT day, item_id, done FROM day_ticks WHERE rev > ?", args: [since] },
      { sql: READ_REV, args: [] },
    ], "read");

    return res.status(200).json({
      rev: Number(m.rows[0].n),
      grades: g.rows.map((r) => [r.item_id, Number(r.state)]),
      days: d.rows.map((r) => [r.day, r.item_id, Number(r.done)]),
      serverNow: Date.now(),
    });
  } catch (e) {
    console.error("pull", e);
    return res.status(500).json({ error: "db" });
  }
}
