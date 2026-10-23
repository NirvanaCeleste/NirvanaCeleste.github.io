/* 首页终端（明面 + 伏笔层）：由 layouts/index.html 引用，走 Hugo minify+fingerprint 管线 */
  (function () {
    "use strict";
    var body = document.getElementById("ht-body");
    var input = document.getElementById("ht-input");
    var win = document.getElementById("ht-window");
    var promptEl = document.getElementById("ht-prompt");

    var hist = [], hi = -1;
    function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }
    function line(html, cls) {
      var el = document.createElement("div");
      el.className = "t-line " + (cls || "");
      el.innerHTML = html;
      body.appendChild(el);
      body.scrollTop = body.scrollHeight;
      return el;
    }
    var REDUCED = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function typeLine(text, cls, done) {
      var el = line("", cls);
      if (REDUCED) { el.textContent = text; if (done) done(); return; }   // 晕动症用户免打字机动画
      var i = 0;
      (function tick() {
        if (i <= text.length) {
          el.textContent = text.slice(0, i);
          i += 1 + Math.floor(Math.random() * 2);
          body.scrollTop = body.scrollHeight;
          setTimeout(tick, 14);
        } else { el.textContent = text; if (done) done(); }
      })();
    }

    /* 可进入的页面（命令 = 门）：《未竟之事》剧本里的三个场景 */
    var ROOMS = {
      album: { path: "/album/" },
      door: { path: "/door/" },
      letters: { path: "/letters/" },
      acm: { path: "/acm/" },
      omori: { path: "/omori/modding-guide/" },
      about: { path: "/about/" }
    };

    function go(name) {
      var r = ROOMS[name];
      if (!r) { line("cd: 没有那个房间： " + esc(name), "t-err"); return; }
      line("连接中<span class='t-dim'>……</span>");
      setTimeout(function () { window.location.href = r.path; }, 420);
    }

    var HELP = [
      ["help",   "显示本帮助"],
      ["ls",     "列出房间"],
      ["cd",     "进入房间（cd 空格 + 房间名）"],
      ["bg",     "换壁纸（bg ls / bg 1-8 / bg blur 0-24 / bg off）"],
      ["pwd",    "当前位置"],
      ["whoami", "我是谁"],
      ["clear",  "清屏"]
    ];

    var CMDS = {
      help: function () {
        HELP.forEach(function (h) {
          line("<span class='t-cmd'>" + h[0].padEnd(8, " ") + "</span><span class='t-dim'>" + esc(h[1]) + "</span>");
        });
      },
      bg: function (rest) { bgCmd(rest); },
      ls: function () {
        var out = [];
        Object.keys(ROOMS).forEach(function (k) { out.push("<span class='t-ok'>" + k + "/</span>"); });
        line(out.join("  ") + "  <span class='t-dim'>blog.md</span>");
      },
      cd: function (rest) {
        var name = (rest || "").trim().replace(/\/$/, "");
        if (!name || name === "~" || name === "/") { line("回到了 ~/home。"); return; }
        go(name);
      },
      pwd: function () { line("/home"); },
      whoami: function () { line("<b>NirvanaCeleste</b> · 房间在别处。"); },
      clear: function () { body.innerHTML = ""; },
      exit: function () { line("<span class='t-dim'>这里没有出口。只有门。</span>"); }
    };
    /* 房间名直接当命令也行：cd save / save 等价 */

    /* ===== 壁纸系统（借鉴 quiz-app 外观系统）===== */
    /* 应用与读取的唯一实现在 layouts/partials/extend-head.html（全站生效）；这里只负责写入 */
    function bgWrite(v) {
      try { v ? localStorage.setItem("blog.appearance.bg.v1", JSON.stringify(v)) : localStorage.removeItem("blog.appearance.bg.v1"); } catch (e) {}
    }
    function bgCmd(rest) {
      var arg = (rest || "").trim().toLowerCase();
      if (!arg) {
        var cur = window.__bgRead();
        line(cur
          ? "壁纸 <span class='t-ok'>" + cur.n + "</span> · blur " + cur.blur + "px。用法：bg ls / bg 1-8 / bg blur 0-24 / bg off"
          : "未选壁纸（用默认底图）。用法：bg ls / bg 1-8 / bg blur 0-24 / bg off");
        return;
      }
      if (arg === "ls") {
        var s = window.__bgRead(), out = [], mqPhone = window.matchMedia("(max-width: 900px)");
        for (var i = 1; i <= 8; i++) out.push(s && s.n === i ? "<span class='t-ok'>[" + i + "]</span>" : i);
        line("壁纸：" + out.join("  ") + "  <span class='t-dim'>（" + (mqPhone.matches ? "手机端图" : "桌面端图") + "）</span>");
        return;
      }
      if (arg === "off") { bgWrite(null); window.__bgApply(); line("已恢复默认底图。"); return; }
      var m = arg.match(/^blur\s+(\d{1,2})$/);
      if (m) {
        var b = Math.min(24, parseInt(m[1], 10));
        var cur2 = window.__bgRead() || { n: 1, blur: 0 };
        bgWrite({ n: cur2.n, blur: b }); window.__bgApply();
        line("blur → " + b + "px");
        return;
      }
      if (/^[1-8]$/.test(arg)) {
        var cur3 = window.__bgRead();
        bgWrite({ n: parseInt(arg, 10), blur: cur3 ? cur3.blur : 0 }); window.__bgApply();
        var mqPhone = window.matchMedia("(max-width: 900px)");
        line("壁纸 → <span class='t-ok'>" + arg + "</span> <span class='t-dim'>（" + (mqPhone.matches ? "mobile" : "desktop") + "-0" + arg + "）</span>");
        return;
      }
      line("用法：bg 1-8 · bg ls · bg blur 0-24 · bg off", "t-err");
    }

    function run(s) {
      if (!s) return;
      line("<span class='term-prompt'>❯</span> " + esc(s), "t-in");
      hist.push(s); hi = hist.length;
      var sp = s.indexOf(" ");
      var head = (sp < 0 ? s : s.slice(0, sp)).toLowerCase();
      var rest = sp < 0 ? "" : s.slice(sp + 1);
      if (CMDS[head]) CMDS[head](rest);
      else if (ROOMS[head]) go(head);
      else line("command not found: " + esc(head) + " <span class='t-dim'>（help）</span>", "t-err");
    }

    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { run(input.value.trim()); input.value = ""; }
      else if (e.key === "ArrowUp") { e.preventDefault(); if (hi > 0) { hi--; input.value = hist[hi] || ""; } }
      else if (e.key === "ArrowDown") { e.preventDefault(); if (hi < hist.length) { hi++; input.value = hist[hi] || ""; } }
      else if (e.key === "Tab") {
        e.preventDefault();
        var raw = input.value;
        var endsSpace = /\s$/.test(raw);
        var v = raw.trim().toLowerCase();
        if (!v) return;
        var sp = v.indexOf(" ");
        var names, prefixCmd = "";
        if (sp < 0 && !endsSpace) {
          /* 补命令名或房间名 */
          names = Object.keys(CMDS).concat(Object.keys(ROOMS)).filter(function (c) { return c.indexOf(v) === 0; });
        } else {
          /* 补 cd 的参数：房间名 */
          var head = sp < 0 ? v : v.slice(0, sp);
          var word = sp < 0 ? "" : v.slice(sp + 1).replace(/\/$/, "");
          if (head !== "cd") return;
          prefixCmd = head + " ";
          names = Object.keys(ROOMS).filter(function (c) { return c.indexOf(word) === 0; });
        }
        if (names.length === 1) input.value = prefixCmd + names[0] + (prefixCmd ? "" : " ");
        else if (names.length > 1) line("<span class='t-dim'>" + names.join("  ") + "</span>");
      }
    });
    win.addEventListener("click", function () {
      if (!window.getSelection().toString()) input.focus({ preventScroll: true });
    });

    var lines = [
      ["Nirvana Celeste Space", "t-sys"],
      ["You have been living here for as long as you can remember.", "t-dim"],
      ["输入 help 查看命令", "t-ok"]
    ];
    var k = 0;
    (function next() {
      if (k < lines.length) { typeLine(lines[k][0], lines[k][1], function(){ k++; setTimeout(next, 120); }); }
    })();
  })();
  (function () {
    "use strict";
    var D = {};
    try { D = JSON.parse(document.getElementById("__home_data").textContent) || {}; } catch (e) {}

    /* ============ 迷你终端（伏笔） ============ */
    var mt = document.getElementById("mini-term");
    var body = document.getElementById("term-body");
    var input = document.getElementById("term-input");
    function openTerm() {
      mt.classList.remove("hidden");
      mt.setAttribute("aria-hidden", "false");
      setTimeout(function () { input.focus(); }, 60);
      if (!body.childElementCount) {
        line('<span class="t-dim">you shouldn\'t be here.</span>');
        line('<span class="t-dim">（help 试试）</span>');
      }
    }
    function closeTerm() {
      mt.classList.add("hidden");
      mt.setAttribute("aria-hidden", "true");
    }
    document.getElementById("term-close").addEventListener("click", closeTerm);
    window.addEventListener("keydown", function (e) {
      if (e.key === "`" || e.key === "~") {
        e.preventDefault();
        mt.classList.contains("hidden") ? openTerm() : closeTerm();
      } else if (e.key === "Escape") { closeTerm(); }
    });
    function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

    function line(html, cls) {
      var el = document.createElement("div");
      el.className = "t-line " + (cls || "");
      el.innerHTML = html;
      body.appendChild(el);
      body.scrollTop = body.scrollHeight;
    }
    var TC = {
      help: function () {
        line("可用：<span class='t-cmd'>whoami ls cat xxd omori find clear exit</span>");
        line('<span class="t-dim">……以及没列出来的。</span>');
      },
      whoami: function () { line("<b>NirvanaCeleste</b> · 有几个秘密藏在站里"); },
      ls: function () { line('<span class="t-ok">acm/</span>  <span class="t-ok">omori/</span>  <span class="t-dim">search.md</span>'); },
      "ls -a": function () { TC.ls(); line('<span class="t-ws">.secret   setting_theme_core.css</span>'); },
      cat: function (r) {
        if ((r || "").trim() === ".secret") {
          line('<span class="t-dim">「位相偏移了。角落里有个说谎的文件——自称 css，却不是。」</span>');
          line('<span class="t-dim">（xxd setting_theme_core.css）</span>');
        } else if ((r || "").indexOf("setting_theme_core") >= 0) {
          line("cat: 二进制文件 <span class='t-dim'>（css 会是二进制的吗？）</span>", "t-err");
        } else line("cat: 没有那个文件", "t-err");
      },
      xxd: function (r) {
        if ((r || "").indexOf("setting_theme_core") >= 0) {
          line("<pre class='t-pre'>00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG....</pre>");
          line("魔数 <b>89 50 4E 47</b> —— 是一张 <b>PNG</b>。", "t-ok");
          line('→ <a href="/setting_theme_core.css">/setting_theme_core.css</a> 剩下的谜题，在现实里。');
        } else line("xxd: 没有那个文件", "t-err");
      },
      omori: function () {
        var on = document.documentElement.classList.toggle("ws-mode");
        line(on ? '<span class="t-ws">……这里什么都没有。</span>' : "欢迎回来。");
      },
      find: function (r) {
        var q = (r || "").trim().toLowerCase();
        if (!q) { line("用法：find 关键词"); return; }
        var hits = (D.posts || []).filter(function (p) { return (p.t + " " + (p.g || "")).toLowerCase().indexOf(q) >= 0; });
        if (!hits.length) { line("没找到。", "t-err"); return; }
        hits.slice(0, 6).forEach(function (p) { line('→ <a href="' + p.u + '">' + esc(p.t) + "</a>"); });
      },
      clear: function () { body.innerHTML = ""; },
      sudo: function () { line('<span class="t-err">权限不足：这里的管理员本来就是你。</span>'); },
      exit: function () { closeTerm(); }
    };
    input.addEventListener("keydown", function (e) {
      if (e.key === "Tab") {
        e.preventDefault();
        var v = input.value.trim().toLowerCase();
        if (!v) return;
        var names = Object.keys(TC).filter(function (c) { return c.indexOf(" ") < 0 && c.indexOf(v) === 0; });
        if (names.length === 1) input.value = names[0] + " ";
        else if (names.length > 1) line('<span class="t-dim">' + names.join("  ") + "</span>");
        return;
      }
      if (e.key !== "Enter") return;
      var s = input.value.trim(); input.value = "";
      if (!s) return;
      line('<span class="term-prompt">❯</span> ' + esc(s), "t-in");
      var sp = s.indexOf(" ");
      var head = (sp < 0 ? s : s.slice(0, sp)).toLowerCase();
      var rest = sp < 0 ? "" : s.slice(sp + 1);
      if (head === "ls" && rest.trim() === "-a") TC["ls -a"]();
      else if (TC[head]) TC[head](rest);
      else line('command not found: ' + esc(head), "t-err");
    });


  })();
