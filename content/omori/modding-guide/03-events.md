---
title: "03 · 事件"
date: 2026-09-28
weight: 3
draft: false
comments: true
showTableOfContents: true
description: "OMORI 模组制作指南中文翻译 · 事件 — 事件页、插件命令、脚本与实例"
---

![](/img/omori-guide/img_0000_5be259f03c.webp)

![](/img/omori-guide/img_0000_8e62fc6224.webp)

嗯,事件就是游戏中发生的任何事情。就连玩家也是一种事件,不过这个层面的技术细节,我们这次就先略过不谈。

要打开 `Event Editor`(事件编辑器),点击 <span class="og-g">RPG Maker MV</span> 主窗口顶部的下面这个按钮即可。

![](/img/omori-guide/img_0000_0a0978b48d.webp)

*(来源:FruitDragon)*

### 制作事件

*强烈建议你在动手制作自己的事件之前,先查看与它类似的现成事件,弄清楚它们是如何运作的。*

*另外,你随时都可以复制/粘贴事件,然后再进行修改。*

要新建一个 `Event`(事件),你只需在 `Event Editor` 中双击任意空白方格。你会得到一个新页面,长得大概像这样:

*(来源:FruitDragon)*

谈到 `Events`(事件)时,有几点重要事项需要注意。首先,你能看到需要考虑的东西有多少——这正是因为 `Events` 可以做得非常具体。

我们会详细讲解几乎每一个区域。

![](/img/omori-guide/img_0000_299f6446b6.webp)

#### 事件页——顶部区域

这部分基本上一目了然。一个 `Event`(事件)可以拥有多个页面,而在这里你可以新建事件页、复制现有事件页(粘贴到别处,或在同一事件内再复制一份),也可以删除/清空现有事件页。

当然,你随时可以给事件命名。而备注框则用于一些特殊用途,比如扩展 `Event` 的 `Hitbox`(碰撞箱),或者修改事件的 `X/Y-offset`(X/Y 偏移)。

以下是一些可以写进备注框的 `Notetags`(备注标签):

碰撞箱修改类:

`<Hitbox Left:`<var>2</var>`>`(将碰撞箱向左扩展 <var>2</var> 格)

`<Hitbox Right:`<var>4</var>`>`(将碰撞箱向右扩展 <var>4</var> 格)

`<Hitbox Up:`<var>1</var>`>`(将碰撞箱向上扩展 <var>1</var> 格)

`<Hitbox Down:`<var>1</var>`>`(将碰撞箱向下扩展 <var>1</var>格)

精灵偏移:(正值表示向右/向下,负值表示向左/向上)

`<Sprite Offset Y:`<var>+20</var>`>`(精灵向下移动 <var>20</var> 像素)

`<Sprite Offset X:`<var>-3</var>`>`(精灵向左移动<var>3</var>像素)

`<Sprite Offset:`<var>+7, -5</var>`>`(精灵向右移动<var>7</var>像素,同时向上移动 <var>5</var>像素)

*注:这并不会改变事件的碰撞箱。*

Copy Event(复制事件):它的作用是把一个地图上的整个事件原封不动地复制过来,添加到另一个地图上。很适合用在那种你希望在多张地图上保持一致的特定敌人之类的事件上。

*注 1:你会遇到一些带有 Copy Event 标签、却没有写明自己复制的是哪个事件的事件。那些事件是借助插件来选定的。你通常可以在开发房间里找到它们所复制的那个事件。*

*注 2:你从中复制事件的地图,必须被添加进预加载地图列表中,*

*也就是 `Plugin Manager`(插件管理器)中的 YEP\_EventCopier。它在哪里、以及如何修改这类内容,可以在[插件](/omori/modding-guide/10-plugins/)章节中找到。*

`<Copy Event: Map`<var>46</var>`, Event`<var>3</var>`>`(行为与地图 <var>46</var>中的事件<var>3</var>完全一致。如果你想知道这是哪个事件——它就是遥远镇上贝西尔房间的门。)

触发范围修改类:扩大事件能被 `Player` `Touch`(玩家接触)或 `Event Touch`(事件接触)触发的区域,后面会详细解释。

`<Activation Square:`<var>4</var>`>`(将事件可被玩家接触或事件接触触发的范围,以正方形形状向外扩大 <var>4</var> 个单位。)

`<Activation Radius:`<var>2</var>`>`(将事件可被玩家接触或事件接触触发的范围,以菱形形状向外扩大 <var>2</var> 个单位。)

**Mini Label(迷你标签):**会让一小行文字——也就是“迷你标签”——显示在游戏中事件的上方。它基本上只在开发房间里使用,纯粹是为了便于整理。

```text
<Mini Label:label goes here> 
```

还有很重要的一点:事件页顶部的 <var>ID</var> 编号。这个 <var>ID</var> 编号对之后的 `Scripting`(脚本编写)很重要。有时候,给事件命名时把 <var>ID</var> 编号写进去是个好主意,这样不用每次打开事件页,就能轻松知道编号是多少。

![](/img/omori-guide/img_0000_5f0a313474.webp)

