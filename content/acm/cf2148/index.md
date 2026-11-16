---
title: "Codeforces Round 1050 (Div. 4) · VP"
tags: [codeforces, div-4, 题解]
aliases: ["/acm/30post/"]
date: 2026-11-16
draft: false
comments: true
upsolve:
  - problem: "F"
    name: "Gravity Falls"
    url: "https://codeforces.com/contest/2148/problem/F"
    status: "skip"
    note: "左对齐堆叠 + 重力下落，求字典序最小的最终网格（贪心 + 排序），VP 时写了 22 分钟放弃，348 人通过"
  - problem: "G"
    name: "Farmer John's Last Wish"
    url: "https://codeforces.com/contest/2148/problem/G"
    status: "skip"
    note: "整除前缀 gcd 的最后一次下降位置最大化（数论 + 贪心），全场 121 人通过，空模板零提交"
---

> **30 秒版**：VP 5 / 7（A–E）。**D 吃两发 WA**——「奇偶交替取 top」的假贪心想错，42 分钟才过（7275 人的题）；**F 写了 22 分钟没提交**（感冒药 + 瞌睡，放弃了，348 人过）；B 11 分钟时吃一发读错题的 WA（「能不能认真看一下题目」，注释原话）。G 零接触。VP 不计 rating；官方题解已发布，各题对比已补。

比赛时间：原赛 2025-09-13，VP 2026-11-16 21:20 起（135 分钟场次，实际 22:59 收工）｜[比赛页](https://codeforces.com/contest/2148)｜[官方题解](https://codeforces.com/blog/entry/146112)

CF 的提交记录、榜单、官方题解（blog/entry/146112）都是全的。终版代码与官方样例本地验证：A–E 五题全过。

<details class="tl-fold">
<summary>做题情况（提交时刻来自 CF 评测记录，VP 起点为 21:20）—— 点开展开</summary>

- +0:01:53 A 一发过
- +11:55 B **WA**（读错题，数了 `a[i] < x` 的个数）→ +14:52 B 过
- +25:18 C 一发过
- +31:07 D **WA** → +36:39 D **再 WA**（奇偶交替取 top 的假贪心）→ +42:27 D 过
- +1:16:56 E 一发过
- +1:39 F 残稿落盘，放弃——没提交
- G 空模板（赛前就建好了的），零提交

</details>

## A - Sublime Sequence
https://codeforces.com/contest/2148/problem/A

> **题意**：序列 $x, -x, x, -x, \dots$（长度 $n$），求和。

**代码**（+1:53 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int t;

//比赛总用时 1 min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	while(t--){
		int n,x;
		cin>>x>>n;
		if(n&1) cout<<x<<'\n';
		else cout<<0<<'\n';
	}
	return 0;	
}
```

### 官方题解对比

**官方做法**：相邻的 $(x, -x)$ 两两配对抵消；$n$ 为奇数时末尾剩一个未配对的 $x$，答案就是 $x$。$O(1)$。

**我的做法与解读**：与官方一致——`n & 1` 判奇偶直接出。全场 9828 人过，开局 1 分钟，正常发挥。

## B - Lasers
https://codeforces.com/contest/2148/problem/B

> **题意**：平面 $[0,x] \times [0,y]$，从 $(0,0)$ 走到 $(x,y)$，途中有 $n$ 条横激光、$m$ 条竖激光，每穿过一条计一次。路径必须连续且在平面内，求穿过激光次数的最小值。

**代码**（+14:52 过，+11:55 有一发 WA）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t;
int a[maxn],b[maxn];

//比赛总用时 12 min 一直在说话 太慢了
//14min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	while(t--){
		int n,m,x,y;
		cin>>n>>m>>x>>y;
		int q = 0,p = 0;
		for(int i=1;i<=n;i++){
			cin>>a[i];
//			if(0 < a[i] && a[i] < x) q++;//我他妈是个傻逼吧 几把 人家是 a[i] < y
		}
		for(int i=1;i<=m;i++){
			cin>>b[i];
//			if(0 < b[i] && b[i] < y) p++;
		}
//		cout<<n+m<<'\n';
//		cout<<q+p<<'\n';//不是 这不是一定要走过这些激光吗？
		cout<<n+m<<'\n';//我是傻逼吧 能不能认真看一下题目
	}
	
	return 0;	
}
```

