/* Server sync for the tracker.

   localStorage stays the instant-render path and the offline cache; the database
   is the shared source of truth. This file is additive: if it fails to load, or
   the API is unreachable, the tracker behaves exactly as it did before.

   Changes are detected by DIFFING against a shadow copy inside save()/saveDays()
   rather than by hooking each toggle handler. Every mutation path in the tracker
   already funnels through those two functions — taps, reset, re-grade,
   reset-today and Restore — so one integration point covers all of them and a
   future code path cannot silently escape sync. */
(function () {
  "use strict";

  var CUR = "mt.sync.rev", OUT = "mt.sync.out", SEED = "mt.sync.seeded", AT = "mt.sync.at";
  var PRUNE_DAYS = 120;

  var host = null, out = {}, shG = {}, shD = {};
  var timer = null, inflight = false, backoff = 2000, stopped = false;

  function ls(k, d) { try { return localStorage.getItem(k); } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var rev = function () { return Math.max(0, +ls(CUR, 0) || 0); };

  function persist() { set(OUT, JSON.stringify(out)); }
  function pending() { var n = 0; for (var k in out) n++; return n; }

  /* ---------- shadows: what we believe the stores looked like last time ---------- */
  function snap() {
    shG = {};
    for (var id in host.state) shG[id] = host.state[id] | 0;
    shD = {};
    for (var d in host.days) {
      shD[d] = {};
      for (var i in host.days[d]) if (host.days[d][i]) shD[d][i] = 1;
    }
  }

  function mark(key, v) { out[key] = { v: v, t: Date.now() }; }

  function diffGrades() {
    var changed = false, id;
    for (id in host.state) {
      var v = host.state[id] | 0;
      if ((shG[id] | 0) !== v) { mark("g|" + id, v); shG[id] = v; changed = true; }
    }
    for (id in shG) {
      if (!(id in host.state) && shG[id] !== 0) { mark("g|" + id, 0); shG[id] = 0; changed = true; }
    }
    return changed;
  }

  function diffDays() {
    var changed = false, d, i;
    for (d in host.days) {
      var cur = host.days[d] || {}, sh = shD[d] || (shD[d] = {});
      for (i in cur) if (cur[i] && !sh[i]) { mark("d|" + d + "|" + i, 1); sh[i] = 1; changed = true; }
      for (i in sh) if (sh[i] && !cur[i]) { mark("d|" + d + "|" + i, 0); delete sh[i]; changed = true; }
    }
    /* A day that vanished entirely is local retention pruning, NOT an edit.
       Emitting tombstones for it would delete another device's history. */
    for (d in shD) if (!(d in host.days)) delete shD[d];
    return changed;
  }

  /* ---------- merge ---------- */
  function dayStore(d) {
    if (d === host.TODAY) {
      /* days[TODAY] IS todayStore, and every rendered Today checkbox closes over
         that exact object. Reassigning it detaches all of them and ticks stop
         persisting — a bug this tracker has already shipped once. Write the name. */
      if (host.days[host.TODAY] !== host.todayStore) host.days[host.TODAY] = host.todayStore;
      return host.todayStore;
    }
    return host.days[d] || (host.days[d] = {});
  }

  function pruneDays() {
    var keys = [], d;
    for (d in host.days) keys.push(d);
    if (keys.length <= PRUNE_DAYS) return;
    keys.sort();
    for (var i = 0; i < keys.length - PRUNE_DAYS; i++) {
      if (keys[i] !== host.TODAY) delete host.days[keys[i]];
    }
  }

  function applyRows(grades, days) {
    var touched = false, k, i;
    for (i = 0; i < grades.length; i++) {
      var gid = grades[i][0], gv = grades[i][1] | 0;
      if (out["g|" + gid]) continue;          /* an un-acked local write outranks the server */
      if ((host.state[gid] | 0) === gv) continue;
      if (gv) host.state[gid] = gv; else delete host.state[gid];
      touched = true;
    }
    for (i = 0; i < days.length; i++) {
      var dd = days[i][0], did = days[i][1], dv = days[i][2] | 0;
      if (out["d|" + dd + "|" + did]) continue;
      var m = dayStore(dd);
      if (!!m[did] === !!dv) continue;
      if (dv) m[did] = 1; else delete m[did];
      touched = true;
    }
    if (!touched) return false;
    pruneDays();
    snap();                                   /* re-baseline BEFORE saving, so the */
    host.save(); host.saveDays();             /* diff does not re-emit what we just got */
    host.repaintAll();
    return true;
  }

  /* ---------- transport ---------- */
  function payload() {
    var g = [], d = [], k;
    for (k in out) {
      var e = out[k];
      if (k.charAt(0) === "g") { g.push([k.slice(2), e.v, e.t]); }
      else { var p = k.indexOf("|", 2); d.push([k.slice(2, p), k.slice(p + 1), e.v, e.t]); }
    }
    return { grades: g, days: d };
  }

  function gone() { location.replace("/login.html?next=" + encodeURIComponent(location.pathname)); }

  async function req(url, opts) {
    var r = await fetch(url, Object.assign({ credentials: "same-origin", cache: "no-store" }, opts));
    if (r.status === 401) { stopped = true; note("Signed out."); gone(); throw new Error("auth"); }
    if (!r.ok) throw new Error("http " + r.status);
    return r.json();
  }

  async function sync() {
    if (inflight || stopped) return;
    if (navigator.onLine === false) { note(); return; }
    inflight = true;
    try {
      var seeding = !ls(SEED, "") && pending() > 0;
      var snapshot = {}, k;
      for (k in out) snapshot[k] = out[k].t;

      if (pending()) {
        var body = payload();
        if (seeding) body.mode = "seed";
        await req("/api/push", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(body),
        });
        /* Compare-and-delete: a mark made while the request was in flight has a
           newer timestamp and must survive to be sent on the next flush. */
        for (k in snapshot) if (out[k] && out[k].t === snapshot[k]) delete out[k];
        persist();
        if (seeding) set(SEED, "1");
      }

      var data = await req("/api/pull?since=" + rev());
      /* A server rev BELOW our cursor means the database was recreated. Re-seed
         rather than sit forever with a cursor no row will ever exceed. */
      if (data.rev < rev()) { set(SEED, ""); set(CUR, "0"); markEverything(); }
      applyRows(data.grades || [], data.days || []);
      set(CUR, String(data.rev));
      set(AT, String(Date.now()));
      if (!ls(SEED, "")) set(SEED, "1");
      backoff = 2000;
      note();
      if (pending()) schedule(400);            /* marks arrived mid-flight */
    } catch (e) {
      if (String(e.message) !== "auth") {
        note();
        backoff = Math.min(backoff * 2, 5 * 60e3);
        schedule(backoff);
      }
    } finally { inflight = false; }
  }

  function markEverything() {
    var t = Date.now(), id, d;
    for (id in host.state) if (host.state[id]) out["g|" + id] = { v: host.state[id] | 0, t: t };
    for (d in host.days) for (id in host.days[d]) if (host.days[d][id]) out["d|" + d + "|" + id] = { v: 1, t: t };
    persist();
  }

  function schedule(ms) { clearTimeout(timer); timer = setTimeout(sync, ms); }

  /* ---------- status ---------- */
  function note(force) {
    var el = document.getElementById("syncNote");
    if (!el) return;
    var n = pending(), at = +ls(AT, 0) || 0;
    if (force) { el.textContent = force; return; }
    if (stopped) { el.textContent = "Signed out — reload to sign in."; return; }
    if (navigator.onLine === false) { el.textContent = n ? "Offline — " + n + " queued." : "Offline."; return; }
    if (n) { el.textContent = n + " change" + (n === 1 ? "" : "s") + " queued…"; return; }
    if (!at) { el.textContent = "Not synced yet."; return; }
    var mins = Math.floor((Date.now() - at) / 60000);
    el.textContent = "Synced " + (mins < 1 ? "just now" : mins === 1 ? "1 min ago" : mins + " min ago") + ".";
  }

  /* ---------- public ---------- */
  window.PrepSync = {
    start: function (h) {
      host = h;
      try { out = JSON.parse(ls(OUT, "{}") || "{}") || {}; } catch (e) { out = {}; }
      snap();

      /* First run on this device: push what is already here. Seed mode may only
         RAISE a grade and never writes a tombstone, so two devices that each hold
         real progress merge to the union instead of the second one erasing the first. */
      if (!ls(SEED, "")) markEverything();

      host.onSaved(function () { if (diffGrades()) { persist(); note(); schedule(1200); } });
      host.onSavedDays(function () { if (diffDays()) { persist(); note(); schedule(1200); } });

      addEventListener("online", function () { backoff = 2000; schedule(200); });
      addEventListener("offline", function () { note(); });
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) { PrepSync.beacon(); return; }
        if (Date.now() - (+ls(AT, 0) || 0) > 60000) schedule(300);
      });
      addEventListener("pagehide", function () { PrepSync.beacon(); });

      var btn = document.getElementById("syncNow");
      if (btn) btn.addEventListener("click", function () { backoff = 2000; schedule(0); });

      var so = document.getElementById("signout");
      if (so) so.addEventListener("click", async function () {
        if (pending() && !confirm(pending() + " change(s) have not synced yet. Sign out anyway?")) return;
        try { await fetch("/api/logout", { method: "POST", credentials: "same-origin" }); } catch (e) {}
        /* Drop the cached pages too. Without this the whole library stays readable
           offline on a device you just signed out of. */
        try {
          var keys = await caches.keys();
          await Promise.all(keys.map(function (k) { return caches.delete(k); }));
          var regs = await navigator.serviceWorker.getRegistrations();
          await Promise.all(regs.map(function (r) { return r.unregister(); }));
        } catch (e) {}
        stopped = true;
        location.replace("/login.html");
      });

      setInterval(function () { if (!document.hidden) schedule(0); }, 5 * 60e3);
      setInterval(function () { note(); }, 30e3);

      note();
      schedule(600);                            /* after first paint, never before */
    },

    /* Last-gasp send on hide/unload. It deliberately does NOT clear the outbox:
       sendBeacon cannot read a response, so it cannot know the write landed. The
       next real flush re-sends, which is safe because an op that already won is a
       no-op that does not bump rev. */
    beacon: function () {
      if (stopped || !pending() || !navigator.sendBeacon) return;
      try {
        navigator.sendBeacon("/api/push",
          new Blob([JSON.stringify(payload())], { type: "application/json" }));
      } catch (e) {}
    },

    _test: {
      payload: payload, applyRows: applyRows, sync: sync, diffGrades: diffGrades,
      diffDays: diffDays, markEverything: markEverything, snap: snap,
      out: function () { return out; }, host: function () { return host; },
    },
  };
})();
