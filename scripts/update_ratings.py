# -*- coding: utf-8 -*-
"""刷新 static/data/ 下的 rating 快照（/acm/ 首页走势卡的数据源）。

用法：python scripts/update_ratings.py
打完 rated 比赛跑一次，然后随文章一起 commit/push。
- Codeforces：官方 API
- AtCoder：history/json（非官方但长期稳定的接口）
- 牛客：没有公开接口，暂不支持
"""
import json
import re
import ssl
import urllib.request

OUT_CF = "static/data/cf-rating.json"
OUT_AC = "static/data/atcoder-rating.json"
CF_API = "https://codeforces.com/api/user.rating?handle=NirvanaCeleste"
AC_API = "https://atcoder.jp/users/NirvanaCeleste/history/json"

ctx = ssl.create_default_context()


def get(url):
    with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
        return json.load(resp)


# Codeforces
d = get(CF_API)
if d.get("status") != "OK":
    raise SystemExit(f"CF API 失败: {d.get('comment')}")
rows = [{
    "contest": r["contestName"].replace(" (Div. 2)", "").replace(" (Div. 3)", "").strip(),
    "rank": r["rank"],
    "old": r["oldRating"],
    "new": r["newRating"],
    "ts": r["ratingUpdateTimeSeconds"],
} for r in d["result"]]
with open(OUT_CF, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
print(f"CF: {len(rows)} 场，最新 {rows[-1]['new']}")

# AtCoder
rows = []
for r in get(AC_API):
    if not r.get("IsRated"):
        continue
    m = re.match(r"^abc(\d+)$", r.get("ContestScreenName", ""))
    name = f"ABC {m.group(1)}" if m else r["ContestNameEn"][:28]
    rows.append({
        "contest": name,
        "rank": r["Place"],
        "old": r["OldRating"],
        "new": r["NewRating"],
        "perf": r["Performance"],
    })
with open(OUT_AC, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
print(f"AtCoder: {len(rows)} 场，最新 {rows[-1]['new']}")
