(async()=>{
  const L=[], log=(ok,m)=>L.push((ok?"PASS  ":"FAIL  ")+m);
  const PAGES=["/index.html","/library.html","/questions.html","/resources.html",
               "/answers/05-scale-and-narrative.html","/accenture/question-bank.html",
               "/diagrams/index.html","/diagrams/01-aml-ctf-compliance-rag.svg",
               "/assets/flow-02.svg","/manifest.webmanifest"];
  for(const u of PAGES){
    try{
      const r=await fetch(u,{cache:"no-store"});
      const t=await r.text();
      log(r.ok && t.length>200, `offline fetch ${u} -> ${r.status}, ${t.length}B`);
    }catch(e){ log(false, `offline fetch ${u} threw ${e.message}`); }
  }
  // a URL that was never cached must fall back to offline.html, not a network error
  try{
    const r=await fetch("/definitely-not-cached.html",{mode:"navigate"});
    const t=await r.text();
    log(r.ok && /offline/i.test(t), `uncached navigation -> offline.html fallback (${r.status})`);
  }catch(e){ log(false,"uncached navigation threw "+e.message); }
  return L.join("\n");
})()