(function () {
    "use strict";
    var D = {};
    try { D = JSON.parse(document.getElementById("__home_data").textContent) || {}; } catch (e) {}

    /* ============ 迷你终端（伏笔） ============ */
    var mt = document.getElementById("mini-term");
    var body = document.getElementById("term-body");
    var input = document.getElementById("term-input");
    function openTerm() {
      mt.classList.remove("hidden");
      mt.setAttribute("aria-hidden", "false");
      setTimeout(function () { input.focus(); }, 60);
      if (!body.childElementCount) {
        line('<span class="t-dim">you shouldn\'t be here.</span>');
        line('<span class="t-dim">（help 试试）</span>');
      }
    }
    function closeTerm() {
      mt.classList.add("hidden");
      mt.setAttribute("aria-hidden", "true");
    }
    document.getElementById("term-close").addEventListener("click", closeTerm);
    window.addEventListener("keydown", function (e) {
      if (e.key === "`" || e.key === "~") {
        e.preventDefault();
        mt.classList.contains("hidden") ? openTerm() : closeTerm();
      } else if (e.key === "Escape") { closeTerm(); }
    });
    function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

    function line(html, cls) {
      var el = document.createElement("div");
      el.className = "t-line " + (cls || "");
      el.innerHTML = html;
      body.appendChild(el);
      body.scrollTop = body.scrollHeight;
    }
    var TC = {
      help: function () {
        line("可用：<span class='t-cmd'>whoami ls cat xxd omori find clear exit</span>");
        line('<span class="t-dim">……以及没列出来的。</span>');
      },
      whoami: function () { line("<b>NirvanaCeleste</b> · 有几个秘密藏在站里"); },
      ls: function () { line('<span class="t-ok">acm/</span>  <span class="t-ok">omori/</span>  <span class="t-dim">search.md</span>'); },
      "ls -a": function () { TC.ls(); line('<span class="t-ws">.secret   setting_theme_core.css</span>'); },
      cat: function (r) {
        if ((r || "").trim() === ".secret") {
          line('<span class="t-dim">「位相偏移了。角落里有个说谎的文件——自称 css，却不是。」</span>');
          line('<span class="t-dim">（xxd setting_theme_core.css）</span>');
        } else if ((r || "").indexOf("setting_theme_core") >= 0) {
          line("cat: 二进制文件 <span class='t-dim'>（css 会是二进制的吗？）</span>", "t-err");
        } else line("cat: 没有那个文件", "t-err");
      },
      xxd: function (r) {
        if ((r || "").indexOf("setting_theme_core") >= 0) {
          line("<pre class='t-pre'>00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG....</pre>");
          line("魔数 <b>89 50 4E 47</b> —— 是一张 <b>PNG</b>。", "t-ok");
          line('→ <a href="/setting_theme_core.css">/setting_theme_core.css</a> 剩下的谜题，在现实里。');
        } else line("xxd: 没有那个文件", "t-err");
      },
      omori: function () {
        var on = document.documentElement.classList.toggle("ws-mode");
        line(on ? '<span class="t-ws">……这里什么都没有。</span>' : "欢迎回来。");
      },
      find: function (r) {
        var q = (r || "").trim().toLowerCase();
        if (!q) { line("用法：find 关键词"); return; }
        var hits = (D.posts || []).filter(function (p) { return (p.t + " " + (p.g || "")).toLowerCase().indexOf(q) >= 0; });
        if (!hits.length) { line("没找到。", "t-err"); return; }
        hits.slice(0, 6).forEach(function (p) { line('→ <a href="' + p.u + '">' + esc(p.t) + "</a>"); });
      },
      clear: function () { body.innerHTML = ""; },
      sudo: function () { line('<span class="t-err">权限不足：这里的管理员本来就是你。</span>'); },
      exit: function () { closeTerm(); }
    };
    input.addEventListener("keydown", function (e) {
      if (e.key === "Tab") {
        e.preventDefault();
        var v = input.value.trim().toLowerCase();
        if (!v) return;
        var names = Object.keys(TC).filter(function (c) { return c.indexOf(" ") < 0 && c.indexOf(v) === 0; });
        if (names.length === 1) input.value = names[0] + " ";
        else if (names.length > 1) line('<span class="t-dim">' + names.join("  ") + "</span>");
        return;
      }
      if (e.key !== "Enter") return;
      var s = input.value.trim(); input.value = "";
      if (!s) return;
      line('<span class="term-prompt">❯</span> ' + esc(s), "t-in");
      var sp = s.indexOf(" ");
      var head = (sp < 0 ? s : s.slice(0, sp)).toLowerCase();
      var rest = sp < 0 ? "" : s.slice(sp + 1);
      if (head === "ls" && rest.trim() === "-a") TC["ls -a"]();
      else if (TC[head]) TC[head](rest);
      else line('command not found: ' + esc(head), "t-err");
    });


  })();