#### 事件页——出现条件

*(来源:FruitDragon)*

这些选项告诉你需要满足哪些 `Conditions`(条件)才能运行那个特定的事件页。由于一个事件里可以包含多个事件页,条件就能帮助区分它们。

**快速指南:**

- `Switches`(开关)是可用于触发事件的真/假语句。你可能也知道它们叫旗标(flag)或布尔值(boolean)。
- `Variables`(变量)就是字面意思——变量。
- `Self Switches`(独立开关)是专属于你当前正在编写的这个事件的真/假语句。它们本来不是给多个事件用的,不过借助 `Scripting`(脚本)也能做到,稍后细说。
- `Item`(道具):表示玩家背包里必须持有该道具。不能用来检查装备。
- `Actor`(角色):表示只有当该特定角色(Actor)在玩家队伍中时,事件才会运行。要检查带标签的角色,请放置一个

*检查以下脚本的 `Conditional Branch`(条件分支)*

```text
“$gameParty.leader()._actorId === ACTOR ID”
```

![](/img/omori-guide/img_0000_cb51d04ee5.webp)

![](/img/omori-guide/img_0000_f82aa075dc.webp)

`Event Pages`(事件页)按从左到右的优先级运行,所以如果 `Event` `Page 4` 和 `Event Page 6` 的 `Conditions`(条件)都满足,游戏就会运行 `Event Page 6`,因为它的优先级最高。

下面来看几个例子:

*(来源:FruitDragon)*

这组 `Conditions`(条件)意味着:除非 `Switch`(开关)<var>Mom’s Broom Equipped</var> 为真,否则这个 `Event Page`(事件页)不会运行——说白了,玩家不装备妈妈的扫帚,它就不运行。

![](/img/omori-guide/img_0000_29dff5e909.webp)

![](/img/omori-guide/img_0000_965ced95a1.webp)

*(来源:FruitDragon)*

这组条件意味着:当玩家已经开始整理(家务)、且 `Self Switch A`(独立开关 A)被触发时,该事件页就会运行。

*(来源:FruitDragon)*

这组 `Conditions`(条件)意味着:当 OMORI 在队伍中、且你正拿着道具时,该事件页才会运行。(这个特定条件在原版游戏里是不可能成立的——因为 <var>Holding Item</var> 这个 `Switch`(开关)是桑尼家中整理家务这项任务专用的。)

![](/img/omori-guide/img_0000_bf89e7f72a.webp)

*(来源:FruitDragon)*

这个则表示:当存档的 WTF 值大于或等于 10、且神秘药水在玩家背包中时,该事件页才会运行。

#### 事件页——图像

*(来源:FruitDragon)*

这部分也基本上一目了然。双击那个灰白相间的棋盘格方框,就会弹出一个图像选择窗口。

![](/img/omori-guide/img_0000_9eadb0c19a.webp)

*(来源:FruitDragon)*

在那里,你可以从 `img/characters` 文件夹中挑选一张精灵图,用作该事件的图像。

![](/img/omori-guide/img_0000_73d6bd298d.webp)

*(来源:FruitDragon)*

这些精灵图通常以 3 x 4 的基本行走动画组的形式存在——不过在某些情况下(比如上面那张),有些动画需要的精灵图会更少。想确切了解它们是如何运作的,可以直接跳到[精灵图章节](/omori/modding-guide/05-sprites-art/)。

文件夹里还有一些形状不同寻常的精灵图,选择时它们看起来会非常奇怪,因为它们需要借助插件才能使用。

除了真正的角色精灵图之外,还有一张很常用的图,通常用于开发目的:

![](/img/omori-guide/img_0000_a56dc046dd.webp)

*(来源:FruitDragon)*

最边上的那些方框,用来标记 `Tag Events`(标签事件)、`Camera`(摄像机)

以及传送事件(Teleport Events)、初始化事件(Initializing Events)、敌人(Enemies)等在

这些类型的事件分别位于地图上的什么位置——不然很难把它们区分开。`DEV_` 图集不会出现在游戏中,所以你不用担心会有个莫名其妙的 `INIT` 方框突然出现在森林游乐场正中央之类的状况。

#### 事件页——自主移动

这个框用来决定事件在未被触发时如何移动。

![](/img/omori-guide/img_0000_f61fbc5cde.webp)

![](/img/omori-guide/img_0000_525e50f1a7.webp)

![](/img/omori-guide/img_0000_f69525e762.webp)

![](/img/omori-guide/img_0000_2ee183849f.webp)

*(来源:FruitDragon)*

说实话,这些选项都相当一目了然。

![](/img/omori-guide/img_0000_7e1a9b298f.webp)

*你可以看看森林游乐场的过场剧情,见识一下它们大部分的高级用法。*

#### 事件页——优先级

*(来源:FruitDragon)*

`Priority`(优先级)决定事件处于地图的哪一层。

<var>Below characters</var>(角色之下)表示它位于角色的脚下面那一层。

<var>Same as characters</var>(与角色同层)表示它与角色处于同一层,就像挡在角色路中间的一件实体障碍物。

