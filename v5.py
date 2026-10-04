# -*- coding: utf-8 -*-
"""首页 v5：纯控制台，零算法竞赛展示
删：状态栏/热力日历/双入口卡/omori-dlg/全部统计数据注入
终端导航补全：cd acm / cd omori / cd about，chips 同步
"""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = "layouts/index.html"
t = open(p, encoding="utf-8").read()

# 1) 数据注入整块替换：只留 posts
m = re.search(r'  \{\{/\* ===== 数据汇聚 ===== \*/\}\}.*?</script>\n', t, re.S)
assert m, "data block"
new_data = """  {{ $indexPosts := slice }}
  {{ range where site.RegularPages "Section" "in" (slice "acm" "omori") }}
    {{ $indexPosts = $indexPosts | append (dict "t" .Title "u" .RelPermalink "g" (delimit (.Params.tags | default slice) ",") ) }}
  {{ end }}

  <script id="__home_data" type="application/json">{{ dict "posts" $indexPosts | jsonify | safeJS }}</script>
"""
t = t.replace(m.group(0), new_data)

# 2) 状态栏移除
m = re.search(r'      <div class="term-status" role="status">.*?</div>\n    </div>\n', t, re.S)
assert m, "status bar"
t = t.replace(m.group(0), "    </div>\n")

# 3) chips 增补导航
old = """      <button class="t-chip" data-cmd="cd letters">cd letters</button>
      <button class="t-chip" data-cmd="whoami">whoami</button>"""
new = """      <button class="t-chip" data-cmd="cd letters">cd letters</button>
      <button class="t-chip" data-cmd="cd acm">cd acm</button>
      <button class="t-chip" data-cmd="cd omori">cd omori</button>
      <button class="t-chip" data-cmd="whoami">whoami</button>"""
assert old in t, "chips"
t = t.replace(old, new)

# 4) 热力日历 section + omori-dlg div 移除
m = re.search(r'  \{\{/\* ===== 活跃热力日历 ===== \*/\}\}.*?</section>\n\n?', t, re.S)
assert m, "heatmap section"
t = t.replace(m.group(0), "")
old = """  {{/* OMORI 同款手绘对话框 tooltip */}}
  <div class="omori-dlg" id="omori-dlg" aria-hidden="true"><span class="omori-dlg-text"></span></div>

"""
assert old in t, "omori dlg"
t = t.replace(old, "")

# 5) 双入口卡移除
m = re.search(r'  \{\{/\* ===== 双入口 ===== \*/\}\}.*?</div>\n\n?', t, re.S)
assert m, "entries"
t = t.replace(m.group(0), "")

# 6) 第二脚本：删 omori-dlg/showDlg 与热力日历 JS（只留迷你终端）
m = re.search(r'    /\* ============ OMORI 对话框（打字机） ============ \*/.*?\}\n    var TC = \{', t, re.S)
assert m, "dlg js"
t = t.replace(m.group(0), "    var TC = {")
m = re.search(r'    /\* ============ 活跃热力日历 ============ \*/.*?\n  \}\)\(\);\n', t, re.S)
assert m, "hm js"
t = t.replace(m.group(0), "\n  })();\n")

# 7) ROOMS 增补导航目的地
old = """    var ROOMS = {
      album: { path: "/album/" },
      door: { path: "/door/" },
      letters: { path: "/letters/" }
    };"""
new = """    var ROOMS = {
      album: { path: "/album/" },
      door: { path: "/door/" },
      letters: { path: "/letters/" },
      acm: { path: "/acm/" },
      omori: { path: "/omori/modding-guide/" },
      about: { path: "/about/" }
    };"""
assert old in t, "rooms"
t = t.replace(old, new)

open(p, "w", encoding="utf-8", newline="\n").write(t)
print("index v5 done")

# ============ CSS ============
c = "assets/css/custom.css"
s = open(c, encoding="utf-8").read()

# 删状态栏样式
m = re.search(r'/\* tmux 风状态栏（统计并入终端） \*/.*?\.ts-right \{[^}]*\}\n', s, re.S)
assert m, "status css"
s = s.replace(m.group(0), "")
# 删 omori-dlg 样式块
m = re.search(r'/\* ---------- 首页：OMORI 手绘对话框 tooltip（打字机） ---------- \*/.*?(?=/\* ---------- )', s, re.S)
assert m, "dlg css"
s = s.replace(m.group(0), "")
# 删热力日历样式块
m = re.search(r'/\* ---------- 首页：活跃热力日历 ---------- \*/.*?(?=/\* ---------- )', s, re.S)
assert m, "hm css"
s = s.replace(m.group(0), "")
# 删残留的 chart-head/title（已无使用者）
m = re.search(r'/\* ---------- 首页面板通用（热力图沿用 head/title） ---------- \*/.*?\n', s, re.S)
assert m, "chart head css"
s = s.replace(m.group(0), "")
# 终端加高
s = s.replace(".home-term { height:480px; position:relative; }", ".home-term { height:540px; position:relative; }")
s = s.replace("  .home-term { height:420px; }", "  .home-term { height:440px; }")

open(c, "w", encoding="utf-8", newline="\n").write(s)
print("css v5 done")
