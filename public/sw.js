/* Precache everything, serve cache-first. Because the whole site is precached,
   cache-first is always a hit — instant and offline by construction. Correctness
   comes from the version bump, not from revalidation.
   BUILD changes whenever any file changes, which is the entire update mechanism. */
const BUILD = "20261020-e176acea";
const CACHE = "prep-" + BUILD;
const PRECACHE = [
  "/",
  "/404.html",
  "/ai-engineer-interviews/checklist.html",
  "/ai-engineer-interviews/real-questions.html",
  "/ai-engineer-interviews/resources.html",
  "/answers/01-latency-and-cost.html",
  "/answers/02-relevance-and-agent-success.html",
  "/answers/03-turnaround-and-effort.html",
  "/answers/04-sklearn-accuracy.html",
  "/answers/05-scale-and-narrative.html",
  "/answers/metric-defence.html",
  "/assets/apple-touch-icon.png",
  "/assets/favicon-32.png",
  "/assets/flow-01.svg",
  "/assets/flow-02.svg",
  "/assets/flow-03.svg",
  "/assets/flow-04.svg",
  "/assets/icon-192-maskable.png",
  "/assets/icon-192.png",
  "/assets/icon-512-maskable.png",
  "/assets/icon-512.png",
  "/assets/icon.svg",
  "/assets/site.9a022d4b.css",
  "/assets/site.d62a8d99.js",
  "/assets/sync.bf928ee9.js",
  "/diagrams/01-aml-ctf-compliance-rag.svg",
  "/diagrams/02-indic-voice-agent.svg",
  "/diagrams/03-enterprise-rag-knowledge-assistant.svg",
  "/diagrams/04-agentic-coding-assistant.svg",
  "/diagrams/05-offline-air-gapped-training-envs.svg",
  "/diagrams/06-student-performance-ml-platform.svg",
  "/diagrams/index.html",
  "/index.html",
  "/library.html",
  "/login.html",
  "/manifest.webmanifest",
  "/offline.html",
  "/questions.html",
  "/resources.html",
  "/robots.txt",
  "/story-bank.html",
  "/tracker.html"
];

self.addEventListener("install", (e) => {
  /* NOT caches.addAll().

     addAll() follows redirects and stores the FINAL response under the ORIGINAL
     url. With an auth gate in front, an install that runs while the cookie is
     expired would fetch /index.html, follow the 302, and cache the LOGIN PAGE
     under /index.html — and under all 47 urls. This service worker has no
     revalidation path by design, so that state is permanent and the user has no
     way back short of clearing site data.

     Rejecting a redirected response fails the install instead. That is the good
     outcome: the previous worker stays active, the cached site keeps working, and
     site.js's hourly reg.update() retries once you are signed in again. */
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    for (let i = 0; i < PRECACHE.length; i += 6) {
      await Promise.all(PRECACHE.slice(i, i + 6).map(async (u) => {
        const res = await fetch(u, { cache: "reload", credentials: "same-origin" });
        if (!res.ok || res.redirected) {
          throw new Error("precache " + u + " -> " + res.status +
                          (res.redirected ? " (redirected)" : ""));
        }
        await c.put(u, res);
      }));
    }
  })());
  /* deliberately NO skipWaiting() — the page offers the update instead */
});

self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener("message", (e) => {
  if (e.data === "SKIP_WAITING") self.skipWaiting();
});

self.addEventListener("fetch", (e) => {
  const r = e.request;
  if (r.method !== "GET") return;
  const url = new URL(r.url);
  /* never intercept cross-origin — an opaque response must not enter the cache */
  if (url.origin !== location.origin) return;
  /* never intercept the API: cache-first would pin a stale /api/pull for ever and
     sync would silently stop working */
  if (url.pathname.startsWith("/api/")) return;

  e.respondWith((async () => {
    const c = await caches.open(CACHE);
    const hit = await c.match(r, { ignoreSearch: true });
    if (hit) return hit;
    try {
      const net = await fetch(r);
      if (net.ok) c.put(r, net.clone());
      return net;
    } catch (err) {
      if (r.mode === "navigate") {
        return (await c.match("/offline.html")) || Response.error();
      }
      return Response.error();
    }
  })());
});
