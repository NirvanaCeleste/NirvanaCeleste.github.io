---
title: "OMORI 模组制作指南(中文翻译)"
date: 2026-09-28
weight: 0
draft: false
comments: true
description: "OMORI Modding Guide 中文翻译版——从零开始制作 OMORI 模组的社区教程"
---

> 本文档由社区指南《OMORI Modding Guide - WIP》(作者:**FruitDragon & TomatoRadio**)翻译为简体中文,共 12 章,覆盖从环境搭建到插件开发的 OMORI 模组制作全流程。
> 原文配色约定:**紫色 = 代码/路径/命令**、<var>红色 = 需替换的变量</var>、<span class="og-g">绿色 = 程序名</span>、蓝色 = 超链接。

## 章节目录

1. **[准备工作与 GitHub](/omori/modding-guide/01-setup/)** — 环境搭建、工具选择与团队协作
2. **[YAML 文件与对话](/omori/modding-guide/02-yaml/)** — 对话文本系统、格式代码与脸图
3. **[事件](/omori/modding-guide/03-events/)** — 事件页、插件命令、脚本与实例
4. **[地图](/omori/modding-guide/04-maps/)** — Tiled 制图全流程与图块集
5. **[精灵图与美术](/omori/modding-guide/05-sprites-art/)** — 全部图像资源规格
6. **[状态与情绪](/omori/modding-guide/06-states/)** — 特性、参数与情绪系统
7. **[武器与饰品](/omori/modding-guide/07-weapons-charms/)** — 最简单的装备系统
8. **[技能与物品](/omori/modding-guide/08-skills-items/)** — 伤害公式、备注标签与追击
9. **[队伍成员与敌人](/omori/modding-guide/09-party-enemies/)** — 角色、AI 与多阶情绪 Boss
10. **[插件与 OneMaker MV](/omori/modding-guide/10-plugins/)** — 社区资源与编辑器增强
11. **[常见错误与技巧](/omori/modding-guide/11-errors/)** — 报错排查速查
12. **[致谢与开发者内容](/omori/modding-guide/12-thanks/)** — 社区资源索引


## 术语表

本翻译的译名与 **RPG Maker MV 官方简体中文版**保持一致；少数有意差异在备注列说明。

| 英文 | 本翻译 | RPG MV 官方 | 备注 |
|---|---|---|---|
| Event | 事件 | 事件 | |
| Map | 地图 | 地图 | |
| Switch | 开关 | 开关 | |
| Variable | 变量 | 变量 | |
| Actor | 角色 | 角色 | |
| Item | 物品 | 物品 | 全文统一（初版曾混用"道具"） |
| Skill / Weapon / Armor | 技能 / 武器 / 防具 | 同左 | |
| Enemy / Troop | 敌人 / 敌群 | 同左 | |
| State | 状态 | 状态 | |
| Tileset / Tile | 图块集 / 图块 | 图块 | |
| Plugin / Plugin Command | 插件 / 插件命令 | 插件 | |
| Common Event | 公共事件 | 公共事件 | |
| Notetag | 备注标签 | （编辑器内为"备注"字段） | |
| Sprite | 精灵 / 精灵图 | — | |
| Playtest | 测试 | 测试运行 | 测试文件夹亦称"测试文件夹"(playtest folder) |
| Parallax | 视差背景 | 远景 | |
| Collision / Region / Layer | 碰撞 / 区域 / 图层 | 同左 | |
| GitHub: repository / commit / branch | 仓库 / 提交 / 分支 | — | |

## 欢迎

![](/img/omori-guide/img_0000_4d466d8afe.webp)

## 欢迎!

*如果你是来提反馈的,请留下你的名字,因为凡是提供了反馈、且该反馈最终被我们收录的人,我们都想为其献上特别鸣谢。*

最近我一直在制作 <span class="og-g">OMORI</span> 模组（mod）。但我注意到一件事——市面上缺乏那种教你 <span class="og-g">RPG Maker MV</span>、并且是从 <span class="og-g">OMORI</span>模组制作视角出发的教程。

于是,我们俩——[FruitDragon](https://mods.one/author/fruitdragon) 和 [TomatoRadio](https://mods.one/author/tomatoradio)——联手编写了这份指南,几乎涵盖了制作 <span class="og-g">OMORI</span>模组的方方面面!

点击其中任意一项即可跳转到对应的章节!这些章节按从上到下的顺序设计,遇到反复出现的概念时,会把你引回前面学过的内容。

*如果你用的是桌面版,还可以使用文档左侧的“文档标签(Document Tabs)”功能。你可能需要双击“The Actual Guide”才能将其展开,显示所有章节及其细分小节。*

注 1:本指南是写给初学者的教程,并不是用来学习 <span class="og-g">RPG Maker MV</span> 高级内容的。TomatoRadio 计划做一个自己的 wiki,尽可能多地记录与制作 <span class="og-g">OMORI</span> 模组相关的内容。注 2:本指南同样围绕我们(FruitDragon 和 TomatoRadio)对 <span class="og-g">RPG Maker MV</span> 和 <span class="og-g">OMORI</span> 的了解编写。如果你是位经验丰富的模组作者、知道别的做法,原因就在这里;不过如果你觉得自己的某些见解对这份指南有帮助,欢迎给我们任意一人发私信,我们会看看是否适合收录进来。
