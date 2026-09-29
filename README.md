# NirvanaCeleste's Blog

Hugo + [Blowfish](https://github.com/nunocoracao/blowfish)（Hugo Module 方式引入）+ GitHub Actions 部署到 GitHub Pages。
线上地址：`https://nirvanacelesteblog.dpdns.org/`（自定义域名，CNAME 解析到 github.io）。

## 目录结构

```
content/
  acm/            算法竞赛复盘（每场一个 page bundle：cf1123/index.md + 截图）
  acm/upsolve/    补题清单（自动聚合页，数据来自各帖 front matter 的 upsolve 字段）
  omori/          OMORI 模组制作指南（12 章中文翻译，series 组织）
  about/          关于页
layouts/
  index.html               首页（双入口卡片 + 最近发布）
  acm/upsolve.html         补题清单聚合模板
  shortcodes/ratings.html  CF + AtCoder 双 rating 走势卡（构建期渲染 SVG）
  partials/head.html       head 覆盖：KaTeX（仅 acm 分区）+ 灯箱 + 阅读进度条 + 跳题按钮数据
  partials/rating-card.html 单平台走势卡（被 ratings.html 调用）
assets/css/custom.css      全部自定义样式（chips / 补题清单 / rating 卡 / 跳题按钮 / 暗色适配）
static/
  data/cf-rating.json      Codeforces rating 快照（脚本生成，见下）
  data/atcoder-rating.json AtCoder rating 快照（同上）
  js/probnav.js            帖子跳题按钮（读 front matter upsolve 状态着色）
  lib/katex/               自托管 KaTeX
scripts/
  update_ratings.py        拉取 CF + AtCoder 刷新两份 rating 快照
  check_links.py           构建后检查站内死链（CI 会跑）
```

## 日常流程

写一篇新复盘：

```bash
hugo new acm/cfXXXX/index.md     # 用 archetypes/acm.md 模板
# 截图放进同一文件夹（page bundle），正文里直接 ![名字](名字.png)
hugo server -D                   # 本地预览 http://localhost:1313
```

- front matter 里的 `upsolve:` 列表是补题清单的数据源：
  `status: wrong`（赛时交了没过/没调出来）、`skip`（根本没尝试）、`done`（赛后已补）。
  补完一道题把对应条目改成 `done`，[/acm/upsolve/](/acm/upsolve/) 会自动更新。
- 打完 rated 比赛刷新 rating 走势：`python scripts/update_ratings.py`（CF + AtCoder 都会更新；牛客没有公开 API 暂不支持），然后一起 commit。
- 复盘帖正文顶部会自动出现「跳题」按钮栏：A/B/C/D… 一键跳到对应题目，颜色按 upsolve 状态标（绿=过了、红=没写对、蓝=没尝试；没有 upsolve 字段的帖子是中性紫色）。

提交推送即部署（GitHub Actions：`hugo --minify` → pagefind 建索引 → 内链检查 → 发布）。

## 注意事项（踩过的坑）

- **`static/setting_theme_core.css` 是 ARG 用的伪装文件（PNG），不要动、不要移动、不要"修复"。**
- CI 的 Hugo 版本钉在 `0.164.0`（`peaceiris/actions-hugo`），本地也用同版本以免行为不一致。
- 图片必须放 page bundle 或 `static/`，raw HTML 里引用的资源 Hugo 不会自动发布。
- front matter 控制构建用 `build:`（老写法 `_build:` 在 Hugo 0.145+ 已移除）。
- KaTeX 只在 acm 分区加载（`layouts/partials/math.html` 里按 `.Section` 判断），别的页面写 `$` 不会当公式。
