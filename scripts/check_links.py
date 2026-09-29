# -*- coding: utf-8 -*-
"""检查 public/ 里所有站内链接（href/src）是否都有对应文件。

用法：在仓库根目录构建后运行  python scripts/check_links.py [public目录]
CI 在 pagefind 索引完成后跑一遍，内链 404（图片忘拷、别名写错等）直接挂掉构建。
"""
import os
import re
import sys
from urllib.parse import unquote

root = sys.argv[1] if len(sys.argv) > 1 else "public"
ATTR = re.compile(r'(?:href|src)=["\'](.*?)["\']', re.I)
broken = []

for dirpath, _dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        try:
            html = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for url in ATTR.findall(html):
            url = url.strip()
            if not url or url.startswith(("http://", "https://", "#", "data:", "mailto:", "//", "/pagefind/")):
                continue
            path = unquote(url.split("#", 1)[0].split("?", 1)[0])
            if not path.startswith("/"):
                path = "/" + os.path.relpath(os.path.join(dirpath, path), root).replace(os.sep, "/")
            if os.path.isfile(os.path.join(root, path.lstrip("/"))):
                continue
            if os.path.isfile(os.path.join(root, path.lstrip("/"), "index.html")):
                continue
            broken.append((os.path.relpath(p, root), url))

if broken:
    print(f"发现 {len(broken)} 个失效内链：")
    for src, url in broken:
        print(f"  {src} -> {url}")
    sys.exit(1)
print("内链检查通过。")
