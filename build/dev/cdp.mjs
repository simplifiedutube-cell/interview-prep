/* Drive headless Chrome over the DevTools Protocol.
   --dump-dom deadlocks once a service worker is in play, so evaluate directly.
     node build/dev/cdp.mjs <url> <expr-file>   */
import { spawn } from "node:child_process";
import { readFileSync, rmSync } from "node:fs";

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const url = process.argv[2];
const expr = readFileSync(process.argv[3], "utf8");
const PROF = "/tmp/cdp-prof";
if (process.argv[4] === "--fresh") { try { rmSync(PROF, { recursive: true, force: true }); } catch {} }

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const alive = async () => {
  try { await fetch("http://127.0.0.1:9333/json/version"); return true; } catch { return false; }
};
let chrome = null;
if (!(await alive())) {
  chrome = spawn(CHROME, [
    "--headless", "--disable-gpu", `--user-data-dir=${PROF}`,
    "--remote-debugging-port=9333", "--no-first-run", "--no-default-browser-check",
    "about:blank",
  ], { stdio: "ignore" });
  for (let i = 0; i < 120 && !(await alive()); i++) await sleep(250);
}
const fail = (m) => { console.log("ERROR " + m); chrome?.kill(); process.exit(1); };

let ws, id = 0;
const pending = new Map();
const send = (method, params = {}) =>
  new Promise((res, rej) => { pending.set(++id, { res, rej }); ws.send(JSON.stringify({ id, method, params })); });

try {
  let list = [];
  for (let i = 0; i < 60; i++) {
    try { list = await (await fetch("http://127.0.0.1:9333/json/list")).json(); } catch {}
    if (list.some((t) => t.type === "page")) break;
    await sleep(250);
  }
  const page = list.find((t) => t.type === "page") || fail("no page target");

  ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
  ws.onmessage = (e) => {
    const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id).res(m); pending.delete(m.id); }
  };

  await send("Page.enable");
  await send("Runtime.enable");
  await send("Page.navigate", { url });
  await sleep(4500);

  if (process.argv.includes("--offline")) {
    await send("Network.enable");
    await send("Network.emulateNetworkConditions", {
      offline: true, latency: 0, downloadThroughput: 0, uploadThroughput: 0,
    });
    await sleep(400);
  }

  const i2 = process.argv.indexOf("--nav2");
  if (i2 > -1) {
    await send("Page.navigate", { url: process.argv[i2 + 1] });
    await sleep(2500);
  }

  const r = await send("Runtime.evaluate", {
    expression: expr, awaitPromise: true, returnByValue: true,
  });
  if (r.result?.exceptionDetails) fail(JSON.stringify(r.result.exceptionDetails.exception?.description || r.result.exceptionDetails));
  console.log(r.result?.result?.value ?? JSON.stringify(r.result));
} catch (e) {
  console.log("ERROR " + (e?.message || e));
} finally {
  chrome?.kill();
  await sleep(200);
  process.exit(0);
}