### 官方题解对比

**官方做法**：路径是连续曲线且被限制在矩形内——**无论怎么走，区域里的每一条横激光和竖激光都必然被穿过**，答案就是 $n + m$。$O(1)$。

**我的做法与解读**：第一发把题读成了「数坐标小于 $x$ / $y$ 的激光条数」——注释原话「我他妈是个傻逼吧 几把 人家是 a[i] < y」「我是傻逼吧 能不能认真看一下题目」。11 分钟的 WA 之后才看懂：所有激光横贯整个矩形（横激光从 $(0,a_i)$ 到 $(x,a_i)$），连续路径躲不开任何一条。$A$ 写了 1 分钟、$B$ 吃了 14 分钟——读题账。

## C - Pacer
https://codeforces.com/contest/2148/problem/C

> **题意**：要求在时刻 $0 \dots m$ 分别位于 $a_0 = 0, a_1, \dots, a_n$（每分钟走一步）。在时刻 $i$ 恰好在要求点上有屏（得分 +1）。每分钟可以选择走或原地不动，求最大得分。

**代码**（+25:18 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
int a[maxn],b[maxn];

//比赛总用时 24 min 太慢了


int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	while(t--){
		int n,m;
		cin>>n>>m;
		ll ans = 0;
		for(int i=1;i<=n;i++){
			cin>>a[i]>>b[i];//还能再升一下内存不过没必要了
			ll det = a[i] - a[i-1];
			if(b[i] == b[i-1]){
				if(det & 1) ans += det - 1;
				else ans += det; 
			}
			else{
				if(det & 1) ans += det;
				else ans += det - 1;
			}
		}
		ans += m - a[n];//别忘了最后的
		cout<<ans<<'\n';
	}
	
	return 0;	
}
```

### 官方题解对比

**官方做法**：两个相邻要求点之间最多拿满 $a_{i+1} - a_i$ 分（每分钟都走）；拿满的条件是 $(a_{i+1} - a_i)$ 与 $(b_{i+1} - b_i)$ **同奇偶**（走 $d$ 步改变朝向 $d$ 次，奇偶必须一致）。奇偶不符就先原地站一分钟，拿 $a_{i+1} - a_i - 1$ 分。起点视作 $a_0 = 0, b_0 = 0$，最后补上 $m - a_n$ 段。

**我的做法与解读**：与官方完全一致——同奇偶满拿、异奇偶减一，尾部补上。24 分钟一发过，自己标注「太慢了」——B 的读题事故把节奏带慢了。

## D - Destruction of the Dandelion Fields
https://codeforces.com/contest/2148/problem/D

> **题意**：割草机初始关闭。按任意顺序访问每块草地恰好一次：到达时若草数为**奇数**，割草机开关**翻转**；机器开着就把这块地的蒲公英全割掉。求最多割多少。

**代码**（+42:27 过，+31:07 / +36:39 两发 WA）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t;
int ji[maxn],ou[maxn];

//比赛总用时 31 min 太慢了
//36min 又去忙别的事情 太慢了
//42min 我是个傻逼？

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int tot1 = 0,tot2 = 0;
		while(n--){
			int a;
			cin>>a;
			if(a&1) ji[++tot1] = a;
			else ou[++tot2] = a;
		}
		ll ans = 0;
		if(tot1){
			sort(ji+1,ji+tot1+1);
//			sort(ou+1,ou+tot2+1);//没必要啊
			for(int i=1;i<=tot2;i++) ans += ou[i];
//			ll s1 = 0,s2 = 0;
//			for(int i=tot1;i>=1;i-=2) s1 += ji[i];//唐了 这个地方另外一个有可能更大一点
//			for(int i=tot1-1;i>=1;i-=2) s2 += ji[i];
//			ans += max(s1,s2);
			//我是个傻逼吗
			for(int i=tot1;i>=(tot1/2)+1;i--) ans += ji[i];
		}
		cout<<ans<<'\n';
	}
	
	return 0;	
}
```

