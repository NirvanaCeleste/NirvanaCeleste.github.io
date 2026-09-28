---
title: "05 · 精灵图与美术"
date: 2026-09-28
weight: 5
draft: false
comments: true
showTableOfContents: true
description: "OMORI 模组制作指南中文翻译 · 精灵图与美术 — 全部图像资源规格"
---

![](/img/omori-guide/img_0000_fce5ead23d.webp)

![](/img/omori-guide/img_0000_5d9fd91eb2.webp)

*(来源:FruitDragon)*

现在,这篇关于 <span class="og-g">Tiled</span>与图块地图制作的深度指南就到此结束了!希望它对你有帮助!

*(另外,没错,我在地图制作教程里用作示例的那张地图,正是[The Dreamer](https://mods.one/mod/thedreamer)里的 Vast Forest Maze(广袤森林迷宫)地图。那可是我 FruitDragon 亲手为那个 Mod 做的!)*

接下来进入下一部分:

我听到你们有些人在想了:“FruitDragon,事件和 `tilemaps`是挺不错的,可我不想让它们长成那副样子。要是我的 Mod 舞台设在被战火撕碎的 `Black Mesa Research Facility`废墟里呢?这要怎么做?”呃,首先,我不是 FruitDragon,从这一节开始主要由 TomatoRadio 给你带路。其次,我不会画画,所以那部分只能靠你自己了。不过,我可以告诉你这些美术资源该怎么设定格式。

![](/img/omori-guide/img_0000_311996e2f3.webp)

本节将详细介绍 <span class="og-g">OMORI</span> 中每一种图像类型的格式,让你知道如何按自己的用途去制作它们。

*注:所有这些图像都位于 `img`文件夹中,该文件夹下有众多子文件夹,我就是按它们来分类的。子文件夹确实重要,它们决定了一张图像的用途。*

### 大地图精灵图 <span class="og-g">OMORI</span>中的大多数大地图精灵图都以 `spritesheets` 的形式存放在“`characters`”文件夹里。更确切地说,这些是 `Events`可被设置为使用的图像。在给你展示它们的所有设置方式之前,我先讲讲它们在最基础的层面上是如何运作的。

这是你在 <span class="og-g">OMORI</span> 里能拥有的最基础的 `spritesheet`。它由 8 组 3×4 的精灵组成,每组内的精灵尺寸完全一致。不同 `spritesheets` 之间精灵的尺寸可以不同,只要遵循这个格式就行。我会把这 8 组中的每一组称为一个“`section`”(区块)。每个 `sections`在上下左右四个基本方向上各有 3 帧移动精灵,如下图所示。除了把它们排列整齐之外,你不需要做任何额外的事,动画就能正常工作。

![](/img/omori-guide/img_0000_a930e296a7.webp)

![](/img/omori-guide/img_0000_2e37a9806c.webp)

*(来源:DW\_NPC\_10.png,原版游戏)*

看吧。如你所见,太空男孩队长的 `spritesheet` 虽然尺寸相同,却有几个“`sections`”完全不按这个结构来。许多 `spritesheets`还会把角色动画存进同一张图里,它们是在事件代码中通过 `scripts`调用的。

*(来源:DW\_SBF.png,原版游戏)*

好了。这其实只是这类图集 5 种设置方式中的一种。而格式靠什么区分?靠文件名。<span class="og-g">RPG Maker MV</span>(或插件)会检查所有已加载精灵图的文件名,来决定如何切分它们。我现在就给你看看它们长什么样。

如果在文件名开头加上 <var>$</var>,它就会变成一张专为单个`character/section`设计的 3×4 图集。这最适合带动画的角色,或尺寸特殊的物体。

![](/img/omori-guide/img_0000_7944acf698.webp)

![](/img/omori-guide/img_0000_293d9e6bd4.webp)

*(来源:$glassomori.png,原版游戏)*

*(来源:$BS\_Raft.png,原版游戏)*

如果在文件名开头加上 <var>[SF]</var>,它就会变成一张专为单个 `character/section`设计的单帧图像。这最适合不带动画的角色,或尺寸特殊的物体。

*注意:在事件编辑器中,它会被显示成按 12×8 切分。别担心,游戏里它会显示为单个精灵。*

![](/img/omori-guide/img_0000_a18643616d.webp)

![](/img/omori-guide/img_0000_d2788a6524.webp)

*(来源:\[SF\]Blanket\_Fort\_Empty.png,原版游戏)*

*(来源:\[SF\]FA\_basil\_TV.png,原版游戏)*

如果在文件名末尾加上 `%(`<var>x</var>`)`,行走精灵的数量就会增加 <var>x</var> 所代表的数字。大地图的“某物”和跑步精灵用的就是这个。另外,由于 OMORI 用于此功能的插件比 <span class="og-g">OMORI</span>所用的 <span class="og-g">RPG Maker</span> <span class="og-g">MV</span> 版本更旧,这个插件有点小 bug,只对 <var>$</var> 图像有效。如果你需要/想要用更大的图集,可以用[这个 Galv 插件](https://galvs-scripts.com/2015/12/12/mv-character-frames/),效果几乎一样。**(这是 OMORI 专属功能。如果你在** **原版 RPGMaker MV 里尝试这个功能,它是不会生效的。)**

*注意:在事件编辑器中,它会被显示成按 12×8 或 3×4 切分。别担心,游戏里它会正确显示。*

![](/img/omori-guide/img_0000_8995c21235.webp)

![](/img/omori-guide/img_0000_df437f52e8.webp)

*(来源:$DW\_BASIL\_RUN%(8).png,原版游戏)*

*(来源:$bs\_en\_nanci%(7).png,原版游戏)*

在 <span class="og-g">RPG Maker MV</span> 中,角色会自动相对于地图向上偏移 6 像素,以营造纵深感。不过,如果你想对某些精灵(比如门)关闭这个效果,可以在文件名开头加上 <var>!</var>。

![](/img/omori-guide/img_0000_f52f2a2d87.webp)

*(来源:!FA\_PLAYERHOUSE\_OBJ.png,原版游戏)*

*(来源:!objects\_fa\_doors\_sunset\_2.png,原版游戏)*

### 对话立绘

这部分在[YAML/对话](/omori/modding-guide/02-yaml/)一节里已经简单提过,不过为了内容完整,不妨再稍微深入一点。

所有对话立绘都存放在“`faces`”文件夹里。它们遵循一套非常固定的格式,不容偏离。

每张图像(也就是 png 文件)是一个“`faceset`”(脸图集),每行包含 4 张 106×106 像素的脸图,而行数几乎想加多少加多少。说真的,你可以把游戏里每一个 `faceset`都合并进一张图,照样运行得好好的。

`faceset`中的每张脸图都有一个编号,也就是它的“`faceindex`”(脸图索引)。编号从 <var>0</var>开始,从左到右、从上到下依次排列,对话文件里就是这样选中它们的。如果你记不清每张脸对应的编号,一个好办法是在每个格子的角落用纯黑(#000000 十六进制色号)写上编号。因为是黑色,它们在游戏内文本框上是看不见的。(这个方法对自定义窗口皮肤/文本框无效,比如 [OMORI IS MISSING](https://mods.one/mod/omoriismissing)或[HIKITO](https://mods.one/mod/hikito)这类 Mod 里展示的那种。)

![](/img/omori-guide/img_0000_32b777b9ef.webp)

*注:关于原版文本框还有一点要记住:它的边框会裁掉所有对话立绘外圈的 4 像素。*

*(来源:TomatoRadio)*

给 `faceset` 编号的一个示例。背景是为了看得清楚而加的,实际的 `faceset` 里不应出现。

![](/img/omori-guide/img_0000_b64b7aa3bd.webp)

*(来源:MainCharacter\_Mari.png,原版游戏)*

玛丽的 `Faceset`。这里还能看到一堆用于黑色空间和回忆片段的其他精灵。把你的 `facesets`合并成包含多个角色是个好主意,尤其是当你没打算添加新表情的时候。这能减少你要记的文件名数量、避免索引重叠,还能压缩文件体积。

事实上,脸图集的尺寸几乎没有上限——像这么大的图像在游戏里依然运行得完全正常。给你个参考:这里面有 400 张脸。

*(来源:big.png,TomatoRadio 心爱的作品)*

### 队伍战斗立绘 `Battle portraits` 的运作方式与 `dialogue portraits` 非常相似,也存放在同一个文件夹里。每张立绘同样是 106×106 像素;不过,游戏 UI 实际会盖住外侧的 6 像素,留给你发挥的只有 100×100 的区域。

但与 `dialogue portraits` 不同的是,`battle portraits` 按每行三张排列,每一行是某个特定情绪所用的动画帧,会从左到右循环播放。

每一行对应哪个情绪是编码在 `states` 里的,所以你要做新图集的话,必须遵循这个格式。

```text
0. Neutral
1. Happy
2. Ecstatic
```

<var>3</var>`. Afraid`(也用于“OMORI did not succumb”状态)

```text
4. Sad
5. Depressed
6. Angry
7. Enraged
8. Toast/Blacked Out
9. Hurt
10. Victory
11. Manic
12. Miserable
13. Furious
```

<var>14</var>`. Stressed Out` (仅桑尼使用)

如果你想要更多情绪,就必须把图集往下扩展,添加更多行。

这是梦世界(DW)胜利表情所用的彩带纸屑,欢迎自行下载取用。

![](/img/omori-guide/img_0000_bf6882360e.webp)

*(来源:[这个谷歌文档](https://docs.google.com/document/d/1LyoDxBbtw4MUb7HirIZEaigpbJOcbwTelby7vttIAlg/edit#heading=h.dckld2q0kapk),图像作者不明)*

*(来源:01\_OMORI\_BATTLE.png,原版游戏)*

在上面的示例中,最下面那行三阶情绪 OMORI 并不使用,但如果要用崩溃(Stressed Out)精灵,位置就在那一行。

*(来源:03\_KEL\_BATTLE.png,原版游戏)*

由于只有 OMORI 和梦世界贝西尔(主机版独占)能达到三阶情绪,大多数图集到这儿就结束了。

### 敌人战斗立绘

敌人战斗立绘存放在两个地方。敌人的一张中性单帧存放在“`enemies`”文件夹,而完整图集存放在“`sv_actors`”文件夹。

`sv_actors`文件夹里的完整图集与队伍战斗立绘的运作方式类似。每行包含 4 个精灵;不过,第 2 帧和第 4 帧是相同的,这样动画看起来就是“1、2、3、2、1”而不是“1、2、3、1”。这种做法还有别的名字,比如回旋(boomeranging)、橡皮筋(rubberbanding)等等。

*注:动画的帧数只是惯例,你完全可以为特定敌人用更多帧。比如,在与 OMORI 的最终战里,他就只用了 3 帧。*

与队伍成员不同,每种情绪调用哪些精灵是由每个敌人各自的程序手动指定的,所以你可以按喜欢的任意顺序往图集上摆。不过按照惯例,它们通常是这么排的:

```text
0. Neutral
1. Hurt
2. Defeat
3. Sad
4. Angry
5. Happy
```

![](/img/omori-guide/img_0000_38eefd1838.webp)

![](/img/omori-guide/img_0000_24fa639a0a.webp)

![](/img/omori-guide/img_0000_1ae5202cb8.webp)

*(来源:!battle\_sprout\_mole.png,原版游戏)*

上面就是 `sv_actors`文件夹里大多数敌人精灵图的排版样式。

*(来源:!battle\_humphrey\_face.png,原版游戏)*

这是它们在 `enemies`文件夹里的样子,就是中性精灵的单独一帧。

注意,这仅供 <span class="og-g">RPG Maker MV</span>`Database` 使用,游戏内是看不到的,所以如果你的敌人设计只是小改(同时保持原本尺寸),就不需要更新它。贝西尔和陌生人的 `enemies`图像里用的还是旧设计,你完全可以亲眼验证这一点。

另外,没错,汉弗莱的第三阶段在文件里就只是一张脸。不难猜,但还是很好笑。

*(来源:!battle\_basil\_something.png,原版游戏)*

大多数与“某物(Something)”相关的敌人感受不到情绪,因此那些精灵没有被包含进来。这是贝西尔的图集,只包含中性和受击精灵,外加一个未使用的倒地精灵。

![](/img/omori-guide/img_0000_605d1940cb.webp)

*(来源:!battle\_biscuit\_doughie.png,原版游戏)*

额外的情绪,比如三阶情绪,通常就像上面这样被塞在最底下。

### 战斗动画 <span class="og-g">OMORI</span>中的大多数攻击都把全部帧存放在“`animations`”文件夹里,并在“`Animations`”标签页中进行动画编辑,该标签页位于 <span class="og-g">RPG Maker</span>

```text
MVDatabase.
```

`Animations`以图集形式存放,每个“`Pattern`”(图案帧,即一个动画帧)分到 192×192 像素。每行最多横向排 5 个 `Patterns`,但和 `Portraits` 一样,行数没有上限。在 <span class="og-g">OMORI</span> 里,一帧动画常常要用到多个图案帧,因此做动画时必须把它们对齐。

![](/img/omori-guide/img_0000_fa6d653400.webp)

*(来源:e\_protect\_the\_earth.png,原版游戏)*

*(来源:TomatoRadio)*

这就是上面那张图在实际 `Animations`标签页里的样子。从那些灰色方块你就能看出,图像被拆成了多个部分。

### 战斗背景

战斗背景,或者按大家的常用叫法 `Battlebacks`,做起来真的又轻松又好玩。它们存放在“`battlebacks1`”文件夹里。

严格来说,你可以把任何 640×480 的图像放进这个文件夹,它就能当 `battleback` 用;不过 <span class="og-g">OMORI</span>的战斗背景有一套非常独特的风格。具体来说,<span class="og-g">OMORI</span>的 **战斗背景用的是经过抖色(dithering)处理的图库照片**,对应它的

```text
battlebacks.
```

<span class="og-g">OMORI</span>的照片来自 [Pexels](https://www.pexels.com)和 [Pixabay](https://pixabay.com),我也推荐这两家,照片全部免费且无水印。拿到照片后,你得把它裁剪和/或缩放到 640×480,然后过一遍抖色工具。<span class="og-g">Photoshop</span>的效果最精确,[Ditherit](http://ditherit.com) 的效果也不错。

![](/img/omori-guide/img_0000_83e390eef4.webp)

那抖色(dithering)到底是什么?简单说,就是用交替排列的像素来模拟更多色调,从而缩减图像的调色板。这让图像在保留层次感的同时,文件体积变得很小。而且它给图像带来的那种非常独特的效果,坦白讲,就是莫名地挺酷。

示例:

*原图([摄影](https://www.pexels.com/photo/water-fountain-beside-green-leaf-trees-242258/):Mike Bird)*

![](/img/omori-guide/img_0000_1144abc851.webp)

*裁剪至 640×480*

![](/img/omori-guide/img_0000_6dfb22d3e3.webp)

*用 [Ditherit](https://ditherit.com/)做的抖色处理*

请特别留意图像两侧灌木丛的质感。如你所见,颜色从数百种深浅不同的绿色缩减到只剩五六种,但灌木依然保留了它的质感。

很神奇,对吧?

另外还有个很少有人提的功能:借助插件命令,你可以在一场战斗中同时使用多张战斗背景图像,还包括可滚动的战斗背景。OMORI 之战就是这么实现的,[Autumn Break](https://mods.one/mod/autumnbreak)的最终战也一样。所以放心大胆地去做些好看的景色吧!

### 图块集 `Tilesets`收录了 <span class="og-g">OMORI's</span>地图用到的所有图块和道具。它们是以图集形式存放在“`tilesets`”文件夹里的。

<span class="og-g">OMORI's</span>大多数 `tilesets`都是 1024×1024,这是可用的最大尺寸。每个单独图块为 32×32,一些较大的道具(如树木和建筑)会占用多个图块。图块可以通过图集上其他图块的循环动画动起来,详见

*[地图制作章节](/omori/modding-guide/04-maps/)。*

![](/img/omori-guide/img_0000_c02887b5ef.webp)

*(来源:DW\_SnowForest.png,原版游戏)*

`Snowglobe Mountain's Tileset`,也就是雪球山的图块集。注意水的全部三帧都在这里,它们就是用来做动画图块的。

另外注意,`Church of Something's`(某物教堂)的那座山也在这儿。你的 `tileset`不必局限于单个地区,而且把较小的 `tilesets`合并起来通常更好,能节省文件空间,尤其是当它们装着类型相近的素材时。这样你的工作区更清爽,你和你玩家的电脑也省下更多存储和处理开销。

```text
.
.
.
.
.
.
```

图块集!!!我知道你才刚看完怎么制作它们,但是!!我特意花了点时间给你收集整理了一套基础底板。我知道,多贴心呀!!!当然,你也可以直接去改原版的东西,但它们的排版太烂了!真的烂,我的天哪。烂透了。

![](/img/omori-guide/img_0000_d062bd854d.webp)

*(来源:DW\_SlimegirlLairTiles.png,原版游戏)*

看看这有多烂!!!整个乱成一锅粥,烂死了!!!不不不,让我来给你解释解释这玩意为什么这么烂。桥是一团糟,感觉就是哪儿塞得下就往哪儿塞。瀑布离真正的水隔了整整一个学区远。与此同时,蓝色水崖一个人跑到缅因州吊着,它的兄弟姐妹们还在亚利桑那州的家里琢磨它到底是怎么跑过去的。

现在让我给你看点好得多的东西!

![](/img/omori-guide/img_0000_5310d6f42d.webp)

![](/img/omori-guide/img_0000_30ddb079c9.webp)

![](/img/omori-guide/img_0000_ad746a444d.webp)

*(来源:我本人!!!外加一些原版素材……哦对,还有我妹的……)*

这!!!就是图块基础底板!!!

“等等等等,我听见你尖叫了!!!这是什么????为什么所有东西都这么亮??”听我解释。

![](/img/omori-guide/img_0000_5310d6f42d.webp)

咱们先从标准底板开始。

如果你不需要任何现成的物件,就拿这个当标准用!这上面的东西你后面都用得上。首先,讲颜色。

![](/img/omori-guide/img_0000_aafcf368a8.webp)

*(来源:又是我本人!!!!,不过 TOMATO 把它“修”了一下,改成了写 cliff……)*

红色是你放草的地方。在这些图里,我已经把多余的草切掉了,所以务必把你的边缘草延伸出来,盖到红色部分上面、一直压到蓝色上,像这样;

![](/img/omori-guide/img_0000_16c6ac9d30.webp)

*(来源:Aseprite)*

OMORI 大多数地方用的都是同一种草,不过你当然可以不这么干。深蓝色是你的悬崖(CLIFFS)。它们底部通常带点轻微的阴影和裂纹,但具体得看地区。

![](/img/omori-guide/img_0000_14a20a7e2e.webp)

*(来源:对 HS\_PIREFLAIFORIST.png 的修改版,原版?)*

绿色是你的水。要做动画水的话,你得在 <span class="og-g">tiled</span> 里手动添加帧。我有 90% 的把握已经有人在 <span class="og-g">tiled</span> 那部分讲过这个了,总之帧是按这个顺序排的 && 帧延迟大约是 200 毫秒。我也说不好,反正你见了就懂。

*(来源:从我那垃圾宫殿里掏出来的绿色垃圾)*

黄色是你的楼梯!这部分我保持简单(树不算,那个我后面会讲,先等等)。左边那个和更靠中间的那个是不、一、样、的。右下那个边缘笔直,更适合偏人造的场合(或者不管你创造的世界上是哪路怪东西当了智慧物种),而右上那个边缘更粗糙,是给我们这些憨憨和低智慧生物用的。

剩下的那些则是给更大的楼梯用的,就是那种大块头级别的货色!

![](/img/omori-guide/img_0000_3d21fd6ee3.webp)

青色是你的小路,以及散落在周围的那些零碎杂物。随手撒一点,效果好得很。另外,就像说红色时那样,草可以而且将会盖到青色上面。原版游戏把草往里压,最深也就到这个程度。

现在,剩下其他东西基本都不用解释了。草、树、石头,你懂的。只要留意一点:换色的树你可能用不上,但我强烈推荐。哪怕只是很小的改动,也能给地图增色不少。

![](/img/omori-guide/img_0000_4840162c3f.webp)

*(来源:map159.png,原版游戏,由某个 rph 工具编译而成[名字我忘了哈哈哈](https://github.com/rphsoftware/omori-map-preview-renderer/actions/runs/20416117980))*

“那么,到处散落的这些黑色玩意是干嘛的?”那些是你的连接件。把它们想成拼图块上的卡口。务必时刻让它们对齐。你可以随便用哪种取色器(或者吸管工具)选中它们来检查。我个人会把它们剪切出来放到另一个图层上,这样随时都能查看

![](/img/omori-guide/img_0000_8ea6fbd13c.webp)

*(来源:我觉得它们就像那种自闭症小孩会特别喜欢的小塑料连接件*

*叫 K'NEK!!!人家叫 K'NEK!!!)*

这是一张 TOMATO 做的可爱测试地图,用来展示这一切是怎么运作的

![](/img/omori-guide/img_0000_891668c487.webp)

*(来源:啊啊啊啊好烫好烫啊啊啊啊啊啊啊啊.png)*

接下来是室外和室内底板。

同样的东西,但这次加了偷来的货!这里有大量可拿去修改的原版素材,全部按类型码得整整齐齐。

![](/img/omori-guide/img_0000_1b3e98c318.webp)

*(来源:这玩意是我瞎 \*@(# 编的)*

![](/img/omori-guide/img_0000_dccf27469a.webp)

*(来源:我又瞎 @#@% 编了一个)*

有些原版图块对齐得很怪,但它们是有用意的。很多时候,它们是要摆到柜台上,或者要跟另一个物件对齐。如果有哪个东西看着不对劲,试着把它挪动几个像素。

好了,你肯定早就注意到我和 PINKER 了。我纯粹是来凑数填空的!顺便一提,如果你打算用这些底板,劳驾别把我删掉!我\sinv\[1\]超——爱——\sinv\[0\]别人给我的作品署名!!!好啦

PINKER 确实是有用处的。她被向上偏移了六个像素。在 RPG Maker MV 中,所有事件(名字里带“!”的除外)都会被向上顶起六(6)

![](/img/omori-guide/img_0000_2fdeca95fa.webp)

像素(相对于图块地图而言)。这是出于纵深感的考虑,但这意味着画地图时你可能得靠猜玩家看起来会是什么样,不过 PINKER 看起来什么样你可是清清楚楚!!!她就是那个得了“虱子病”的,所以我只能把她关进生化危害隔离箱,不过我觉得你应该是安全的……

好啦,玩得开心 \{\{\sinv\[1\]拜——拜——\sinv\[0\]

要是你想把我的这些垃圾产出(SLOP)拿去自用,可以去 [这个素材包](https://mods.one/mod/fdtromoutils/)里找,是另外两个书呆子(NERDS)做的。他们肯收留我,人真的很好……

![](/img/omori-guide/img_0000_2109993ecf.webp)

*-[Tester](https://mods.one/author/Patch357)*

```text
.
.
.
.
```

### 视差背景 `Parallaxes`是用作地图背景的循环图像,存放在“`parallaxes`”文件夹里。它们主要用于头脑空间和遥远镇的天空,也用作黑色空间地图的背景。

*(来源:Space\_parallax.png,原版游戏)*

头脑空间的星空。

![](/img/omori-guide/img_0000_62876fb5b1.webp)

*(来源:sunset\_sky.png,原版游戏)*

遥远镇的日落天空。

![](/img/omori-guide/img_0000_84c6fbea34.webp)

*(来源:!parallax\_glitch.png,原版游戏)*

这是黑色空间 `Subconscious Spill`(潜意识溢出)里用的雪花屏噪点。`Room of Stumps`(树桩房间)里玛丽的照片、`Time Area`(时间区域)里的时钟也都是视差背景,还有一大堆别的,要全列出来恐怕得费一番工夫。

`parallax`图像只有一条规格:文件名前带 <var>!</var> 的图像会与地图保持对齐,不带 <var>!</var> 的图像则会随玩家移动。另外,任何要滚动的视差背景最好都做成无缝边缘——不过这一点,你自己应该也猜得到……

![](/img/omori-guide/img_0000_1cf36c7a3e.webp)

`Parallaxes`还可以用来把地图加载进编辑器,方便把事件放到正确的位置,不过这在 [地图制作章节](/omori/modding-guide/04-maps/)里有更详细的讨论。

### 图片 `Pictures`是显示在画面最上层的图像,可以用几种不同的方式控制。`Pictures`的用途五花八门,但大体上可以归结为一句话:出于这样那样的原因,出现在世界画面之上的图像。

包括但不限于:

```text
 Cutscenes 
```

美术弹窗

```text
 Lighting 
```

![](/img/omori-guide/img_0000_bf03e8fdb9.webp)

*(来源:release\_stress\[5x5\].png,原版游戏)*

“释放压力”过场动画。

*(来源:pictures\_fa\_extra.png,原版游戏)*

遥远镇美术弹出图的一张合集。是的,这里面还混了一些

梦世界的图片。:D

![](/img/omori-guide/img_0000_55af9ad2ad.webp)

*(来源:lighting\_overlay.png,原版游戏)*

光照覆盖层。

你想显示在画面顶部的 `picture`,其每一帧的尺寸必须落在 640×480 像素以内,但比起其他大多数素材形式,它们的玩法要灵活得多。

它们还可以在游戏内被赋予 `Multiply`(正片叠底)、`Screen`(滤色)和 `Add`(线性减淡/添加)混合模式,这点非常好用。比如 [parallels](https://mods.one/mod/parallels)里太空船的停电画面就用了正片叠底图层。

此外,这些图片还能用脚本来做动画,过场动画通常就是这么实现的。这些脚本我们列在了 [事件章节](/omori/modding-guide/03-events/)里。

最后!(我知道讲了不少,但图片是真的好用)图片可以被“钉”在当前地图的中心。而且由于 ID 为 1 的图片会显示在玩家和事件之下,这就意味着你可以让一整张地图本身是一张图片,并按这种方式显示。这也能用来做更复杂的、地图专属的覆盖层。

![](/img/omori-guide/img_0000_5f2b67d46c.webp)

### 物品图标

接下来是物品图标。在原版游戏里,这些图标位于 img/system 文件夹,分散在一组图集中:`itemCharms.png`、

`itemConsumables.png`、`itemImportant.png` 和 `itemWeapons.png`。而 `itemWeapon.png` 和 `itemWeapons.png` 完全相同,实际使用的是 itemWeapons 这张。

顾名思义,每张图集各用于一种特定类型的物品。

游戏会根据物品在游戏内被标记的类型,从对应的那张图集调用图像。

*(来源:itemWeapons.png,原版游戏)*

物品图标为 108×108 像素,排布方式随你,只要图集宽度固定、每行能正好放下整数个图标就行。看原版图集就特别明显:它们每行混着排 7、8 或 9 个图标。图集高度可以无限延长,想加多少行都行。

![](/img/omori-guide/img_0000_4269b072ec.webp)

![](/img/omori-guide/img_0000_2747204634.webp)

![](/img/omori-guide/img_0000_4579251d77.webp)

风格上,原版始终是黑底白色铅笔画风,但实际上你想做成什么样都行。

不过,用原版那套方法访问这些图标既费劲又不现实。改用 Stahl\_AltItemIcon,你只需指定图集名称再加索引,不管物品是什么类型,都能取到任意图标。这个插件可以在 [OMORI](https://github.com/modsone/omori-modding-resources) [Modding 资源仓库](https://github.com/modsone/omori-modding-resources)里找到;要是那里没有,去 [Omori Modding Hub](https://discord.gg/exu5KTxDvC)问一声也能找到。这个方法还允许你定义新的物品图集。

不过有一点要记住:图标会被压缩并重新缩放,以塞进游戏指定的位置。因此,直接拿像素精灵当图标用,不模糊是不可能的。如果你就是想用像素精灵,可以用 [FD_ItemIconRescale](https://github.com/modsone/omori-modding-resources/blob/main/Battle%20System%20Plugins/Menu%20and%20UI/FD_ItemIconRescale.js) 创建不会被缩放的图标图集。(请注意,它尚未与商店图标一起测试过,物品放进游戏内商店时可能不起作用。如需协助,请联系 FruitDragon——他是该插件的作者,也是本文档的所有者。)

### 窗口皮肤

接下来是窗口皮肤!如果你玩过 [Broken Dreams](https://mods.one/mod/brokendreams)、[HIKITO](https://mods.one/mod/hikito)、[OMORI.exe](https://mods.one/mod/omoriexe) 或其他许多 Mod,那你已经见过窗口皮肤的实战了。它们是 `img/system` 里的图像,决定游戏中各种窗口的外观,比如文本框和菜单。

*(来源(从左到右):Window.png,原版游戏 | REDACTED.png,TomatoRadio 的未公开项目 | Window\_Guide.png,TomatoRadio)*

这里我们就能看清 `windowskins`的构造了。先从左上角开始。这个 96×96 的方块是 `windowskin`的背景,会被拉伸以贴合任何窗口的尺寸。由于会被拉伸,精细的图像会变形、模糊,所以颜色和渐变才是 `windowskin`背景的最佳选择。

背景右边是边框和箭头。边框由 4 条边和 4 个角组成,靠平铺拼出窗口的边框。它们不会被拉伸变形。大多数 `windowskins`的边框厚 5 像素,但最厚可以到 24 像素。四角也可以加装饰设计,不过在较小的窗口(比如名字框)上可能会显得乱。

箭头用在菜单里,提示这里可以滚动。它们要放在指南图中那些灰色矩形的范围内,不会拉伸。

图像左下角是一个平铺图案。它是一张 96×96 的精灵,会叠加在背景之上,并平铺满整个窗口。[Lucille](https://mods.one/mod/roseglass)的 `windowskin`上那些星星就是这么实现的。图中那个绿色 `windowskin`里,会有藤蔓铺满窗口。建议把这部分做成半透明。

光标和暂停标志(位于右下象限的上半部分)在 <span class="og-g">OMORI</span> 里几乎见不到,但为了完整性,我还是把两个都讲讲。

对于不用“红手”光标图标来选择选项的菜单,游戏可能会退回 <span class="og-g">RPG Maker MV</span> 默认的光标显示方式,也就是用 `windowskin`的这一部分。它会像背景一样在选项上拉伸,并以大约一秒为周期淡入淡出。

而暂停标志是一个 24×24 的动画图标,原本会在消息窗口等待玩家输入时顶替红手出现。这个功能完全没被用上,因此 `windowskin`的这一部分也完全闲置。

最后,颜色!由 32 个 12×12 方块组成的网格,构成了可以通过该 `windowskin`用于文本的颜色列表。更确切地说,游戏取的是从左上角以 1 起算的第 (7,7) 个像素(已在指南图中框出)来决定颜色,其余像素随便你怎么用,比如标记索引号。值得注意的是,更换 `windowskins`可能引起这些颜色出问题,操作请谨慎。

说到这儿,那我们到底要怎么更换 `windowskin` 呢?

这个嘛,正常情况下你是(轻易)换不了 `windowskin`的。所以 Mod 们转而使用 [HIME_WindowskinChange](https://himeworks.com/2016/04/windowskin-change/) 插件。有了它,这段脚本:

```text
$gameSystem.setWindowskin(“NAME”); 
```

就能用来更换 `windowskin` 了。当然,关于窗口皮肤可能出的各种毛病,我要一口气给你念叨一遍。若有对应的解决办法,我也会一并附上。

- 每换一个角色说话就得改一次 `windowskin`,太折腾了。
    - 使用 [WN_ExtendedYAML](https://github.com/modsone/omori-modding-resources/blob/main/Data%20Organization%20Plugins/WN_ExtendedYAML.js)或更推荐的 [DoubleExtendedYAML](https://github.com/modsone/omori-modding-resources/blob/main/Data%20Organization%20Plugins/DoubleExtendedYAML.js),可以直接在 YAML 里设置窗口皮肤,绕开这个问题。
- 为某条消息更换的 `windowskin`会连带着应用到主菜单和其他我不想动的地方。
    - 使用 [TR_RestrictiveWindowskins](https://github.com/modsone/omori-modding-resources/blob/main/UI%20plugins/Window%20Skins%20or%20Layout/TR_RestrictiveWindowskins.js) 可以控制哪些窗口会被这次 `windowskin`更换波及。
- 文字颜色没有跟着更新。
    - 使用 [BABY_ExternalColorImage](https://github.com/modsone/omori-modding-resources/blob/main/UI%20plugins/Window%20Skins%20or%20Layout/BABY_ExternalColorImage.js) 应该能修好,但不保证回回都灵。
- 我需要多于 32 种颜色。
    - 用 [BABY_ExternalColorImage](https://github.com/modsone/omori-modding-resources/blob/main/UI%20plugins/Window%20Skins%20or%20Layout/BABY_ExternalColorImage.js),能拿到 288 种颜色。应该够你用了。
- 我的 `windowskin`在正式版里不生效/我在正式版里有文字变成黑色。
    - 确保你的 [OneLoader](https://mods.one/mod/oneloader) 和 [BundleTool](https://mods.one/mod/bt)都是最新版本。旧版本在给原版 `Window.png` 打补丁时有问题。

### 影片 `Movies`是在游戏内播放的预渲染视频,专门用于各种游戏内过场。它们全是 640×480 的 `.webm` 文件。

它们主要用于动态图层太多、`pictures`应付不来或效果不好的场合。举几个例子:

```text
 All three credits cutscenes 
```

红色空间(Red Space)过场

书柜(The Bookcase)过场

OMORI 的诞生(The Creation Of OMORI)过场

很遗憾,我们没法在本教程里嵌入这些示例 :),但请务必去 playtest 文件夹里的“`movies`”文件夹亲眼看看!(不是 `img`文件夹!)

### 图集(Atlas)

最后是 `Atlases`。这帮家伙相当古怪,但也极其有用,我要是把它们漏掉那可说不过去,毕竟它们还是 <span class="og-g">OMORI</span> 里最复杂的图像类型。

简单来说,`Atlases`就是精灵图集。它们是由多张小图拼成的大图,通常按网格或其他格式排布。引擎随后会把这些大图拆解开,变成一张张可以单独调用的图像。

我们来看一个原版游戏里的例子,好解释清楚:

![](/img/omori-guide/img_0000_efaa117c19.webp)

*(来源:battleATLAS.png,原版游戏)*

这就是存放标题界面精灵的那张 `atlas`!在这里翻一翻,你能看到两个 OMORI、桑尼,还有当前与你的主题相反的那个标题配色。

现在来看看到底是什么在拆解这张图。

进入你 playtest 的 `data`,你会找到一个叫 `Atlas.yaml` 的文件。

用你顺手的编辑器打开它,迎接你的将是这幅景象:

![](/img/omori-guide/img_0000_768400676f.webp)

*(来源:atlas.yaml,原版游戏)(我觉得这张应该一目了然……)*

首先,这些条目全部缩进在 `source:` 行之内。为免讲得太技术化,这么说吧:如果某行缩进在另一行里面,代码里就可以通过上一级行来调用缩进行的那个条目。因此,游戏需要所有这些条目都缩进在 `source:` 之内。

接下来看图像本身。

![](/img/omori-guide/img_0000_289380b08d.webp)

很凑巧,标题界面正好是列表里的第一张图,我们都不用滚动页面就能分析它。

第一行是你要创建的图像的文件路径,包括所有文件夹和文件扩展名,也就是 <var>.png</var>。

这也就会成为实际游戏运行时使用的文件名,所以记住它。

接下来的几行则缩进在文件名之下。

`atlasName:` 这是完整 `atlas`大图在 `img/atlases` 中的名称。

`rect:` 其中 `x` 和 `y` 是原图左上角在新图中的落点坐标。`width` 和 `height` 是新图的尺寸。如果听着犯迷糊,那就把 `x` 和`y` 设为 <var>0</var>,把 `width` 和 `height` 设为图像本身的尺寸。

`sourceRect:` 其中 `x` 和 `y` 是图像在完整 `atlas` 中左上角的坐标。`Width` 和 `Height` 顾名思义,不言自明。

如果一切都设置正确,你就可以随时在游戏里使用这些图像了,它们的行为和其他图像别无二致。

当然,还有一些注意事项。

这些图像不会出现在编辑器里,所以如果你想用编辑器来选取图像,是看不到它们的。这意味着,它们最适合用在靠备注标签(notetag)或脚本调用的图像上,比如脸图集或徽章。

这里有一个把它们用作 [parallels](https://mods.one/mod/parallels)状态图标的例子。
