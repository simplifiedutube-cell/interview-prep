(async()=>{
  const L=[], log=(ok,m)=>L.push((ok?"PASS  ":"FAIL  ")+m);
  const regs=await navigator.serviceWorker.getRegistrations();
  log(regs.length===1, `service worker registrations: ${regs.length} (want 1)`);
  log(regs[0] && !!regs[0].active, "worker reached active state");
  const keys=await caches.keys();
  log(keys.length===1 && keys[0].startsWith("prep-"), `cache buckets: ${JSON.stringify(keys)} (want one prep-*)`);
  if(keys[0]){
    const c=await caches.open(keys[0]), ks=await c.keys();
    log(ks.length>=40, `cached entries: ${ks.length}`);
    for(const u of ["/index.html","/library.html","/questions.html","/offline.html",
                    "/answers/05-scale-and-narrative.html","/diagrams/index.html",
                    "/manifest.webmanifest","/assets/apple-touch-icon.png","/assets/flow-01.svg","/"]){
      log(!!await c.match(u), `precached ${u}`);
    }
  }
  const m=await (await fetch("/manifest.webmanifest")).json();
  log(m.display==="standalone"&&m.start_url==="/index.html", `manifest: display=${m.display} start_url=${m.start_url}`);
  log(document.querySelector('link[rel="apple-touch-icon"]')!==null, "apple-touch-icon link present");
  log(document.querySelector('meta[name="theme-color"]').content==="#F5F6F2", "theme-color = page background");
  return L.join("\n");
})()
