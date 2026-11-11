const { chromium } = require('playwright');
const S = process.argv[2];
(async () => {
  const b = await chromium.launch();
  // 1. harnesses
  for (const h of ['_func','_regress','_sync']) {
    const p = await b.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.goto('http://localhost:8099/'+h+'.html');
    await p.waitForFunction(()=>document.title==='DONE',null,{timeout:30000}).catch(()=>{});
    const out = await p.textContent('#out');
    console.log('=== '+h+'\n'+out+(errs.length?'\nPAGEERR '+errs.join(' | '):''));
    await p.close();
  }
  // 2. ids: before (file) vs after (served)
  const ids = async (url) => { const p=await b.newPage(); await p.goto(url); await p.waitForTimeout(500);
    const r = await p.$$eval('li.item[data-id]', ls=>ls.map(l=>l.dataset.id)); await p.close(); return r; };
  const before = await ids('file://'+S+'/before/index.html');
  const after = await ids('http://localhost:8099/tracker.html');
  const A = new Set(after); const lost = before.filter(i=>!A.has(i));
  console.log(`ids before=${before.length} after=${after.length} lost=${lost.length} new=${after.length-before.length}`);
  await b.close();
})();
