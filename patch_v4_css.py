# -*- coding: utf-8 -*-
"""CSS v4：终端主角 + 状态栏 + chips + 输入框修复；清掉图表/键盘专属样式（保留 heatmap 用的 chart-head/title）"""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = "assets/css/custom.css"
t = open(p, encoding="utf-8").read()

# 1) 删除旧 home-hero/home-stats/stat-* 块与 viz 图表/键盘样式块
m = re.search(r'/\* ---------- 首页：WHITE SPACE 场景 \+ 统计卡 ---------- \*/.*?/\* ---------- 首页：图表 \+ 补题键盘 ---------- \*/', t, re.S)
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

/* ---------- 首页面板通用（热力图沿用） ---------- */"""
t = t.replace(m.group(0), new_home)

# 2) 删除 chart/kb 专属规则（保留 .chart-panel/.chart-head/.chart-title/.chart-tabs? tabs 无用了；保留 panel/head/title 给 hm 用）
m = re.search(r'\.chart-box \{ position:relative; \}.*?\.kb-dim \{[^}]*\}\n', t, re.S)
assert m, "chart kb rules"
t = t.replace(m.group(0), "")

open(p, "w", encoding="utf-8", newline="\n").write(t)
print("css v4 done, len =", len(t))
