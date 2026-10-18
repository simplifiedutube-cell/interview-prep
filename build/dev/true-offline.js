(async()=>{
  const L=[], log=(ok,m)=>L.push((ok?"PASS  ":"FAIL  ")+m);
  log(location.pathname==="/tracker.html", "landed on /tracker.html with the server down");
  log(document.querySelectorAll("li.item").length>400,
      `tracker rendered from cache: ${document.querySelectorAll("li.item").length} items`);
  log(!!navigator.serviceWorker.controller, "page is controlled by the service worker");
  for(const u of ["/library.html","/questions.html","/resources.html","/diagrams/index.html"]){
    try{ const r=await fetch(u); const t=await r.text();
         log(r.ok&&t.length>1000, `served from cache with no server: ${u} (${t.length}B)`); }
    catch(e){ log(false, `${u} threw ${e.message}`); }
  }
  return L.join("\n");
})()