<var>Above characters</var>(角色之上)表示它在角色头顶上方,角色可以从它底下畅通无阻地走过去。

![](/img/omori-guide/img_0000_8d1155ce80.webp)

#### 事件页——触发方式

*(来源:FruitDragon)*

它决定事件如何被触发。

<var>Action Button</var>(动作按键)表示玩家必须使用动作按键来激活事件(OMORI 中默认是 Z 键)。如果事件是 <var>Above characters</var>(角色之上)或 <var>Below characters</var>(角色之下),玩家就必须站在它的下方/上面,按下动作按键来激活;而 <var>Same as characters</var>(与角色同层)则表示玩家需要站在旁边面对它,再按下动作按键。

<var>Player Touch</var>(玩家接触)表示玩家必须碰到事件才能激活它(如果事件是 <var>Same as characters</var>(与角色同层),还必须面对着该事件)。它也可以按照下列方式触发——即

动作按键(Action Button)。

<var>Event Touch</var>(事件接触)表示事件可以主动碰到玩家来激活自己。(玩家不需要面对该事件。)它也可以按照下列方式触发——即

动作按键(Action Button)或玩家接触(Player Touch)。

![](/img/omori-guide/img_0000_4538d4c8ba.webp)

<var>Autorun</var>(自动执行)表示只要条件一满足,它就会立刻自动运行。同时,它还会锁定玩家的所有移动,直到事件切换页面或被删除为止。

<var>Parallel</var>(并行)表示该事件页会与当时地图上正在运行的其他事件页同时运行。玩家的移动不会被锁定。

#### 事件页——选项

*(来源:FruitDragon)*

<var>Walking</var>(步行动画)表示行走动画只在事件移动时开启,且仅在当时开启。

<var>Stepping</var>(原地踏步)表示即使事件没有在移动,行走动画也会保持开启。

<var>Direction Fix</var>(朝向固定)表示事件中的角色无法改变朝向。如果你想让角色倒退着走路而不转身,或者某个角色只有单一朝向的精灵图,这个选项就非常有用。

<var>Through</var>(穿透)能让角色穿过平时无法通行的物体、图块和事件。

![](/img/omori-guide/img_0000_6f86bb1b2e.webp)

#### 事件页——内容

终于,我们来到了 `Event Editor`(事件编辑器)的最后一部分。

*(来源:FruitDragon)*

这个空空如也的框,就是放代码的地方。

“可是……”你问道,“什么代码?我们在这里到底能放什么?”

问得好,亲爱的未来 <span class="og-g">OMORI</span> 模组制作者!因为这正是我们的下一个话题!

### 事件代码

这一节大部分内容会是概述,因为要过一遍的东西实在太多了。想要更深入、更详细的讲解,可以去问问

