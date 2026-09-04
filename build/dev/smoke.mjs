/* Post-deploy smoke test. Run it once the Vercel URL is live:
     node build/dev/smoke.mjs https://your-app.vercel.app 'your passphrase'
   It verifies the gate is actually closed and that sync round-trips. */
const base = (process.argv[2] || "").replace(/\/$/, "");
const pass = process.argv[3];
if (!base || !pass) {
  console.error("usage: node build/dev/smoke.mjs <url> '<passphrase>'");
  process.exit(2);
}

const L = [];
const log = (ok, m) => { L.push((ok ? "PASS  " : "FAIL  ") + m); return ok; };
const j = (r) => r.json().catch(() => ({}));

// --- the gate must be closed
let r = await fetch(base + "/answers/metric-defence.html", { redirect: "manual" });
log(r.status === 302 || r.status === 307,
    `private page without a cookie -> ${r.status} (want 302/307 to /login.html)`);
log(String(r.headers.get("location") || "").includes("/login.html"),
    `  redirect target: ${r.headers.get("location")}`);

r = await fetch(base + "/api/pull?since=0");
log(r.status === 401, `GET /api/pull without a cookie -> ${r.status} (want 401)`);

r = await fetch(base + "/login.html");
log(r.ok, `/login.html is reachable while signed out -> ${r.status}`);
r = await fetch(base + "/manifest.webmanifest");
log(r.ok, `/manifest.webmanifest reachable signed out -> ${r.status} (Add to Home Screen needs this)`);

// --- wrong passphrase
r = await fetch(base + "/api/login", {
  method: "POST", headers: { "content-type": "application/json" },
  body: JSON.stringify({ passphrase: "definitely-not-it" }), redirect: "manual",
});
log(r.status === 401, `wrong passphrase -> ${r.status} (want 401)`);

// --- correct passphrase
r = await fetch(base + "/api/login", {
  method: "POST", headers: { "content-type": "application/json" },
  body: JSON.stringify({ passphrase: pass }), redirect: "manual",
});
const setCookie = r.headers.get("set-cookie") || "";
const cookie = setCookie.split(";")[0];
if (!log(r.status === 200 && cookie.startsWith("prep_auth="),
         `correct passphrase -> ${r.status}${r.status !== 200 ? " " + JSON.stringify(await j(r)) : ""}`)) {
  console.log(L.join("\n")); process.exit(1);
}
log(/HttpOnly/i.test(setCookie) && /Secure/i.test(setCookie) && /SameSite=Lax/i.test(setCookie),
    "cookie is HttpOnly + Secure + SameSite=Lax");

const H = { cookie, "content-type": "application/json" };

// --- the gate opens
r = await fetch(base + "/answers/metric-defence.html", { headers: { cookie }, redirect: "manual" });
log(r.ok, `private page WITH the cookie -> ${r.status}`);

// --- sync round trip, using a throwaway id
const id = "t99.smoke" + Math.floor(Math.random() * 1e4).toString(36);
const now = Date.now();
r = await fetch(base + "/api/push", {
  method: "POST", headers: H, body: JSON.stringify({ grades: [[id, 2, now]] }),
});
const pushed = await j(r);
log(r.ok && typeof pushed.rev === "number", `push -> ${r.status}, rev ${pushed.rev}`);

r = await fetch(base + "/api/pull?since=0", { headers: { cookie } });
const pulled = await j(r);
log(r.ok && (pulled.grades || []).some((g) => g[0] === id && g[1] === 2),
    `pull returns the row just written (${(pulled.grades || []).length} grades total)`);

// --- tombstone
r = await fetch(base + "/api/push", {
  method: "POST", headers: H, body: JSON.stringify({ grades: [[id, 0, now + 1000]] }),
});
r = await fetch(base + "/api/pull?since=0", { headers: { cookie } });
const after = await j(r);
log((after.grades || []).some((g) => g[0] === id && g[1] === 0),
    "un-tick comes back as a 0 row, not an absence (tombstone works)");

console.log("\n" + L.join("\n"));
const fails = L.filter((l) => l.startsWith("FAIL")).length;
console.log(`\n${L.length - fails} passed, ${fails} failed`);
if (!fails) console.log(`\nNote: the smoke row ${id} is left in the database and is harmless —\nit matches no real item, so nothing renders it.`);
process.exit(fails ? 1 : 0);
