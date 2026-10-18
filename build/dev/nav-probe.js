(()=>{
  const t=document.body.innerText;
  const title=document.title;
  return "url: "+location.pathname+"\n"+
         "title: "+title+"\n"+
         "renders offline fallback: "+(/offline/i.test(t)?"YES":"NO")+"\n"+
         "has link back to tracker: "+(!!document.querySelector('a[href="/tracker.html"]'))+"\n"+
         "--- body ---\n"+t.slice(0,220);
})()