### 官方题解对比

**官方做法**：没有奇数草地则答案为 0（割草机永远开不了）。否则：**先访问奇数草数最大的一块**（开机），再把所有偶数地全访问（机器不会关），最后访问奇数地——注意每访问两块奇数地机器才会回到开的状态，所以**取奇数地里较大的一半**（排序后从大到小每隔一个取一个）。

**我的做法与解读**：终版与官方一致——偶数全收、奇数排序后取较大的一半。前两发 WA 的假贪心是想「奇数从大到小交替取，比较 $s_1 / s_2$ 两种起点」——方向就不对（注释原话「唐了 这个地方另外一个有可能更大一点」「我是个傻逼吗」）。7275 人过的题吃了两发 WA，42 分钟才收：贪心的正确形态（先开机、偶数白拿、奇数对半）想清楚再落键，能省 15 分钟。

## E - Split
https://codeforces.com/contest/2148/problem/E

> **题意**：数组 $a$ 与整数 $k$。子数组 $a[l,r]$「awesome」：$[l,r]$ 内的元素必须放进 multiset 1，其余元素任意分进 $1 \dots k$ 号 multiset，能否让 $k$ 个 multiset **完全相同**。求 awesome 子数组的个数。

**代码**（+1:16:56 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t;
int a[maxn];
int tot[maxn],cnt[maxn];

//比赛总用时 min
//开始真正的思考 感觉 和元素分配（区间长度 出现的次数）有关 
//很好 不用离散化
//还有一个约束条件是 下标连续的问题
//或许我们可以维护 值得大小为 1-n 的下标？
//要求是？至少有对于[l,r]上面的某一个值的个数 di max(di,)
//哦 我好像想到了一个 n^3的暴力？ 是否合法 判断可以优化到O(n)
//双指针？ 好多[l,r] 都是会被重复计算的 很多不合法的可以直接跳过
//似乎 需要次数整除 等等 好像可以优化到O(1)
//wow 真的写出来了 回来一定要联系一下双至臻
//1h 13min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++) cin>>a[i];
		vector<int> t;
		for(int i=1;i<=n;i++){
			if(!tot[a[i]]) t.push_back(a[i]);
			tot[a[i]]++;
		}
		bool pd = 1;
		for(int v : t){
			if(tot[v] % k != 0){
				pd = 0;
				break;
			}
		}
		if(!pd) cout<<0<<'\n';//这个很简单 因为如果不能保证平均分 那肯定不敢这么就弄都没接
		else{
			ll ans = 0;
			int l = 1;
			for(int r=1;r<=n;r++){
				cnt[a[r]]++;
				while(cnt[a[r]] > tot[a[r]] / k){
					cnt[a[l]]--;
					l++;
				}
				ans += r - l + 1;//这个需要想想 需要你判断拆贡献
			}
			cout<<ans<<'\n';
		}
		for(int v : t) tot[v] = 0,cnt[v] = 0;
	}
	return 0;	
}
```

### 官方题解对比

**官方做法**：所有 multiset 完全相同 ⟺ 每个值的全局计数 $cnt_i$ 必须被 $k$ 整除（否则答案为 0），且每个 multiset 恰好含 $cnt_i / k$ 个 $i$。于是子数组 $[l,r]$ awesome ⟺ 窗口内每个值的计数都不超过 $cnt_i / k$——双指针滑窗计数即可，总复杂度 $O(n)$ 量级。

**我的做法与解读**：与官方完全一致——先判全局整除，再滑窗「窗口内某值计数超半就收缩左端」，`ans += r - l + 1` 拆贡献计数。一发过，用时 1:13——通过率 32%（3172 人），是 A–E 里最重的一题。注释「wow 真的写出来了 回来一定要联系一下双至臻（指针）」——多测清空（`tot / cnt` 逐值还原）这次也做对了。

## F - Gravity Falls（未提交）
https://codeforces.com/contest/2148/problem/F

> **题意**：$n$ 个长度不同的数组左对齐堆叠，随后「重力」让所有悬空元素逐行下落。求一种堆叠顺序，使最终网格**字典序最小**。

**残稿**（F.cpp，+1:39 落盘，**未提交**——22 分钟只写了这些）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int t,n;

//比赛总用时 min
//开起来是什么贪心？我已经开始瞌睡了 呜呜 感冒药
//因为是左对齐的 所以长度是固定的 不会受到排列顺序的影响
//那么问题现在显而易见 尽可能让高位的数字尽可能小
//我还好像想到一个 但是那个是N^2logn的时间复杂度
//就是对于每一位排个序 然后直接从高位到低位的模拟这个选择过程
//每选择一个踢出一个
//先想想这个对吗，没错是对的 从低到高的放置，保证了
//现在的问题是 如果 哦 其实不用吧我记得
//直接强行转成 不对 空位不能补零
//累了 好累 不想打了
//感觉要用到什么预处理 倍增之类的？来快速护理这个位数不同的情况
//放弃了 VP还有32min 放弃了
//

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	
	return 0;	
}
```

