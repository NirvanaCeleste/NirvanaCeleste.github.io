# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = "layouts/index.html"
t = open(p, encoding="utf-8").read()

# ---- 终端区块升级（hero + 状态栏 + chips） ----
old = """  {{/* ===== 明面终端：导航启动器（输命令进入页面） ===== */}}
  <section class="home-term-row" aria-label="交互终端">
    <div class="term-window home-term" id="ht-window">
      <div class="term-bar">
        <span class="term-dot" style="background:#ff5f57"></span>
        <span class="term-dot" style="background:#febc2e"></span>
        <span class="term-dot" style="background:#28c840"></span>
        <span class="term-title">nirvana@blog: ~/home</span>
        <span class="term-hint">输入 help</span>
      </div>
      <div class="term-body" id="ht-body" aria-live="polite"></div>
      <div class="term-input-line">
        <span class="term-prompt" id="ht-prompt">❯</span>
        <input id="ht-input" autocomplete="off" spellcheck="false" enterkeyhint="send" aria-label="终端输入">
      </div>
    </div>
  </section>"""
new = """  {{/* ===== 明面终端：首页主角 ===== */}}
  <section class="term-hero" aria-label="交互终端">
    <div class="term-window home-term" id="ht-window">
      <div class="term-bar">
        <span class="term-dot" style="background:#ff5f57"></span>
        <span class="term-dot" style="background:#febc2e"></span>
        <span class="term-dot" style="background:#28c840"></span>
        <span class="term-title">nirvana@blog: ~/home</span>
        <span class="term-hint">输入 help</span>
      </div>
      <div class="term-body" id="ht-body" aria-live="polite"></div>
      <div class="term-input-line">
        <span class="term-prompt" id="ht-prompt">❯</span>
        <input id="ht-input" autocomplete="off" spellcheck="false" enterkeyhint="send" aria-label="终端输入">
      </div>
      <div class="term-status" role="status">
        <a class="ts-cell" href="https://codeforces.com/profile/NirvanaCeleste" target="_blank" rel="noopener">CF <b>{{ $cfNow }}</b><i class="{{ if ge $cfDelta 0 }}up{{ else }}down{{ end }}">{{ if ge $cfDelta 0 }}+{{ end }}{{ $cfDelta }}</i></a>
        <a class="ts-cell" href="https://atcoder.jp/users/NirvanaCeleste" target="_blank" rel="noopener">AC <b>{{ $acNow }}</b><i class="{{ if ge $acDelta 0 }}up{{ else }}down{{ end }}">{{ if ge $acDelta 0 }}+{{ end }}{{ $acDelta }}</i></a>
        <a class="ts-cell" href="/acm/">复盘 <b>{{ len $ups }}</b></a>
        <a class="ts-cell" href="/acm/upsolve/">待补 <b>{{ add $wrong $skip }}</b><i class="warn">🔥{{ $wrong }}</i></a>
        <span class="ts-right">UTF-8 · zh-CN</span>
      </div>
    </div>
    <div class="term-chips" aria-label="快捷命令">
      <button class="t-chip" data-cmd="help">help</button>
      <button class="t-chip" data-cmd="ls">ls</button>
      <button class="t-chip" data-cmd="cd album">cd album</button>
      <button class="t-chip" data-cmd="cd door">cd door</button>
      <button class="t-chip" data-cmd="cd letters">cd letters</button>
      <button class="t-chip" data-cmd="whoami">whoami</button>
    </div>
  </section>"""
assert old in t, "term block"
t = t.replace(old, new)

# ---- chips JS + 开机行 ----
old = """    var lines = [
      ["Nirvana Celeste Space", "t-sys"],
      ["You have been living here for as long as you can remember.", "t-dim"],
      ["输入 help 查看命令", "t-ok"]
    ];"""
new = """    document.querySelectorAll(".t-chip").forEach(function (ch) {
      ch.addEventListener("click", function () {
        run(ch.dataset.cmd || "");
        input.focus({ preventScroll: true });
      });
    });

    var lines = [
      ["Nirvana Celeste Space", "t-sys"],
      ["You have been living here for as long as you can remember.", "t-dim"],
      ["输入 help · 或点下方的快捷命令", "t-ok"]
    ];"""
