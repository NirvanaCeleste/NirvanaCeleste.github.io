# -*- coding: utf-8 -*-
"""首页 v4：纯控制台方向
1. 删 viz-row（图表+键盘）及其 JS/CSS
2. 统计卡 → 终端底部 tmux 风状态栏（可点击）
3. 修 #ht-input 被 Tailwind 全局样式污染（紫边框/padding）
4. 终端变主角：居中放大、聚焦发光、快捷命令 chips
"""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = "layouts/index.html"
t = open(p, encoding="utf-8").read()

# ---- A) 数据注入瘦身：去掉 hist / board ----
old = '"ac" (dict "now" $acNow "delta" $acDelta "n" $acN "last" $acLast "hist" $acHist) "contests" (len $ups) "wrong" $wrong "skip" $skip "done" $done "posts" $indexPosts "board" $board "days" $days | jsonify | safeJS }}'
new = '"ac" (dict "now" $acNow "delta" $acDelta "n" $acN "last" $acLast) "contests" (len $ups) "wrong" $wrong "skip" $skip "done" $done "posts" $indexPosts "days" $days | jsonify | safeJS }}'
assert old in t, "inject"
t = t.replace(old, new)
old = '"cf" (dict "now" $cfNow "delta" $cfDelta "n" $cfN "last" $cfLast "hist" $cfHist)'
new = '"cf" (dict "now" $cfNow "delta" $cfDelta "n" $cfN "last" $cfLast)'
t = t.replace(old, new)

# ---- B) 删统计卡 section + viz-row section ----
m = re.search(r'  \{\{/\* ===== 统计卡 ===== \*/\}\}.*?</section>\n\n?', t, re.S)
assert m, "stats section"
t = t.replace(m.group(0), "")
m = re.search(r'  \{\{/\* ===== 可视化：rating 图表 \+ 补题键盘 ===== \*/\}\}.*?</section>\n\n?', t, re.S)
assert m, "viz section"
t = t.replace(m.group(0), "")

# ---- C) 终端升级：hero 包裹 + 状态栏 + chips ----
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

# chips 逻辑挂进终端脚本
old = """    var lines = [
      ["Nirvana Celeste Space", "t-sys"],
      ["You have been living here for as long as you can remember.", "t-dim"],
      ["输入 help 查看命令", "t-ok"]
    ];"""
new = """    document.querySelectorAll(".t-chip").forEach(function (ch) {
      ch.addEventListener("click", function () {
        input.value = ch.dataset.cmd || "";
        input.focus({ preventScroll: true });
        run(input.value.trim());
        input.value = "";
      });
    });

    var lines = [
      ["Nirvana Celeste Space", "t-sys"],
      ["You have been living here for as long as you can remember.", "t-dim"],
      ["输入 help · 或点下方的快捷命令", "t-ok"]
    ];"""
assert old in t, "boot"
t = t.replace(old, new)

# ---- D) 删第二脚本里的图表/键盘/countUp ----
m = re.search(r'    /\* ============ Rating 交互图表 ============ \*/.*?/\* ============ 活跃热力日历 ============ \*/', t, re.S)
assert m, "chart+kb"
t = t.replace(m.group(0), "    /* ============ 活跃热力日历 ============ */")

m = re.search(r'\n    /\* ============ 统计卡数字增长 ============ \*/.*?\}\)\(\);\n  \}\)\(\);', t, re.S)
assert m, "countup"
t = t.replace(m.group(0), "\n  })();")

open(p, "w", encoding="utf-8", newline="\n").write(t)
print("index.html v4 done")
