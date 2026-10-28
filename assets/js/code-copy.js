/* 代码块右上角「复制」按钮：走程序化剪贴板，不受全站 user-select:none 影响 */
(function () {
  "use strict";
  var READY = "复制", DONE = "已复制 ✓", FAIL = "未复制";

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.cssText = "position:fixed;left:-9999px;top:0;opacity:0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  function flash(btn, text, cls) {
    btn.textContent = text;
    if (cls) btn.classList.add(cls);
    setTimeout(function () {
      btn.textContent = READY;
      btn.classList.remove(cls);
    }, 1600);
  }

  function wire(block) {
    var pre = block.querySelector("pre");
    if (!pre || block.querySelector(".code-copy-btn")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "code-copy-btn";
    btn.textContent = READY;
    btn.setAttribute("aria-label", "复制代码");
    btn.addEventListener("click", function () {
      var text = pre.innerText.replace(/\n$/, "");
      var done = function () { flash(btn, DONE, "ok"); };
      var fail = function () { flash(btn, FAIL, "fail"); };
      var settled = false;
      var viaFallback = function () {
        if (settled) return;
        settled = true;
        if (fallbackCopy(text)) done(); else fail();
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        /* 个别 WebView 的权限承诺会永远挂起：1 秒不结算就走 execCommand 备援 */
        var timer = setTimeout(viaFallback, 1000);
        navigator.clipboard.writeText(text).then(function () {
          if (settled) return;
          settled = true;
          clearTimeout(timer);
          done();
        }, function () {
          if (settled) return;
          settled = true;
          clearTimeout(timer);
          viaFallback();
        });
      } else {
        viaFallback();
      }
    });
    block.appendChild(btn);
  }

  function init() {
    var blocks = document.querySelectorAll("div.highlight");
    for (var i = 0; i < blocks.length; i++) wire(blocks[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