*[Mods.one Discord 服务器](https://discord.gg/EDTMF85Hnp)或 [OMORI Modding Hub](https://discord.gg/pkBEr7ywCG) 里的某个人——说不定就是我们中的谁。*

双击内容框,你会得到下面这个菜单,里面有三页选项:

![](/img/omori-guide/img_0000_2dd36791a1.webp)

*(来源:FruitDragon)*

其中很多命令都不言自明,尤其是如果你已经会写代码的话,所以我只讲几个 <span class="og-g">OMORI</span> 里常用的,以及几个 <span class="og-g">RPG Maker MV</span> 比较特有的命令。

#### 事件命令——消息(Message)

这是个特例。<span class="og-g">OMORI</span> 使用另一套系统来显示文字、选项之类的内容。因此,这些命令一律别用。取而代之,你要使用下文会讲到的 `Plugin Command`(插件命令)。

#### 事件命令——游戏进度(Game Progression)

这些都非常重要,因为你可以靠它们来打开/关闭 `Switches`(开关)和 `Self Switches`(独立开关),修改 `Control Variables`(控制变量)的值,还能用现实时间而不是游戏帧数来设置计时器。

#### 事件命令——流程控制(Flow Control)

`Comments`(注释)很有用,能让你看明白事件页上正在发生什么,通常用来给 `Script`(脚本)做标注。

`Conditional Branches`(条件分支,或者说 If-Then/If-Else 语句)极其有用,可以让事件中的某些内容只在特定条件满足时才发生。它们和绝大多数编程语言里的 if-else 语句基本上是一回事。

`Exit Event Processing`(中止事件处理)**——**本质上是让事件在中途终止,就像按下一个大大的红色“停止”按钮。它不会解除 `Autorun`(自动执行)造成的玩家锁定,你必须切换 `Event Pages`(事件页)或删除该事件才行。

`Label`(标签)和 `Jump to Label`(跳转到标签)这类东西,看示例事件来理解效果要好得多,不过我会尽力讲清楚。

它们的作用类似标题,能让你跳过大段大段的代码。

由于 <span class="og-g">RPG Maker MV’s</span> 代码窗口是自上而下线性运行的,不借助 `Conditional Branches`(条件分支),想让某几段代码被跳过是极其困难的。`Labels`(标签)解决了这个问题。你在代码某处放一个 `Label`,再在代码另一处放一个跳转到该 `Label` 的 `Jump to Label`,代码就能从 `Jump` 语句直接跳到 `Label`,中间的内容一概不执行。反过来也成立——它还能让你不用循环就重复执行某些代码段。`Labels` 通常会和 `Conditional Branches`(条件分支)搭配使用。(它们还经常与 `Plugin`

命令 AddChoice 与 ShowChoices 搭配使用。)

最后是 `Common Events`(公共事件)。它们要复杂得多,所以我们单独给它们开一节。

##### 公共事件 vs. 地图事件 `Common Event`(公共事件)是可以在多个地方调用的事件,就像可复用的代码,或者用已经会编程的人的话说,是一个函数/方法。正如本指南[YAML 章节](/omori/modding-guide/02-yaml/)所提到的,它也可以被对话调用。这方面的例子包括 `Shake Screen`(震屏)事件、`Picnic Save`(野餐存档)事件等等——它们全都是在多个地方使用的东西,这样代码就不必每次都复制一遍。不绑定特定地点的事件也可以放在这里。原版游戏中的 `Tag System`(标签系统)事件就是一个例子,如下所示:

![](/img/omori-guide/img_0000_6281bc2cb7.webp)

*(来源:FruitDragon)*

由于标记(tagging)是在你使用菜单中的 Tag 选项时发生的,而不是在玩家与物体互动时发生的,所以它被做成了 `Common Event`(公共事件),好让菜单能够调用它。

`Map Event`(地图事件)是只出现在地图上某一个地点的事件,通常要具体得多。这方面的例子包括 `Cutscenes`(过场剧情)和 `Map` `Transitions`(地图转场),因为 `Map Transitions`(地图转场)需要具体的坐标,而 `Cutscenes`(过场剧情)需要特定的角色和对话。

有一点很重要:`Map Events`(地图事件)**可以调用**`Common Events`(公共事件)**,**但 `Common Events`(公共事件)**不能调用**`Map Events`(地图事件)**。话虽如此,**`Common Events`**可以调用其他**`Common Events`(公共事件)**。**

##### 并行公共事件

现在再往深一层:根据 `Trigger`(触发)条件的不同,`Common Events`(公共事件)分为三种类型。

大多数 `Common Events`(公共事件)都是由 `Map Events`(地图事件)触发的,我们把这类称为 `Regular Common Events`(常规公共事件),因为在整个游戏和大多数模组里,你主要见到的就是它们。不过还有另外两种类型,即 `Autorun`(自动执行)和 `Parallel Common Events`(并行公共事件),我们把它们统称为 `Automatic Common` `Events`(自动公共事件)。与 `Regular Common Events`(常规公共事件)不同,它们不由 `Map Events`(地图事件)调用,而是在某个 `Switch`(开关)处于开启状态时运行。`Autorun Common Events`(自动执行公共事件)在运行期间会锁定玩家的移动,而 `Parallel Common Events`(并行公共事件)则会与玩家和 `Map Events`(地图事件)并行运行。这两者非常适合用在你希望同时在许多地图上被动运行的系统上,这样你就不用在不同的地图上放置多个跑着同样代码的 `Map Events`(地图事件)了——万一以后需要全部修改,那可就麻烦了。

*还有一点值得注意:`Automatic Common Events`(自动公共事件)也可以像 `Regular Common Events`(常规公共事件)那样被 `Map Events`(地图事件)调用,尽管几乎没人这么用。*

##### 制作公共事件

要创建 `Common Event`(公共事件),你只需在 `Database`(数据库)里找一个空着的 `Common` `Event` 栏位,把代码填进去就行。另外,要给它指定上述类型,你需要把 `Trigger`(触发)选项改成想要的模式——<var>None</var>(无)对应 `Regular Common Event`(常规公共事件),然后再指派一个 `Switch`(开关)来控制 `Automatic Common Events`(自动公共事件)的启停。

![](/img/omori-guide/img_0000_18be6cf7e7.webp)

*(来源:FruitDragon)*

当然,别忘了给它命名!之后你想调用这个 `Common Event`(公共事件)的时候,就得靠名字认出它来。

![](/img/omori-guide/img_0000_05031dc791.webp)

*(来源:FruitDragon)*

除此之外,添加代码的方式和在 `Map Events`(地图事件)里写代码基本完全一样,所以我们回去继续讲地图事件吧!

*唯一值得注意的一点是:任何作用于 `Map Event`(地图事件)本身的命令*

(`Self Switches`(独立开关)、`Movement Routes`(移动路径)等)都会作用于 `Map Event`(地图事件),也就是调用这个 `Common`

*`Event`(公共事件)的那个事件。也因此,`Automatic Common Events`(自动公共事件)并不支持这些命令。*

#### 事件命令——移动(Movement)

这里我要专门讲讲 `Set Movement Route`(设置移动路径)。它就是你在过场剧情里让角色四处移动的方法。当你点击它时:

![](/img/omori-guide/img_0000_2ed9a87fad.webp)

*(来源:FruitDragon)*

`Movement Routes`(移动路径)用途极为广泛。这些选项大多不言自明,所以我会重点讲讲脚本(Script)选项提供的功能。这些脚本来自 [YEP_MoveRouteCore.js](http://www.yanfly.moe/wiki/Move_Route_Core_(YEP)) 插件,你可以在里面看到更多选项。我只讲基础部分。

```text
UP: x 
LEFT: x 
RIGHT: x 
DOWN: x 
UPPER LEFT: x 
UPPER RIGHT: x 
LOWER LEFT: x 
LOWER RIGHT: x 
JUMP FORWARD: x 
```

以上这些都会让事件朝所标明的方向移动 <var>x</var> 格。

```text
MOVE TO: x 
JUMP TO: x
STEP TOWARD: x
STEP AWAY FROM: x
TURN TOWARD: x
```

![](/img/omori-guide/img_0000_28c2e77e61.webp)

```text
TURN AWAY FROM: x
TELEPORT: x 
```

这些命令都一目了然,不过 <var>X</var> 在这里有特殊用法。<var>x</var> 可以是 <var>x, y</var>(精确的地图坐标),可以是 <var>EVENT X</var>(表示 `ID` 为 <var>X</var> 的那个 `event`(事件)),也可以是 <var>PLAYER</var>——至于这指的是什么嘛,我想你猜得到。

#### 事件命令——角色(Character)

这里我要专门讲讲 `Show Balloon Icon`(显示气泡图标)和 `Erase Event`(消除事件)。

`Show Balloon Icon`(显示气泡图标):显示那个有时会在过场剧情中弹出、用来表现角色心情的图标。

*注:要让这条命令正常工作,你需要设置两样东西:把 `Control Variable`(控制变量)“<var>Change Balloon Variable</var>”设为 <var>0</var>,然后运行 `Common Event`(公共事件)“<var>Balloon Image</var>”。这个只需要运行一次。*

源图像可以在 `img/system/balloon.png` 中找到。

`Erase Event`(消除事件):在玩家停留在当前地图期间,把该事件消除掉。当玩家离开地图再回来时,事件会重新出现。

#### 事件命令——图片、音频与视频(Picture, Audio & Video)

这些命令全都用于过场剧情和音效。可以去看看一些带过场剧情的事件(尤其是“`❈ >> BEGIN`”地图里的 INIT 事件),了解它们是如何运作的。

这些命令全都用于过场剧情和音效。可以去看看一些带过场剧情的事件(尤其是“❈ >> BEGIN”地图里的 INIT 事件),了解它们是如何运作的。

缩写含义:

`BGM` - 背景音乐(电子游戏原声带)\[循环播放\]

`BGS` - 环境音(比如环境噪声)\[循环播放\]

`SE` - 音效(比如开门声)\[不循环\]

`ME` - 音乐效果(当某个 `ME` 播放时,除该 `ME` 外的所有声音都会暂停)\[不循环\]

![](/img/omori-guide/img_0000_04f9e5bece.webp)

*(来源:FruitDragon)*

现在来到第三页,也是最后一页。我只讲 `Advanced`(高级)部分,因为其余的都相当一目了然。

![](/img/omori-guide/img_0000_2fa21e8d19.webp)

![](/img/omori-guide/img_0000_2c58e9aeef.webp)

不过,这些内容比其余的深入得多,所以我会逐个讲解。

### 插件命令 <span class="og-g">OMORI</span> 有非常多的插件。你只要打开位于 `Database`(数据库)旁边的 `Plugin Manager`(插件管理器),就能看到这一点。`Plugin Command`(插件命令)做的事情,就是取出一条发给某个插件的命令并执行它。

用得最多的恐怕要数 `ShowMessage` 插件命令了,它用来运行……对话。

我们兜兜转转,又回到了原点。

#### 对话

我们已经讲过如何在 `.yaml` 文件里编写对话。现在,该讲讲怎么在游戏中实际运行这些对话了。

*(来源:FruitDragon)*

点击 `Plugin Command`(插件命令),我们就会看到上面的窗口。你只需要输入下面的文本:

*(来源:FruitDragon)*

把 <var>file_name</var> 替换成你想从中读取消息的文件名(例如 <var>00_template</var>),把 <var>XX</var> 替换成消息的编号。

就这么简单!当你在游戏中触发这个事件时,对话就会显示出来。

##### 对话选项

你可能已经知道——不,你应该知道——<span class="og-g">OMORI</span> 里有很多需要玩家在对话中做出选择的场合,而选择通常会决定接下来会说什么。嗯,这些同样是用 `Plugin`

`Commands`(插件命令)实现的。这次要用到两个。

第一个命令是 `AddChoice`。它会把你的对话添加进去,供稍后调用。要使用它,请输入以下文本。

```text
“AddChoice file_name.message_XXlabel”
```

中间那段和普通对话一样,只不过现在,它决定的是这个选项会显示成哪条消息。然后是 <var>label</var>(标签)。如果你还记得前面的内容:`labels` 是 <span class="og-g">RPG Maker MV</span> 事件中的标记,可以跳转到它们那里,用来跳过或循环代码。在这个语境下,每个对话选项基本上就相当于一条跳转到指定 <var>label</var> 的 `Jump To Label`(跳转到标签)命令——你只要把 <var>label</var> 这个词换成你输入的标签名即可。现在,把你所有的对话选项都照此办理一遍就完事了。

接下来,我们需要真正把选项显示出来。这要用到 `ShowChoices` 命令。只需添加这条命令,后面再跟上当玩家点击“X”或“取消”时默认选中的选项编号。

*注:编号从 <var>0</var> 开始数,所以如果你想让玩家点击取消时执行的是第二个选项,实际上要填的是<var>1</var>。是有点怪,但计算机就是这么回事。如果你不想让玩家能按取消跳过对话选项框,可以改填 <var>-1</var>。*

现在,你已经完全掌握对话的用法了。恭喜!

#### 摄像机控制 `Plugin Commands`(插件命令)的另一个常见用途是控制摄像机。这要通过四条基本上一目了然的命令来完成。

*注:速度的运作方式有点反直觉:数字越大,速度反而越慢,反之亦然。默认值是 800,如果你在命令中省略 Speed,就会使用这个值。*

`CAM PLAYER`<var>SPEED</var>:以指定的速度跟随玩家。

`CAM EVENT`<var>IDSPEED</var>:以指定的速度跟随指定的事件。

`CAM DISABLE`:重置摄像机,让它以默认速度跟随玩家。

#### 天气

虽然 <span class="og-g">RPG Maker MV</span> 本体自带天气效果命令,但 <span class="og-g">OMORI</span> 用的是一个深入得多的插件来控制天气。该插件由三条用于改变天气的插件命令组成,并使用六种天气类型,分别是 `rain, storm`(雨、暴雨)、`snow`(雪)、`embers`(余烬)、`shine`(辉光),以及 `leaves`(落叶)。

```text
AriesSetWeatherImage weather filename 
```

它决定游戏为指定天气类型使用哪张图像,图像从 `img/pictures` 文件夹中调取。<span class="og-g">OMORI</span> 虽然只用到 `rain`(雨)、`storm`(暴雨)和 `snow`(雪),但另外三种类型的图像它也自带了,你可以直接拿来用。当然,你也可以用自己的图像。

```text
AriesToggleStormThunder boolean 
```

这是一个真/假值,决定 `storm`(暴雨)天气类型是否会周期性地闪现雷光。

```text
AriesWeatherweather power duration 
```

这条才是真正设置天气的命令。<var>Power</var>(强度)是一个 <var>1</var>-<var>9</var> 的数字,决定天气的猛烈程度。<var>Duration</var>(时长)是天气淡入所需的帧数。

### 脚本 `Scripts`(脚本)威力强大。它们能让你做到原版 <span class="og-g">RPG Maker MV</span> 做不到的事情。当然,理论上你得懂 <span class="og-g">Javascript</span>……但这也正是为什么查看现成事件如此重要:只要适用,你完全可以琢磨明白它们的脚本,然后照搬过来。这能帮你省不少力气,而且你并不需要真的会 <span class="og-g">Javascript</span>——你只需要知道怎么搞清楚一段代码是干什么的。

游戏中很多地方都会用 `Scripts`(脚本)来设置变量,比如传送用的变量。`Scripts` 还能用来设置其他事件的 `Self Switches`(独立开关)。而这些仅仅是个开头。就像我说的,这东西是真的强大。

*(来源:FruitDragon)*

这是游戏中常见的一个 `Script`(脚本)示例。这个脚本用来设置地图之间传送所用的变量。

*注:<span class="og-g">RPG Maker MV</span> 的 `Script`(脚本)命令内置了 12 行的上限。由于 Omocat 与 <span class="og-g">RPG Maker MV</span> 的开发者 Archeia 有合作,她拿到了一个能绕过此限制的定制版本。所以,如果你看到一条 13 行以上的 `Script` 命令,千万别去编辑它,否则它会被拦腰截断、直接报废。不过话虽如此,你还是可以用最近发布的 <span class="og-g">RPG Maker MV</span> 模组来绕过这个限制,*

*也就是 [OneMaker MV](/omori/modding-guide/10-plugins/)。*

其他常用脚本还包括图片过场剧情脚本、更精细的跟随者控制脚本,以及设置变量和开关的脚本。想查看几乎涵盖所有可用脚本的完整列表,请访问[这份官方](https://docs.google.com/spreadsheets/d/1-Oa0cRGpjC8L5JO8vdMwOaYMKO75dtfKDOetnvh7OHs/edit?gid=1186334695#gid=1186334695)[表格](https://docs.google.com/spreadsheets/d/1-Oa0cRGpjC8L5JO8vdMwOaYMKO75dtfKDOetnvh7OHs/edit?gid=1186334695#gid=1186334695)。

![](/img/omori-guide/img_0000_31b568f7a0.webp)

#### 动画事件

精灵动画是个相当大的话题,所以我在这里只讲基础。

通常的做法是:把精灵设置到精灵表(spritesheet)的某个区域,然后来回、左右翻转精灵,让想要的画面显示出来;或者用 `Script`(脚本)命令手动设置它们。想了解各个朝向对应哪些图像,直接参考游戏中几乎每个 NPC 都有的行走动画就行。

下面是一个开门时会用到的脚本示例:

*(来源:FruitDragon)*

*(来源:!objects\_fa\_doors.png,原版游戏)*

这就是那张精灵表的样子,你可以借此看清它的原理。

对于更复杂的动画,你可以使用这个脚本:

```text
script: this.setCustomFrameXY(x,y) 
```

*注:这里的“`this`”指的是运行这段代码的那个事件。如果你想设置另一个事件的动画,就必须把它替换成对应的脚本调用,也就是 `$gameMap.event(`<var>eventId</var>`)`。不过,如果要把这段脚本放进那个事件的移动路径里,则要改回使用 `this`。*

这个脚本会把事件设置到其精灵表中的某个精确帧上。游戏中大多数复杂动画都靠它实现。要取消这些自定义帧,请使用 `this.setCustomFrameXY(`<var>null</var>`,`<var>null</var>`)`。一个值得参考的好例子是拥抱动画。

一般来说,先在游戏的其他地方找找你想做的动画的示例是个好主意,这样你心里就有数了:该怎么让你想动起来的东西动起来。

#### 商店

商店是种有点奇葩的小东西,因为它们其实出场机会并不多。

尽管如此,我还是来讲讲怎么搭建它们。

首先,假设你要做一家带全新对话的商店,那你就得把这些对话全部写出来。这些对话必须放进 `System.yaml`。最省事的做法,就是复制粘贴一个现成的店主,然后改掉他们的名字和对话。

*注:你会注意到,遥远镇的大多数店主都会调用其他的 yaml 文件。这是硬性要求。*

现在,我们来真正制作商店。第一步,创建你的新事件,加上任何你想要的开场对话或其他内容。然后,到了买/卖环节时,做一个包含 `Buying`(购买)、`Selling`(出售)和 `Cancel`(取消)的对话选项。具体做法可以参考前面的章节。

现在,在 `Buying`(购买)部分,我们要使用一条 `Script Command`(脚本命令),即“`this.setupShop('`<var>name</var>`',`<var>0</var>`)`”。它的作用是告诉游戏该显示哪套对话,这是通过 `‘`<var>name</var>`’` 来实现的——它应该是你在 `System.yaml` 文件里给店主起的名字。然后那个 <var>0</var> 告诉游戏这是在购买。接下来,只需使用 `Shop Processing`

`Command`(命令),用它添加你的所有道具并设定价格。切记不要勾选“`Purchase Only`”(仅购买)那个框,它在 <span class="og-g">OMORI</span> 里根本不管用。

然后是 `Selling`(出售),我们要把上面那套原样再做一遍,只改一个地方:把 <var>0</var> 换成 <var>1</var>,告诉游戏我们这次是在卖东西而不是买东西。顺便一提,`Shop Processing`(商店处理)你还是得留着——哪怕它在出售时什么都不做——因为正是它让游戏真正调出商店菜单。

最后是 `Cancel`(取消),直接结束事件就行。没什么好多说的。

另外,如果你想给店主加一张立绘,你就得为此折腾插件,或者使用 [TR_PictureShops](https://github.com/modsone/omori-modding-resources/blob/main/Data%20Organization%20Plugins/TR_PictureShops.js)。不过说实话,这没那么重要,毕竟 <span class="og-g">OMORI</span> 里只有邮箱(Mailbox)有立绘。

#### 动画图片

在 <span class="og-g">OMORI</span> 中,`pictures`(图片)在各种过场剧情里随时都在被做成动画,比如白色空间的开场。游戏还会把多张图片合进同一张图集里,却又能做到只使用其中的一帧。那么,它是怎么做到的呢?

答案是:它使用了 `scripts`(脚本)。

我们要做的第一件事,是创建想要做成动画的图片。直接使用 `Show Picture`(显示图片)命令,而且暂时最好把 `opacity`(不透明度)设为 <var>0</var>。另外,务必记住你使用的 `ID`(编号):`IDs` 越大的图片永远显示在越上层,而 `ID` 为 <var>1</var> 的图片则显示在角色之下。

现在,我们可以开始写脚本了。

首先,我们需要向游戏说明每一帧之间的分隔是怎样的,所以要用这个脚本:

```text
this.setupPictureCustomFrames(id, width, height, hframes, vframes); 
```

现在,让我们逐个看看它们分别是什么。

<var>id</var> 就是你要应用这些帧的那张图片的 ID。

<var>width</var> 和 <var>height</var> 是整张图像的像素宽度和高度,注意是整张,而不是单独一帧的。

<var>hframes</var> 和 <var>vframes</var> 是图像中水平方向和垂直方向的帧数。

接下来添加什么内容,取决于我们要做什么。

如果你只是想设置图像的单独一帧,比如一张光照叠加层,就用这个;

```text
this.setPictureFrameIndex(id, frameId); 
```

同样,<var>id</var> 是图片 ID,而 <var>frameId</var> 是帧的 ID。帧 ID 按从左到右、从上到下的顺序排列,从 <var>0</var> 开始。也就是说,左上角是 <var>0</var>,它右边的是 <var>1</var>,依此类推。

但如果你要设置的是一段动画,就改用这个;

```text
this.setPictureAnimation(id, frames, delay, loops, wait); 
```

好,现在我们再来拆解一遍。

首先是 <var>id</var>,和往常一样,是图片 ID。

接下来是 <var>frames</var>。它是一个 `Array`(数组),由你希望动画依次播放的那些 `frameIds`(帧 ID)组成。给不清楚的人解释一下:<span class="og-g">JavaScript</span> 中的数组,就是以变量形式存储的一列值。它们长这样:

`[`<var>value</var>`,`<var>value</var>`,`<var>value</var>`,`<var>value</var>`]` 所以,如果你想让帧从 <var>0-6</var> 依次播放,那么你的 <var>frames</var> 就应该长成 <var>[0,1,2,3,4,5,6]</var> 这样。

<var>delay</var> 是从一帧切换到下一帧所花的帧数(这里的“帧”以你显示器的 fps 计)。

<var>loops</var> 决定动画在完成之前要播放多少遍;如果你想把它设为 <var>infinity</var>(无限),就输入 <var>Infinity</var>。

最后,<var>wait</var> 是一个 <var>true</var> 或 <var>false</var> 值(也叫 `boolean`(布尔值)),决定游戏是否要等动画播放完毕。

现在,配合 `Move Picture`(移动图片)命令,你就可以让你那正在播放动画的图片淡入显示了。而等你处理完**所有**自定义帧图片之后,一定要

记得加上一条 `this.removePictureCustomFrames();`

#### 雾效 [🕊️](https://mods.one/author/FoG)

雾效是我很少见到有模组使用的功能。原版游戏的一些区域会用雾效来营造雾气氤氲的氛围,比如北湖。

从技术角度看,雾效其实就是一张平铺的(“平铺”指边缘无缝衔接,不是指 <span class="og-g">Tiled</span> 那个软件)图像在整个地图上循环滚动。这意味着除了做雾,你其实还能用它实现很多酷炫的效果——至于怎么玩出创意,就留给你自己去琢磨了。我只负责拆解这个脚本。

```text
let fog = this.generateMapFog() 
fog.move.x = x_scroll 
fog.move.y = y_scroll 
fog.name = ‘name’ 
fog.opacity = opacity 
fog.blendMode = blendmode 
this.createMapFog(‘fog1’, fog); 
```

现在,我们来拆解这个脚本里的每一项。

`move.x` 与 `move.y` 决定雾效的滚动速度,等同于视差滚动的速度。

`name` 是雾效图像的文件名,取自 `img/overlays`。

`opacity`(不透明度)的取值范围是 <var>0</var>-<var>255</var>,嗯,就是图像的不透明度。

`blendmode` 是一个决定图像混合模式的值。它是一个数字,对应 <span class="og-g">RPG</span>

<span class="og-g">Maker MV</span> 中的 4 种混合模式,分别是 <var>0</var>(`Normal`(正常))、<var>1</var>(`Additive`(加法))、<var>2</var>(`Multiply`(正片叠底))、<var>3</var>(`Screen`(滤色))。

最后有一条重要提示:如果要在循环地图中使用雾效,雾效图像的尺寸就必须是地图图像尺寸的因数或倍数——举个例子,对于一张 1024\*1024 的地图,雾效图像的尺寸就必须是 1024 的因数/倍数。否则,当到达地图的循环点时,雾就会开始“瞬移”。

![](/img/omori-guide/img_0000_f716eacb41.webp)

### 事件示例

![](/img/omori-guide/img_0000_6e1bfb08fa.webp)

*(来源:parallels,由 FruitDragon 提供)*

传送脚本!

如你所见,门通过 `Movement Route`(移动路径)实现了动画;随后,`Game Variables`(游戏变量)通过一条 `Script`(脚本)完成设置。

最后,调用 `Common Event`(公共事件)<var>Teleporting Style</var>,播放音效,再执行关门的移动路径。接着调用 `Common` `Event`(公共事件)<var>Fade-In Screen</var>,让新地图以一种淡入的效果出现在眼前。

不过,除了正门之外,还有其他类型的 `Teleport Scripts`(传送脚本),所以多去看看它们总是有好处的!

![](/img/omori-guide/img_0000_d69a4f90e8.webp)

*(来源:parallels,由 FruitDragon 提供)*

门的过场剧情!

如你所见,这里加了一段动画来表现门被打开。

音频部分使用了音效。在第一段可见的脚本中, `$gameMap.event(`<var>6</var>`).setPosition(`<var>x</var>`,`<var>y</var>`);` 把 `Event 6`(事件 6)的位置改到了 <var>46</var>、<var>10</var>。随后,在同一脚本的第二部分里(虽然有一部分被截掉了),该事件的 `Self Switch`(独立开关)被设为 True,在这里的效果就是让该事件的精灵显示出来。
