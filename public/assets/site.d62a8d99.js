/* Shared behaviour for every page: drawer, service worker, scroll affordances.
   Deliberately dependency-free and small — it loads on all 22 pages. */
(function () {
  "use strict";

  /* ---------- drawer, reusable ---------- */
  function lock(on) {
    if (on) {
      lock.y = window.scrollY;
      /* overflow:hidden alone does not reliably lock iOS Safari */
      document.body.style.cssText =
        "position:fixed;top:" + -lock.y + "px;left:0;right:0;width:100%;overflow:hidden";
    } else {
      document.body.style.cssText = "";
      window.scrollTo(0, lock.y || 0);
    }
  }

  window.Drawer = function (btn, aside, scrim) {
    if (!btn || !aside) return null;
    var wide = window.matchMedia("(min-width:1001px)");
    function set(open) {
      aside.classList.toggle("open", open);
      if (scrim) scrim.classList.toggle("on", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      if (!wide.matches) lock(open);
    }
    btn.addEventListener("click", function () {
      set(!aside.classList.contains("open"));
    });
    if (scrim) scrim.addEventListener("click", function () { set(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") set(false);
    });
    aside.addEventListener("click", function (e) {
      if (e.target.closest("a") && !wide.matches) set(false);
    });
    return set;
  };

  var side = document.getElementById("s-side");
  if (side) Drawer(document.getElementById("s-menu"), side, document.getElementById("s-scrim"));

  /* ---------- standalone back button ----------
     An installed iOS web app has no browser chrome, so without this you get
     stuck three documents deep with no way back. */
  var back = document.getElementById("s-back");
  if (back) {
    var standalone =
      window.matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
    if (standalone && history.length > 1) {
      back.hidden = false;
      back.addEventListener("click", function () { history.back(); });
    }
  }

  /* ---------- back to top ---------- */
  var top = document.getElementById("s-top");
  if (top) {
    top.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    var t = false;
    addEventListener("scroll", function () {
      if (t) return;
      t = true;
      requestAnimationFrame(function () {
        top.classList.toggle("on", window.scrollY > 600);
        t = false;
      });
    }, { passive: true });
  }

  /* ---------- table overflow fade, only where it actually scrolls ---------- */
  var tws = document.querySelectorAll(".tw, .diagram");
  if (tws.length) {
    var mark = function () {
      tws.forEach(function (el) {
        el.classList.toggle("of", el.scrollWidth > el.clientWidth + 2);
      });
    };
    mark();
    addEventListener("resize", mark, { passive: true });
    if (window.ResizeObserver) {
      var ro = new ResizeObserver(mark);
      tws.forEach(function (el) { ro.observe(el); });
    }
  }

  /* ---------- diagram fit toggle ---------- */
  document.querySelectorAll("[data-fit]").forEach(function (btn) {
    var box = document.getElementById(btn.dataset.fit);
    if (!box) return;
    btn.addEventListener("click", function () {
      var fit = box.classList.toggle("fit");
      /* the label names the action, so no active-state highlight to contradict it */
      btn.textContent = fit ? "⤢ actual size" : "⤡ fit to screen";
    });
  });

  /* ---------- service worker ----------
     Cache-first against a versioned cache. No skipWaiting() on install: swapping
     CSS/JS under an already-rendered page is the classic half-styled-after-deploy
     bug. The user taps the pill instead. */
  var secure = location.protocol === "https:" || location.hostname === "localhost";
  var embedded = window.top !== window.self;   /* an embedded copy must not claim the origin */
  /* Never install from the login page. Logged out, cache.addAll() follows the gate's
     redirect and caches the LOGIN PAGE under all 24 URLs — the app would then serve a
     login screen from cache for ever, even once authenticated. */
  var onLogin = location.pathname === "/login.html";
  if ("serviceWorker" in navigator && secure && !embedded && !onLogin) {
    navigator.serviceWorker.register("/sw.js").then(function (reg) {
      function pill(worker) {
        if (document.querySelector(".upd-pill")) return;
        var b = document.createElement("button");
        b.className = "upd-pill";
        b.textContent = "New version — tap to update";
        b.addEventListener("click", function () {
          b.textContent = "Updating…";
          worker.postMessage("SKIP_WAITING");
        });
        document.body.appendChild(b);
      }
      if (reg.waiting && navigator.serviceWorker.controller) pill(reg.waiting);
      reg.addEventListener("updatefound", function () {
        var w = reg.installing;
        if (!w) return;
        w.addEventListener("statechange", function () {
          if (w.state === "installed" && navigator.serviceWorker.controller) pill(w);
        });
      });
      reg.update();
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) return;
        var last = +localStorage.getItem("mt.updChk") || 0;
        if (Date.now() - last > 36e5) {
          localStorage.setItem("mt.updChk", String(Date.now()));
          reg.update();
        }
      });
    }).catch(function () { /* SW is an enhancement; never block the page */ });

    var reloaded = false;
    navigator.serviceWorker.addEventListener("controllerchange", function () {
      if (reloaded) return;      /* guard the reload loop */
      reloaded = true;
      location.reload();
    });
  }
})();
