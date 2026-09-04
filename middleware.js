/* The access gate, over both pages and API.

   Vercel Hobby cannot password-protect a production URL, so this is the only thing
   standing between the public internet and the metric-defence dossier, the comp
   targets, the client architectures — and write access to the database.

   NOTE: this is the NON-Next.js middleware API. It uses `@vercel/functions`, not
   `next/server`; almost every tutorial online shows the Next form (NextResponse),
   which does not work here. */
import { next } from "@vercel/functions";
import { COOKIE, parseCookies, verifyToken } from "./lib/auth.js";

/* Matched on everything, then filtered in code. Expressing the exclusions as a
   matcher regex is possible but brittle, and getting it subtly wrong fails OPEN.
   The extra invocations for static assets are trivial against the Hobby limit. */
export const config = { matcher: "/(.*)" };

/* Reachable while logged out. /login.html and its assets obviously must be, and so
   must sw.js and the manifest — if the service worker script itself were redirected
   to the login page, registration would fail outright. */
const OPEN = new Set([
  "/login.html",
  "/offline.html",
  "/sw.js",
  "/manifest.webmanifest",
  "/robots.txt",
  "/favicon.ico",
  "/api/login",
]);

const isOpen = (p) => OPEN.has(p) || p.startsWith("/assets/");

export default async function middleware(request) {
  const url = new URL(request.url);
  const path = url.pathname;

  if (isOpen(path)) return next();

  const token = parseCookies(request.headers.get("cookie"))[COOKIE];
  if (await verifyToken(token, process.env.AUTH_SECRET)) return next();

  if (path.startsWith("/api/")) {
    return new Response(JSON.stringify({ error: "unauthorized" }), {
      status: 401,
      headers: { "content-type": "application/json", "cache-control": "no-store" },
    });
  }

  const to = new URL("/login.html", request.url);
  if (path !== "/" && path !== "/index.html") to.searchParams.set("next", path + url.search);
  return Response.redirect(to, 307);
}
