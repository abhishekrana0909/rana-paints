/* Rana Paint & Cement Store: site behaviour */
(function () {
  "use strict";

  var WHATSAPP = "919417123935";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function waLink(text) {
    return "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(text);
  }
  window.RanaWA = waLink;

  /* ---------- Mobile navigation ---------- */
  var toggle = $(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  $$(".nav__item--drop > .nav__link").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var item = btn.parentElement;
      var open = item.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  document.addEventListener("click", function (e) {
    $$(".nav__item--drop.is-open").forEach(function (item) {
      if (!item.contains(e.target) && window.innerWidth > 1024) {
        item.classList.remove("is-open");
        $(".nav__link", item).setAttribute("aria-expanded", "false");
      }
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
    $$(".nav__item--drop.is-open").forEach(function (item) { item.classList.remove("is-open"); });
    closeViewer();
  });
  $$(".nav a").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("nav-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- Header shadow + back to top ---------- */
  var header = $(".header");
  var toTop = $(".to-top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 10);
    if (toTop) toTop.classList.toggle("is-visible", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); });

  /* ---------- Hero slider ---------- */
  var hero = $(".hero");
  if (hero) {
    var slides = $$(".hero__slide", hero);
    var dots = $$(".hero__dots [data-slide]", hero);
    var current = 0, timer = null;
    function show(i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("is-active", k === current); });
      dots.forEach(function (d, k) {
        d.classList.toggle("is-active", k === current);
        d.setAttribute("aria-current", k === current ? "true" : "false");
      });
    }
    function start() { if (!reduceMotion && slides.length > 1) { stop(); timer = setInterval(function () { show(current + 1); }, 6000); } }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    dots.forEach(function (d) { d.addEventListener("click", function () { show(+d.dataset.slide); start(); }); });
    var prev = $(".hero__arrow--prev", hero), next = $(".hero__arrow--next", hero);
    if (prev) prev.addEventListener("click", function () { show(current - 1); start(); });
    if (next) next.addEventListener("click", function () { show(current + 1); start(); });
    hero.addEventListener("mouseenter", stop);
    hero.addEventListener("mouseleave", start);
    show(0); start();
  }

  /* ---------- Reveal on scroll + counters ---------- */
  function countUp(el) {
    var end = parseInt(el.dataset.count, 10), suffix = el.dataset.suffix || "";
    if (reduceMotion) { el.textContent = end.toLocaleString("en-IN") + suffix; return; }
    var t0 = null, dur = 1400;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))).toLocaleString("en-IN") + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        if (en.target.dataset.count) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: 0.12 });
    $$(".reveal, [data-count]").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("is-in"); });
    $$("[data-count]").forEach(countUp);
  }

  /* ---------- Filter chips ---------- */
  $$("[data-filters]").forEach(function (bar) {
    var grid = document.getElementById(bar.dataset.filters);
    if (!grid) return;
    var items = $$("[data-tags]", grid);
    $$("button", bar).forEach(function (btn) {
      btn.addEventListener("click", function () {
        $$("button", bar).forEach(function (b) { b.classList.remove("is-active"); b.setAttribute("aria-pressed", "false"); });
        btn.classList.add("is-active");
        btn.setAttribute("aria-pressed", "true");
        var f = btn.dataset.filter;
        items.forEach(function (it) {
          var show = f === "all" || (" " + it.dataset.tags + " ").indexOf(" " + f + " ") > -1;
          it.classList.toggle("is-hidden", !show);
        });
      });
    });
  });

  /* ---------- Tabs (Birla / shades style) ---------- */
  $$("[data-tabs]").forEach(function (bar) {
    var btns = $$("[role=tab]", bar);
    function activate(btn, focus, byUser) {
      btns.forEach(function (b) {
        var on = b === btn;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-selected", on ? "true" : "false");
        b.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(b.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
      if (focus) btn.focus();
      if (byUser && bar.dataset.hash !== undefined && btn.dataset.hash) history.replaceState(null, "", "#" + btn.dataset.hash);
    }
    btns.forEach(function (b, i) {
      b.addEventListener("click", function () { activate(b, false, true); });
      b.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight") { e.preventDefault(); activate(btns[(i + 1) % btns.length], true, true); }
        if (e.key === "ArrowLeft") { e.preventDefault(); activate(btns[(i - 1 + btns.length) % btns.length], true, true); }
      });
    });
    var fromHash = location.hash && btns.filter(function (b) { return b.dataset.hash === location.hash.slice(1); })[0];
    activate(fromHash || btns.filter(function (b) { return b.classList.contains("is-active"); })[0] || btns[0]);
    if (fromHash) setTimeout(function () { bar.scrollIntoView({ block: "start" }); }, 50);
  });

  /* ---------- Sub-nav scrollspy (brand pages) ---------- */
  var subnav = $(".subnav");
  if (subnav && "IntersectionObserver" in window) {
    var links = $$("a[href^='#']", subnav);
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove("is-active"); });
        var a = map[en.target.id];
        if (a) {
          a.classList.add("is-active");
          var list = a.parentElement.parentElement;
          list.scrollTo({ left: a.offsetLeft - 20, behavior: reduceMotion ? "auto" : "smooth" });
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* ---------- WhatsApp enquiry form ---------- */
  $$("form[data-wa-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = ["Namaste Rana Paints! I want to book a free site visit / estimate.", ""];
      if (d.get("name")) lines.push("Name: " + d.get("name"));
      if (d.get("phone")) lines.push("Phone: " + d.get("phone"));
      if (d.get("place")) lines.push("Village / City: " + d.get("place"));
      if (d.get("work")) lines.push("Work: " + d.get("work"));
      if (d.get("message")) lines.push("Details: " + d.get("message"));
      window.open(waLink(lines.join("\n")), "_blank", "noopener");
    });
  });

  /* ---------- Shade card viewer ---------- */
  var viewer = null;
  function buildViewer() {
    viewer = document.createElement("div");
    viewer.className = "viewer";
    viewer.setAttribute("role", "dialog");
    viewer.setAttribute("aria-modal", "true");
    viewer.innerHTML =
      '<div class="viewer__bar"><h3 id="viewer-title"></h3>' +
      '<a class="btn btn--sm btn--white" data-viewer-pdf target="_blank" rel="noopener" download>Download PDF</a>' +
      '<button class="viewer__close" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>' +
      '<div class="viewer__pages"></div>';
    viewer.setAttribute("aria-labelledby", "viewer-title");
    document.body.appendChild(viewer);
    $(".viewer__close", viewer).addEventListener("click", closeViewer);
    viewer.addEventListener("click", function (e) { if (e.target === viewer) closeViewer(); });
  }
  var lastFocus = null;
  function openViewer(btn) {
    if (!viewer) buildViewer();
    lastFocus = btn;
    $("#viewer-title", viewer).textContent = btn.dataset.title || "Shade card";
    var pdf = $("[data-viewer-pdf]", viewer);
    pdf.href = btn.dataset.pdf;
    var pages = $(".viewer__pages", viewer);
    pages.className = "viewer__pages" + (btn.dataset.strip ? " viewer__pages--strip" : "");
    pages.innerHTML = "";
    JSON.parse(btn.dataset.pages).forEach(function (src, i) {
      var img = document.createElement("img");
      img.src = src;
      img.alt = (btn.dataset.title || "Shade card") + ", page " + (i + 1);
      img.loading = i < 2 ? "eager" : "lazy";
      pages.appendChild(img);
    });
    pages.scrollTop = 0;
    viewer.classList.add("is-open");
    document.body.style.overflow = "hidden";
    $(".viewer__close", viewer).focus();
  }
  function closeViewer() {
    if (!viewer || !viewer.classList.contains("is-open")) return;
    viewer.classList.remove("is-open");
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  $$("[data-viewer]").forEach(function (btn) { btn.addEventListener("click", function () { openViewer(btn); }); });
  var auto = location.hash.match(/^#card-(.+)$/);
  if (auto) { var b = document.querySelector('[data-viewer="' + auto[1] + '"]'); if (b) openViewer(b); }

  /* ---------- Footer year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
