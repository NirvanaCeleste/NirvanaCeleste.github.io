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
    /* 只取 h2 的直接文本节点：主题的锚点 "#" 是嵌在子元素里的，
       线上 --minify 后没有空白分隔，读 textContent 会得到 "A#" 导致匹配失败 */
    var own = "";
    h.childNodes.forEach(function (n) {
      if (n.nodeType === 3) own += n.textContent;
    });
    own = own.trim();
    var m = own.match(/^([A-Za-z][0-9]?)[\.\s\u3000]/) || own.match(/^([A-Z][0-9]?)$/);
    if (!m) return;
    var idNode = h.id ? h : h.querySelector("[id]");
    if (!idNode || !idNode.id) return;
    items.push({ label: m[1].toUpperCase(), id: idNode.id });
  });
  if (items.length < 1) return;

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

  /* 顶部横条模式的吸附偏移：贴在站点顶部导航栏（.main-menu 所在 header）下方 */
  var menu = document.querySelector(".main-menu");
  var hdr = document.getElementById("site-header")
    || document.querySelector("body > header")
    || (menu ? menu.closest("header") : null);
  var top = (hdr ? hdr.offsetHeight : 72) + 8;
  if (top > 140) top = 88; /* 兜底：别量到奇怪的大容器 */
  document.documentElement.style.setProperty("--probnav-top", top + "px");

  /* 宽屏且左侧有真实空隙时：rail 模式，贴正文左缘、顶部与正文开头对齐 */
  function placeRail() {
    var content = art.querySelector("header") || art;
    var rect = content.getBoundingClientRect();
    var btn = bar.querySelector(".probnav-btn");
    var railW = (btn ? btn.offsetWidth : 44) + 20; /* 竖排宽度≈按钮宽+内边距 */
    var free = rect.left - 24;
    if (window.innerWidth >= 1100 && free >= railW) {
      bar.classList.add("probnav--rail");
      bar.style.left = Math.max(12, rect.left - bar.offsetWidth - 16) + "px";
      var vh = window.innerHeight;
      var docTop = rect.top + (window.pageYOffset || 0);
      var t = Math.max(90, Math.min(docTop, vh - bar.offsetHeight - 40));
      bar.style.top = t + "px";
    } else {
      bar.classList.remove("probnav--rail");
      bar.style.left = "";
      bar.style.top = "";
    }
  }
  placeRail();
  var rt;
  window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(placeRail, 120); });

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
