/* Signed-cookie auth, shared by the Edge middleware and the Node API functions.
   Uses WebCrypto only (globalThis.crypto), which exists in both runtimes — Node's
   `crypto` module is not available on the Edge runtime the middleware runs on. */

export const COOKIE = "prep_auth";
export const MAX_AGE = 90 * 24 * 60 * 60;          // 90 days, in seconds

const enc = new TextEncoder();

function b64url(bytes) {
  let s = "";
  for (const b of new Uint8Array(bytes)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

async function hmac(msg, secret) {
  const key = await crypto.subtle.importKey(
    "raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"],
  );
  return b64url(await crypto.subtle.sign("HMAC", key, enc.encode(msg)));
}

/** Constant-time compare. Both operands here are fixed-length base64url HMACs,
    so the length check leaks nothing and the loop runs over every character. */
function safeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/** Token is `<expiryMs>.<hmac>` — the expiry is signed, so it cannot be extended. */
export async function signToken(secret, ttlSec = MAX_AGE) {
  const exp = Date.now() + ttlSec * 1000;
  return `${exp}.${await hmac(String(exp), secret)}`;
}

export async function verifyToken(token, secret) {
  if (!token || !secret) return false;
  const dot = token.indexOf(".");
  if (dot < 1) return false;
  const exp = token.slice(0, dot);
  const sig = token.slice(dot + 1);
  if (!/^\d+$/.test(exp) || Number(exp) < Date.now()) return false;
  return safeEqual(sig, await hmac(exp, secret));
}

export function parseCookies(header) {
  const out = {};
  if (!header) return out;
  for (const part of header.split(";")) {
    const i = part.indexOf("=");
    if (i < 1) continue;
    out[part.slice(0, i).trim()] = decodeURIComponent(part.slice(i + 1).trim());
  }
  return out;
}

/* `Secure` is refused over http://localhost, which is what `vercel dev` serves —
   the cookie would be silently dropped and login would appear to succeed while
   nothing persisted. VERCEL_ENV is "development" only under `vercel dev`. */
const SECURE = () => (process.env.VERCEL_ENV === "development" ? "" : "; Secure");

export function setCookie(token, maxAge = MAX_AGE) {
  return `${COOKIE}=${token}; Path=/; Max-Age=${maxAge}; HttpOnly${SECURE()}; SameSite=Lax`;
}

export function clearCookie() {
  return `${COOKIE}=; Path=/; Max-Age=0; HttpOnly${SECURE()}; SameSite=Lax`;
}

/** Guard for the Node API handlers. Returns true when the request may proceed.
    These verify independently of the middleware, so the database stays protected
    even if the middleware is ever bypassed or misconfigured. */
export async function requireAuth(req, res) {
  const token = parseCookies(req.headers.cookie)[COOKIE];
  if (await verifyToken(token, process.env.AUTH_SECRET)) return true;
  res.status(401).json({ error: "unauthorized" });
  return false;
}
