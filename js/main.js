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

  /* ---------- Hero slider ----------
     Active dot ek progress bar ki tarah bharta hai (CSS animation).
     Jab woh bhar jaata hai (animationend), agli photo aa jaati hai.
     Mouse upar ho toh CSS animation ruk jaati hai, toh slider bhi ruk jaata hai. */
  var hero = $(".hero");
  if (hero) {
    var slides = $$(".hero__slide", hero);
    var dots = $$(".hero__dots [data-slide]", hero);
    var current = 0;
    function show(i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("is-active", k === current); });
      dots.forEach(function (d, k) {
        d.classList.remove("is-active");
        if (k === current) { void d.offsetWidth; d.classList.add("is-active"); }
        d.setAttribute("aria-current", k === current ? "true" : "false");
      });
    }
    dots.forEach(function (d) {
      d.addEventListener("click", function () { show(+d.dataset.slide); });
      d.addEventListener("animationend", function (e) {
        if (d.classList.contains("is-active") && e.animationName === "dotfill") show(current + 1);
      });
    });
    var prev = $(".hero__arrow--prev", hero), next = $(".hero__arrow--next", hero);
    if (prev) prev.addEventListener("click", function () { show(current - 1); });
    if (next) next.addEventListener("click", function () { show(current + 1); });
    show(0);
  }

  /* ---------- Counters ---------- */
  function countUp(el) {
    var end = parseInt(el.dataset.count, 10), suffix = el.dataset.suffix || "";
    if (reduceMotion) { el.textContent = end.toLocaleString("en-IN") + suffix; return; }
    var t0 = null, dur = 1800;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))).toLocaleString("en-IN") + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    el.textContent = "0" + suffix;
    requestAnimationFrame(step);
  }

  /* ---------- Scroll animations (Eduboc jaisa) ----------
     Har section ki cheezein side ya neeche se dheere slide hokar aati hain.
     Ek group ke cards ek ke baad ek aate hain (stagger). */
  var AUTO = [
    [".section-head > *", "up", 0.09],
    [".about__media", "left", 0], [".about > div:not(.about__media)", "right", 0],
    [".stat", "up", 0.1], [".brand-card", "up", 0.08], [".service", "up", 0.08],
    [".how__media", "left", 0], [".steps li", "right", 0.1], [".machine", "up", 0.1],
    [".split", "zoom", 0], [".member", "up", 0.12], [".faq__item", "up", 0.07],
    [".quote__inner > div", "left", 0], [".quote__inner > form", "right", 0],
    [".cta", "zoom", 0], [".contact-card", "left", 0.08], [".map", "right", 0],
    [".product", "up", 0.07], [".feature-panel", "zoom", 0], [".delivery, .band", "up", 0],
    [".shadecard", "up", 0.1], [".pgroup__head", "left", 0], [".more-strip", "up", 0],
    [".footer__grid > div", "up", 0.08], [".footer__mark", "up", 0], [".tabpanel__head", "up", 0],
    [".bhero__inner > *, .pbanner__inner > *", "up", 0.15]
  ];
  var rvItems = [];
  // reveal khatam hone ke baad dheemi transition hata do, taaki hover turant chale
  function settle(el) {
    var d = parseFloat(el.style.getPropertyValue("--rvd")) || 0;
    setTimeout(function () { el.classList.add("rv-done"); }, 1350 + d * 1000);
  }
  function mark(el, dir, delay) {
    if (el.classList.contains("rv")) return;
    el.classList.remove("reveal");
    el.classList.add("rv", "rv--" + dir);
    if (delay) el.style.setProperty("--rvd", delay.toFixed(2) + "s");
    rvItems.push(el);
  }
  if (!reduceMotion && "IntersectionObserver" in window) {
    // hero: page khulte hi ek ek karke
    $$(".hero [data-rv]").forEach(function (el, k) { mark(el, el.dataset.rv, 0.15 + k * 0.12); });
    AUTO.forEach(function (rule) {
      var groups = new Map();
      $$(rule[0]).forEach(function (el) {
        if (el.closest(".hero")) return;
        var g = groups.get(el.parentElement) || 0;
        groups.set(el.parentElement, g + 1);
        mark(el, rule[1], Math.min(g, 6) * rule[2]);
      });
    });
    $$(".reveal").forEach(function (el) { mark(el, "up", 0); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        io.unobserve(en.target);
        settle(en.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    rvItems.forEach(function (el) { io.observe(el); });
    // backup: agar kisi wajah se animation na chale, toh screen pe dikh rahi cheez dikha do
    window.addEventListener("load", function () {
      setTimeout(function () {
        rvItems.forEach(function (el) {
          var r = el.getBoundingClientRect();
          if (r.top < window.innerHeight && r.bottom > 0) { el.classList.add("is-in"); settle(el); }
        });
      }, 2500);
    });
    // hero turant
    setTimeout(function () { $$(".hero .rv").forEach(function (el) { el.classList.add("is-in"); settle(el); }); }, 90);
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("is-in"); });
  }
  if ("IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        countUp(en.target);
        cio.unobserve(en.target);
      });
    }, { threshold: 0.4 });
    $$("[data-count]").forEach(function (el) { cio.observe(el); });
  }

  /* ---------- Service kitaab: click pe khulti hai ---------- */
  var books = $$(".book");
  function setBook(book, open) {
    var front = $(".book__front", book);
    book.classList.toggle("is-open", open);
    front.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) setTimeout(function () {
      var c = $(".book__close", book);
      if (c && book.classList.contains("is-open")) c.focus({ preventScroll: true });
    }, 700);
  }
  function closeBooks(except) {
    books.forEach(function (b) { if (b !== except && b.classList.contains("is-open")) setBook(b, false); });
  }
  books.forEach(function (book) {
    var front = $(".book__front", book), close = $(".book__close", book);
    function open() { closeBooks(book); setBook(book, true); }
    front.addEventListener("click", open);
    front.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
    close.addEventListener("click", function () { setBook(book, false); front.focus({ preventScroll: true }); });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".book")) closeBooks(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeBooks(); });

  /* ---------- FAQ: smooth khulna / band hona ---------- */
  $$(".faq__item").forEach(function (item) {
    var summary = $("summary", item), body = $(".faq__a", item);
    summary.addEventListener("click", function (e) {
      if (reduceMotion || !body.animate) return;
      e.preventDefault();
      if (item.open) {
        var h = body.offsetHeight;
        body.animate([{ height: h + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 450, easing: "cubic-bezier(.22,1,.36,1)" })
          .onfinish = function () { item.open = false; };
      } else {
        item.open = true;
        var h2 = body.offsetHeight;
        body.animate([{ height: "0px", opacity: 0 }, { height: h2 + "px", opacity: 1 }], { duration: 550, easing: "cubic-bezier(.22,1,.36,1)" });
      }
    });
  });

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