assert old in t, "boot"
t = t.replace(old, new)

# ---- 删第二脚本的图表+键盘段 ----
m = re.search(r'    /\* ============ Rating 交互图表 ============ \*/.*?/\* ============ 活跃热力日历 ============ \*/', t, re.S)
assert m, "chart+kb"
t = t.replace(m.group(0), "    /* ============ 活跃热力日历 ============ */")

# ---- 删 countUp 段：从注释起到该脚本收尾 })(); 之前 ----
i = t.index("    /* ============ 统计卡数字增长 ============ */")
j = t.index("\n  })();", i)
t = t[:i] + t[j:]

open(p, "w", encoding="utf-8", newline="\n").write(t)
print("index v4 done")

# ================= CSS =================
c = "assets/css/custom.css"
s = open(c, encoding="utf-8").read()
m = re.search(r'/\* ---------- 首页：WHITE SPACE 场景 \+ 统计卡 ---------- \*/.*?/\* ---------- 首页：图表 \+ 补题键盘 ---------- \*/', s, re.S)
assert m, "old home css"
new_home = """/* ---------- 首页：控制台主角 ---------- */
.term-hero { max-width:900px; margin:1.2em auto 1.6em; }
.home-term { height:480px; }
.home-term .term-body { font-size:.95em; line-height:1.7; }
.home-term:focus-within { border-color:rgba(154,111,240,.65);
  box-shadow:0 0 0 3px rgba(154,111,240,.14), 0 18px 48px rgba(0,0,0,.4); }
.term-input-line input,
.term-input-line #ht-input,
.term-input-line #term-input {
  background:transparent !important; border:none !important; outline:none !important;
  box-shadow:none !important; padding:0 !important; margin:0 !important;
  color:#f0f0f8; caret-color:#7ee787; font:inherit; border-radius:0;
  min-height:0; height:1.6em; -webkit-appearance:none; appearance:none; }
.term-status { display:flex; align-items:center; gap:.2em; padding:.45em .9em;
  background:rgba(255,255,255,.05); border-top:1px solid rgba(255,255,255,.09);
  font-family:Consolas,"Cascadia Mono",monospace; font-size:.78em; overflow-x:auto;
  scrollbar-width:none; }
.term-status::-webkit-scrollbar { display:none; }
.ts-cell { display:inline-flex; align-items:baseline; gap:.4em; color:#b9b9c6;
  text-decoration:none !important; padding:.25em .55em; border-radius:6px;
  white-space:nowrap; transition:background .15s, color .15s; }
.ts-cell b { color:#e6e6f0; font-weight:700; }
.ts-cell i { font-style:normal; font-size:.88em; }
.ts-cell i.up { color:#7ee787; }
.ts-cell i.down { color:#ff7b72; }
.ts-cell i.warn { color:#f2cc60; }
.ts-cell:hover { background:rgba(154,111,240,.18); color:#fff; }
.ts-right { margin-left:auto; color:#5f5f72; white-space:nowrap; }
.term-chips { display:flex; flex-wrap:wrap; gap:.5em; justify-content:center; margin-top:.9em; }
.t-chip { font-family:Consolas,"Cascadia Mono",monospace; font-size:.8em;
  color:#c9c9dd; background:rgba(20,20,26,.8); border:1px solid rgba(154,111,240,.35);
  border-radius:999px; padding:.32em .95em; cursor:pointer; transition:all .15s; }
.t-chip:hover { background:rgba(154,111,240,.22); color:#fff; transform:translateY(-2px);
  box-shadow:0 5px 14px rgba(154,111,240,.25); }
html.ws-mode { filter:grayscale(1) contrast(1.06); transition:filter .8s ease; }

/* ---------- 首页面板通用 ---------- */"""
s = s.replace(m.group(0), new_home)

m = re.search(r'\.chart-box \{ position:relative; \}.*?\.kb-dim \{[^}]*\}\n', s, re.S)
assert m, "chart kb rules"
s = s.replace(m.group(0), "")

open(c, "w", encoding="utf-8", newline="\n").write(s)
print("css v4 done")
