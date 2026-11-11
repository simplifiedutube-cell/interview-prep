const { chromium } = require('playwright');
const O = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({viewport:{width:1440,height:900}});
  const p = await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8099/tracker.html'); await p.waitForTimeout(700);
  await p.screenshot({path:O+'/01-desktop-today.png'});
  // UI action 1: tick the first Today slot via a real click
  await p.locator('#t00 li.item input[type=checkbox]').first().click();
  await p.screenshot({path:O+'/02-desktop-today-ticked.png'});
  const days = await p.evaluate(()=>JSON.parse(localStorage.getItem('mt.days.v2')));
  const k=Object.keys(days).sort().pop(); console.log('after Today tick: mt.days.v2['+k+'] entries =', Object.keys(days[k]).length);
  // UI action 2: navigate via sidebar to Agents, tools & MCP
  await p.locator('nav a[data-nav="t06"]').click(); await p.waitForTimeout(300);
  await p.screenshot({path:O+'/03-desktop-t06.png'});
  // UI action 3: grade first item twice (read -> cold)
  const tri = p.locator('#t06 li.item .tri').first();
  await tri.click(); await tri.click();
  const id = await p.locator('#t06 li.item').first().getAttribute('data-id');
  const st = await p.evaluate(i=>JSON.parse(localStorage.getItem('mt.v3')).items[i], id);
  console.log('after 2 taps on first t06 item: mt.v3.items['+id+'] =', st, '(want 2)');
  await p.screenshot({path:O+'/04-desktop-t06-graded.png'});
  // new items visible
  await p.locator('#q').fill('Tasks'); await p.waitForTimeout(200);
  await p.screenshot({path:O+'/05-desktop-filter-tasks.png'});
  await p.locator('#q').fill('');
  await p.locator('nav a[data-nav="t12"]').click(); await p.waitForTimeout(300);
  await p.locator('#t12 h3', {hasText:'AI-assisted coding'}).scrollIntoViewIfNeeded();
  await p.screenshot({path:O+'/06-desktop-t12-ai-coding.png'});
  console.log('page errors:', errs.length?errs:'none');
  await ctx.close();
  // phone
  const ph = await b.newContext({viewport:{width:390,height:844}, deviceScaleFactor:2, isMobile:true, hasTouch:true});
  const q = await ph.newPage();
  await q.goto('http://localhost:8099/tracker.html#t07'); await q.waitForTimeout(700);
  await q.screenshot({path:O+'/07-phone-t07.png'});
  await q.locator('#menu').click(); await q.waitForTimeout(400);
  await q.screenshot({path:O+'/08-phone-drawer.png'});
  await q.goto('http://localhost:8099/tracker.html'); await q.waitForTimeout(500);
  await q.screenshot({path:O+'/09-phone-today.png'});
  const ov = await q.evaluate(()=>document.documentElement.scrollWidth - innerWidth);
  console.log('phone horizontal overflow px:', ov);
  await b.close();
})();
