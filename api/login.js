import { signToken, setCookie, MAX_AGE } from "../lib/auth.js";
import { db, ensureSchema } from "../lib/db.js";

/* Constant-time compare so a wrong passphrase leaks nothing through timing. */
function safeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const WINDOW = 15 * 60e3;   // failures are counted over 15 minutes
const TRIES = 8;            // then that IP is locked out for the rest of the window

function clientIp(req) {
  return String(
    req.headers["x-real-ip"] ||
    String(req.headers["x-forwarded-for"] || "").split(",")[0] || "unknown",
  ).trim().slice(0, 45);
}

/* Rate limiting is a nice-to-have; SIGNING IN IS NOT.

   An in-memory counter is useless across serverless instances, so the counter
   lives in the database — but that must never make the database a hard dependency
   of authentication. db() throws when TURSO_DATABASE_URL is absent, so every touch
   of it here is best-effort: a missing or broken database degrades to "no rate
   limiting", never to "nobody can sign in".

   This is exactly how it broke the first time: db() was called outside the try,
   so an unconfigured Turso integration crashed the function and the login page
   could only show a generic failure. */
async function limiter() {
  try {
    const c = db();
    await ensureSchema();
    return c;
  } catch (e) {
    console.error("login: rate-limit store unavailable, continuing without it", e);
    return null;
  }
}

export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  try {
    if (req.method !== "POST") return res.status(405).json({ error: "method not allowed" });

    const secret = process.env.AUTH_SECRET;
    const expected = process.env.APP_PASSPHRASE;
    if (!secret || !expected) {
      return res.status(500).json({
        error: "server not configured: set APP_PASSPHRASE and AUTH_SECRET in Vercel, then redeploy",
      });
    }

    const body = typeof req.body === "string" ? safeParse(req.body) : req.body || {};
    const given = typeof body.passphrase === "string" ? body.passphrase : "";
    const ip = clientIp(req);
    const now = Date.now();
    const c = await limiter();

    let row = null;
    if (c) {
      try {
        row = (await c.execute({ sql: "SELECT n, first FROM login_fail WHERE ip = ?", args: [ip] })).rows[0];
      } catch (e) { console.error("login/read", e); }
    }
    const openWindow = row && now - Number(row.first) < WINDOW;
    if (openWindow && Number(row.n) >= TRIES) {
      return res.status(429).json({
        error: "too many attempts",
        retryIn: Math.ceil((WINDOW - (now - Number(row.first))) / 1000),
      });
    }

    await sleep(250);        // a floor on the cost of a single guess

    if (!safeEqual(given, expected)) {
      if (c) {
        try {
          await c.execute(openWindow
            ? { sql: "UPDATE login_fail SET n = n + 1 WHERE ip = ?", args: [ip] }
            : { sql: "INSERT INTO login_fail (ip, n, first) VALUES (?, 1, ?) " +
                     "ON CONFLICT(ip) DO UPDATE SET n = 1, first = excluded.first", args: [ip, now] });
        } catch (e) { console.error("login/count", e); }
      }
      return res.status(401).json({ error: "wrong passphrase" });
    }

    if (c) {
      try { await c.execute({ sql: "DELETE FROM login_fail WHERE ip = ?", args: [ip] }); }
      catch (e) { console.error("login/clear", e); }
    }

    res.setHeader("Set-Cookie", setCookie(await signToken(secret), MAX_AGE));
    return res.status(200).json({ ok: true, rateLimited: !!c });
  } catch (e) {
    /* Anything unexpected still answers as JSON. A crash here returns Vercel's
       text/plain FUNCTION_INVOCATION_FAILED, which the login page can only report
       as a generic failure — the caller learns nothing and neither do you. */
    console.error("login", e);
    return res.status(500).json({ error: "sign-in failed: " + String(e && e.message || e) });
  }
}

function safeParse(s) {
  try { return JSON.parse(s); } catch { return {}; }
}
