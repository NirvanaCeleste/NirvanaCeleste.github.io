---
title: "07 · 武器与饰品"
date: 2026-09-28
weight: 7
draft: false
comments: true
showTableOfContents: true
description: "OMORI 模组制作指南中文翻译 · 武器与饰品 — 最简单的装备系统"
---

![](/img/omori-guide/img_0000_56e2482692.webp)

你懂的,在经历了那么多 <span class="og-g">JavaScript</span>和多半有点 bug 的状态机制讲解之后,来讲点简单的东西正合适。

“嘿,我怎么做一个酷炫的武器?”

哦,谢天谢地,总算来了个简单的问题。

是啊。算我俩幸运,`Weapons`和 `Charms`是 <span class="og-g">OMORI</span> 里最容易实现的东西之一,所以这部分会很简短。

![](/img/omori-guide/img_0000_e7512f3750.webp)

*(来源:TomatoRadio)*

好啦。快速过一遍这些东西都是干什么的。

- `Name`:就是名字。别忘了全部大写。
- `Description`:就是描述。记得用 `<br>` 来换行。
- `Weapon Type`:谁能装备它?
- `Animation`:**别用这个**
- `Price`:**别用这个**
- `Parameter Changes`:属性变化。记住 `MP`就是果汁, `Agility`是速度,而 **M. Attack/M. Defense 是用不到的。**
- `Traits`:这些和 `states`选项卡里的完全一样,我就不重复了。只要知道:你需要给所有武器设置命中率,而且 Omori 和 Sunny 的武器用 `Lock Equip` 特性来防止你更换它们。

接下来再快速过一轮 `Notes Section`:

- `<IconIndex:`<var>x</var>`>` 决定使用的图标。它基于 `img/system/itemWeapons.png`,从 <var>0</var> 开始编号,从左到右、从上到下。饰品用的则是`img/system/itemCharms.png`。
- `<PassiveState:`<var>x</var>`>` 在装备期间,按 id 将指定的 `state` 施加给佩戴者。
