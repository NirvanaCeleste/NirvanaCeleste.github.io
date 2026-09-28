---
title: "11 · 常见错误与技巧"
date: 2026-09-28
weight: 11
draft: false
comments: true
showTableOfContents: true
description: "OMORI 模组制作指南中文翻译 · 常见错误与技巧 — 报错排查速查"
---

\[这一节还需要正式排版。\]

这一小节用来收录一些放在别处都不太合适的常见报错和技巧。

### 常见崩溃/报错 **$atlasData is not Defined**

这大概是 Mod 制作中最常见的报错了。只要 `YAML` 文件无效,启动时就会触发。更具体地说,是你有重复的键。最常见的原因是复制了一条消息却忘了改名,于是出现了两个 `message_23`。把它们重命名就修好了。如果是在同一条消息里把同一个参数定义了两次(比如两个 `faceset`),也会触发。

**Cannot read property ‘tilewidth’ of undefined**

这个报错同样鼎鼎有名。加载被旋转或镜像过的图块时就会触发。你多半是做地图时手滑按到了 `Z` 键——那是旋转图块的快捷键。只要把这些旋转过的图块换回正常版本就能修好。另外提醒一句:`bucket` `tool`(油漆桶工具)会把旋转图块视为与普通图块不同的图块,万一你要搜索某个纯色的旋转图块,记得这一点。

你也可以干脆在 `Edit > Preferences > Keyboard >` 里

```text
RotateRight.
```

**Cannot read property ‘hp’ of null**

这是第一个需要靠 `plugin`才能修复的报错。如果战斗中没有 OMORI 或桑尼,游戏就会崩溃,因为它要读取他们的 `hp` 来决定要不要显示低血量覆盖层。要修复的话,请安装 [Nomori](https://github.com/modsone/omori-modding-resources/blob/main/ESSENTIAL%20plugins/rph.no%20omori%20crash.patch.js) 插件。

**Cannot read property ‘Window_ScrollingTextSource’ of undefined** 这个报错是因为缺少 `XX_Blue.yaml` 文件。一些运行旧版本的盗版游戏会出现这种情况。更新到 <span class="og-g">Steam 1.0.8 version</span> 即可解决。

**Failed to Load: img/pictures/OMORI_RS.png |**

**ERR_FILE_NOT_FOUND: OMORI_RS.png**

如果在没有配置 `Plugin Parameters` 的情况下带着 `FD_EasyTitleScreen` 启动游戏,就会出现这个报错。只要进入 `Plugin Manager`,把图片指定成你想要的,或者干脆删掉即可。另外,如果你想看看这些素材长什么样,它们就放在你下载插件的同一处,你可以把它们加进 `img/pictures`。

**Failed to Load: img/faces/default_face_image_here.png /**

**ERR_FILE_NOT_FOUND: default_face_image_here.png**

如果在没有添加默认图片的情况下带着 `Save Load Plus` 启动游戏,就会出现这个报错。`Save Load Plus` 菜单硬编码了一份角色 ID 及其对应图片的列表,找不到时回退到 `default_face_image_here`。只需往 img/faces 里放一张叫这个名字的图片就能修好。

**Failed to Load: img/faces/06_SUNNY_HOUSE_BATTLE.png /**

**ERR_FILE_NOT_FOUND: 06_SUNNY_HOUSE_BATTLE.png**

如果存档文件夹里有来自其他 Mod 的存档,而对应的 Mod 又没有加载,就会出现这个报错。这里的示例是 [Pink Tinted Love Stories](https://mods.one/mod/pinktintedlove) 的一张脸图,但几乎任何带自定义脸图的 的 Mod 都可能触发。要修复,请安装 [Mod Save File Fix](https://mods.one/mod/modsavefiles)。

**“游戏一开始我看不到玩家!”**

请确保在你的起始地图上添加一个 Autorun 事件,在玩家载入时取消玩家的透明状态。

**“战斗里我的角色轮不到行动!”**

这个报错源于游戏里相当诡异的硬编码:行动顺序被强制限定为 Headspace 或 Faraway 的队伍 ID。修复方法:要么使用 [Geo_AutoTurnOrder](https://github.com/modsone/omori-modding-resources/blob/main/ESSENTIAL%20plugins/Geo_AutoTurnOrder.js),按角色的 `BattleStatusIndex`备注标签或其在队伍中的位置来决定行动顺序;要么使用 [ActualTurnOrder](https://mods.one/mod/actualturnorder),按每个队员的速度决定行动顺序。

**“过场动画里我居然还能操作移动!”**

请确保你的过场动画通过一个 `Autorun`事件来运行,它在激活期间会锁住玩家移动。记得在过场结束时把这个事件关掉。

**“我的事件没有自动运行!”**

请确保把它设为 `Autorun`或 `Parallel`。如果设成 `Autorun`,记得在它跑完后把事件关掉。

**“我的图片显示在角色下面了!”**

这个报错源于 <span class="og-g">OMORI</span> 里的一个插件:它会把所有 ID 为`1`的 `Pictures`显示为 `Below Characters`(角色图层之下)。只要把 ID 换成其他任何数字,问题就能解决。

**“我有一个会切换角色行走图的事件,但切换前角色会** **先消失一小会儿!”**

这是图片加载需要时间造成的。要缓解这个问题,在切换发生前不远处加一条 <span class="og-g">Script</span> 命令,脚本内容如下:

```text
ImageManager.loadCharacter(“IMAGENAME”); 
```

这会把图片预先载入内存,等真正切换时加载时间就短了。
