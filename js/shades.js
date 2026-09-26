/* Shade browser for Berger and Birla Opus colour catalogues.
   Data lives in js/data/*.js as window.SHADES[brand] = [[name, code, hex, family], ...] */
(function () {
  "use strict";

  var PAGE = 120;
  var BRAND_NAMES = { berger: "Berger Paints", birla: "Birla Opus" };

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function hsl(hex) {
    var r = parseInt(hex.substr(1, 2), 16) / 255, g = parseInt(hex.substr(3, 2), 16) / 255, b = parseInt(hex.substr(5, 2), 16) / 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b), h = 0, s = 0, l = (max + min) / 2;
    if (max !== min) {
      var d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      h = max === r ? (g - b) / d + (g < b ? 6 : 0) : max === g ? (b - r) / d + 2 : (r - g) / d + 4;
      h *= 60;
    }
    return [h, s, l];
  }
  function isDark(hex) { return hsl(hex)[2] < 0.55; }

  var SOFA =
    '<svg viewBox="0 0 400 140" aria-hidden="true"><g fill="rgba(0,0,0,.18)"><ellipse cx="200" cy="134" rx="170" ry="6"/></g>' +
    '<g fill="#f4f1ec"><rect x="70" y="40" width="260" height="62" rx="18"/><rect x="40" y="62" width="60" height="62" rx="16"/><rect x="300" y="62" width="60" height="62" rx="16"/><rect x="84" y="88" width="232" height="36" rx="10"/></g>' +
    '<g fill="#d8d2c8"><rect x="96" y="54" width="70" height="34" rx="10"/><rect x="234" y="54" width="70" height="34" rx="10"/></g>' +
    '<g fill="#8b6f4e"><rect x="60" y="122" width="8" height="12" rx="2"/><rect x="332" y="122" width="8" height="12" rx="2"/></g></svg>';

  function init(app) {
    var brand = app.dataset.brand;
    var raw = (window.SHADES || {})[brand] || [];
    var data = raw.map(function (r) { return { name: r[0], code: r[1], hex: r[2], family: r[3], hsl: hsl(r[2]) }; });

    var families = [];
    data.forEach(function (d) { if (families.indexOf(d.family) < 0) families.push(d.family); });

    // Inside a family: light to dark. For "All colours": take the most vivid shade of each
    // family in turn, so the first screen shows a colourful mix instead of only whites.
    var byFamily = {};
    families.forEach(function (f) { byFamily[f] = []; });
    data.forEach(function (d) { byFamily[d.family].push(d); });
    families.forEach(function (f) { byFamily[f].sort(function (a, b) { return b.hsl[2] - a.hsl[2]; }); });
    var mixed = [], buckets = families.map(function (f) {
      return byFamily[f].slice().sort(function (a, b) { return b.hsl[1] - a.hsl[1]; });
    });
    for (var r = 0, left = data.length; left > 0; r++) {
      buckets.forEach(function (b) { if (b[r]) { mixed.push(b[r]); left--; } });
    }

    var state = { q: "", fam: "all", shown: PAGE, list: mixed, selected: null };

    var tools = el("div", "swatch-tools");
    var search = el("label", "search",
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>' +
      '<span class="skip-link">Search shades</span><input type="search" placeholder="Search by shade name or code" autocomplete="off">');
    var count = el("span", "swatch-count");
    tools.appendChild(search);
    tools.appendChild(count);

    var fbar = el("div", "filters");
    fbar.setAttribute("role", "group");
    fbar.setAttribute("aria-label", "Colour family");
    ["all"].concat(families).forEach(function (f) {
      var b = el("button", f === "all" ? "is-active" : "", f === "all" ? "All colours" : esc(f));
      b.type = "button";
      b.dataset.fam = f;
      b.setAttribute("aria-pressed", f === "all" ? "true" : "false");
      fbar.appendChild(b);
    });

    var layout = el("div", "swatch-layout");
    var left = el("div");
    var grid = el("div", "swatches");
    grid.setAttribute("aria-live", "polite");
    var more = el("div", "swatch-more", '<button type="button" class="btn btn--outline">Show more shades</button>');
    left.appendChild(grid);
    left.appendChild(more);

    var detail = el("aside", "shade-detail");
    detail.setAttribute("aria-live", "polite");
    layout.appendChild(left);
    layout.appendChild(detail);

    app.appendChild(tools);
    app.appendChild(fbar);
    app.appendChild(layout);

    function filter() {
      var q = state.q.trim().toLowerCase();
      var source = state.fam === "all" ? mixed : byFamily[state.fam];
      state.list = source.filter(function (d) {
        if (!q) return true;
        return d.name.toLowerCase().indexOf(q) > -1 || d.code.toLowerCase().replace(/\s/g, "").indexOf(q.replace(/\s/g, "")) > -1;
      });
      state.shown = PAGE;
      render();
    }

    function render() {
      grid.innerHTML = "";
      var frag = document.createDocumentFragment();
      state.list.slice(0, state.shown).forEach(function (d) {
        var b = el("button", "swatch" + (state.selected === d ? " is-selected" : ""),
          '<span class="swatch__chip" style="display:block;background:' + d.hex + '"></span>' +
          '<span class="swatch__info"><span class="swatch__name">' + esc(d.name) + '</span><span class="swatch__code">' + esc(d.code) + "</span></span>");
        b.type = "button";
        b.title = d.name + " (" + d.code + ")";
        b.addEventListener("click", function () { select(d, b); });
        frag.appendChild(b);
      });
      if (!state.list.length) frag.appendChild(el("p", "swatch-empty", "No shade found. Try another name or code."));
      grid.appendChild(frag);
      count.textContent = state.list.length.toLocaleString("en-IN") + " shades";
      more.style.display = state.list.length > state.shown ? "" : "none";
    }

    function select(d, btn) {
      state.selected = d;
      Array.prototype.forEach.call(grid.querySelectorAll(".swatch.is-selected"), function (s) { s.classList.remove("is-selected"); });
      if (btn) btn.classList.add("is-selected");
      var msg = "Namaste Rana Paints! I want " + BRAND_NAMES[brand] + " shade \"" + d.name + "\" (" + d.code + "). Please share price and availability.";
      detail.innerHTML =
        '<div class="shade-detail__wall" style="background:' + d.hex + '">' + SOFA + "</div>" +
        '<div class="shade-detail__body"><h3>' + esc(d.name) + "</h3>" +
        '<div class="shade-detail__meta"><span>Code: ' + esc(d.code) + "</span><span>" + esc(d.family) + "</span><span>" + d.hex + "</span></div>" +
        '<a class="btn btn--wa" target="_blank" rel="noopener" href="' + window.RanaWA(msg) + '">Ask for this shade</a>' +
        "<small>We mix this shade on our computerised colour machine. Screen colours can look slightly different from the real paint, so please check the shade card at the shop.</small></div>";
    }

    search.querySelector("input").addEventListener("input", function (e) { state.q = e.target.value; filter(); });
    Array.prototype.forEach.call(fbar.querySelectorAll("button"), function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call(fbar.querySelectorAll("button"), function (x) { x.classList.remove("is-active"); x.setAttribute("aria-pressed", "false"); });
        b.classList.add("is-active");
        b.setAttribute("aria-pressed", "true");
        state.fam = b.dataset.fam;
        filter();
      });
    });
    more.querySelector("button").addEventListener("click", function () { state.shown += PAGE; render(); });

    render();
    if (mixed.length) select(mixed[0], grid.querySelector(".swatch"));
  }

  Array.prototype.forEach.call(document.querySelectorAll(".swatch-app"), init);
})();