### 官方题解对比

**官方做法**：最底行长度必为所有数组中的最大长度 $max_k$；「堆叠」本质是把上面的数组作为**后缀**追加到底部的数组上。设 $b_1, b_2, \dots$ 为已固定长度 $i$ 的前缀所能得到的字典序最小底行，从哪个数组接上来、以什么顺序——按数组排序后逐个转移维护，总复杂度线性对数级。

**我的做法与解读**：22 分钟写了 30 行注释和一个空 `main`——正确的观察其实已经有了（「左对齐所以各数组长度固定」「尽可能让高位的数字尽可能小」「从高位到低位模拟选择、每选一个踢出一个」），但卡在「位数不同的数组怎么对齐转移」上，叠加感冒药上头的瞌睡，1:39 直接放弃，VP 还剩 32 分钟。全场 348 人通过（3.5%）。这题归 upsolve：官方思路（按后缀追加 + 排序贪心）已经拿到，补题时先实现它再谈别的。

## G - Farmer John's Last Wish（未开题）
https://codeforces.com/contest/2148/problem/G

> **一句话**：$f(a)$ 为前缀 gcd 最后一次「下降」的位置，$g(a) = \max f(\text{重排})$；对每个前缀输出 $g$。tag：数论 + 贪心，全场 121 人通过。空模板零提交，官方题解已抓取（先按总 gcd 归一化再分析），归 upsolve。

---

## 赛后总结

**成绩**：VP 5 / 7（A–E），F 未提交、G 未开题。VP 不计 rating。官方题解已对照（blog/entry/146112），本文「官方题解对比」小节为真实官方做法。

**做得好的**：

- **E 一发过**：A–E 里通过率最低的一题（32%），整除判定 + 双指针 + 多测清空一步没错，用时 1:13。
- **C、D 的终版质量**：C 与官方逐条一致；D 推倒假贪心后的终版（开机 + 偶数全收 + 奇数对半）与官方完全同构。

**不足**：

1. **B 的读题事故**：A 花 1 分钟，B 吃一发 WA 花 14 分钟——错的不是算法，是把「必经激光计数」读成了「数坐标过滤」。教训写在注释里了：「能不能认真看一下题目」。
2. **D 的假贪心两连**：31 分钟第一发 WA 后，36 分钟又交了一发**同一个思路**的变体（交替取 $s_1 / s_2$）——两发 WA 之间没有任何新验证，纯赌。7275 人过的题。规矩同前：WA 之后第二发之前，必须有一个新构造的反例或证明。
3. **F 的 22 分钟空转**：观察全对（左对齐、高位尽量小、逐位选择），卡在「位数不同的数组怎么对齐」上就弃了——感冒药上头是真的，但 348 人过说明这题没有想象中硬。VP 的意义就是练这种「卡住之后怎么办」。
4. **G 零接触**：121 人过，空模板从赛前建到赛后。
