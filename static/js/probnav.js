/* 跳题按钮：ACM 复盘帖顶部生成 A/B/C/... 锚点导航，按做题状态着色。
   数据来自 head.html 注入的 #__acm-upsolve（帖子 front matter 的 upsolve 字段）。 */
(function () {
  "use strict";
  var art = document.querySelector("article");
  if (!art) return;

  var upsolve = [];
  try {
    var ds = document.getElementById("__acm-upsolve");
    if (ds) upsolve = JSON.parse(ds.textContent) || [];
  } catch (e) { /* 无数据按中性处理 */ }
  var wrong = {}, skip = {};
  upsolve.forEach(function (x) {
    if (x.status === "wrong") wrong[x.problem] = 1;
    else if (x.status === "skip") skip[x.problem] = 1;
  });

  var items = [];
  art.querySelectorAll("h2").forEach(function (h) {
    var text = h.textContent.trim();
    var m = text.match(/^([A-Za-z][0-9]?)[\.\s\u3000]/) || text.match(/^([A-Z][0-9]?)$/);
    if (!m) return;
    var idNode = h.id ? h : h.querySelector("[id]");
    if (!idNode || !idNode.id) return;
    items.push({ label: m[1].toUpperCase(), id: idNode.id });
  });
  if (items.length < 2) return;

  var bar = document.createElement("nav");
  bar.className = "probnav";
  bar.setAttribute("aria-label", "题目导航");
  var title = document.createElement("span");
  title.className = "probnav-title";
  title.textContent = "跳题";
  bar.appendChild(title);

  var btns = {};
  items.forEach(function (it) {
    var a = document.createElement("a");
    var st = wrong[it.label] ? "wrong" : skip[it.label] ? "skip" : (upsolve.length ? "ok" : "none");
    a.className = "probnav-btn " + st;
    a.textContent = it.label;
    a.href = "#" + it.id;
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var el = document.getElementById(it.id);
      if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      if (history.replaceState) history.replaceState(null, "", "#" + it.id);
    });
    btns[it.id] = a;
    bar.appendChild(a);
  });

  var header = art.querySelector("header");
  if (header && header.parentNode === art) art.insertBefore(bar, header.nextSibling);
  else art.insertBefore(bar, art.firstChild);

  /* 顶部横条模式的吸附偏移：站点导航栏吸顶时贴它下方，否则贴近视口顶部 */
  var hdr = document.getElementById("site-header") || document.querySelector("body > header");
  var hp = hdr ? getComputedStyle(hdr).position : "";
  var top = (hdr && (hp === "sticky" || hp === "fixed")) ? hdr.offsetHeight + 8 : 10;
  document.documentElement.style.setProperty("--probnav-top", top + "px");

  /* 滚动时高亮当前题目 */
  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      var b = btns[en.target.id] || btns[(en.target.querySelector("[id]") || {}).id];
      if (!b) return;
      if (en.isIntersecting) {
        Object.keys(btns).forEach(function (k) { btns[k].classList.remove("active"); });
        b.classList.add("active");
      }
    });
  }, { rootMargin: "-20% 0px -70% 0px" });
  items.forEach(function (it) {
    var el = document.getElementById(it.id);
    if (el) spy.observe(el.parentElement || el);
  });
})();
