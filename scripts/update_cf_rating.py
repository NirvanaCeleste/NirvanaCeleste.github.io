# -*- coding: utf-8 -*-
"""更新 static/data/cf-rating.json（/acm/ 首页 rating 走势卡的数据快照）。

用法：python scripts/update_cf_rating.py
打完一场 rated 比赛后跑一次，然后随文章一起 commit/push 即可。
"""
import json
import ssl
import urllib.request

HANDLE = "NirvanaCeleste"
OUT = "static/data/cf-rating.json"
API = f"https://codeforces.com/api/user.rating?handle={HANDLE}"

ctx = ssl.create_default_context()
with urllib.request.urlopen(API, context=ctx, timeout=30) as resp:
    d = json.load(resp)
if d.get("status") != "OK":
    raise SystemExit(f"CF API 失败: {d.get('comment')}")

rows = []
for r in d["result"]:
    name = r["contestName"].replace(" (Div. 2)", "").replace(" (Div. 3)", "").strip()
    rows.append({
        "contest": name,
        "rank": r["rank"],
        "old": r["oldRating"],
        "new": r["newRating"],
        "ts": r["ratingUpdateTimeSeconds"],
    })

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
print(f"已写入 {OUT}（{len(rows)} 场 rated，最新 {rows[-1]['new']}）")
