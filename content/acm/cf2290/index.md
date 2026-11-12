---
title: "Codeforces Round 1134 (Div. 4)"
tags: [codeforces, div-4, 题解]
aliases: ["/acm/28post/"]
date: 2026-11-12
draft: false
comments: true
upsolve:
  - problem: "G1"
    name: "Lakeside Trail (Easy Version)"
    url: "https://codeforces.com/contest/2290/problem/G1"
    status: "skip"
    note: "环形步道只能加土，最小化相邻段最大高差（二分 + 贪心 tag），空模板零提交"
  - problem: "G2"
    name: "Lakeside Trail (Hard Version)"
    url: "https://codeforces.com/contest/2290/problem/G2"
    status: "skip"
    note: "同题 hard：n 与 Σn 放大到 2×10⁵ 量级，145 人通过，没开题"
  - problem: "H"
    name: "Extra Road"
    url: "https://codeforces.com/contest/2290/problem/H"
    status: "skip"
    note: "树上先加一条新边，抗住最坏断边最大化可达城市数（dfs + 贪心 tag），全场只 77 人通过，没开题"
---

> **30 秒版**：rank **686 / 7771**，6 / 9（A–F），罚时 383，rating 未更新（截至发稿还没进 ratingChanges）。A/C 各多一发 WA——C 那发是 **0 个测试点通过**的裸奔（「样例都过不了为啥要交」，注释原话）；E 的正确思路赛后才归档，留在 `E.cpp` 里的半成品被自己的暴力判错 152 / 300 组；**F 一发过**（全场通过率 9%）；G1/G2/H 三个空模板零提交。

比赛时间：2026-11-12 22:35 ~ 00:50（135 分钟）｜[比赛页](https://codeforces.com/contest/2290)｜9 项 7771 人计入排名，AK 44 人

CF 的判定和排名这次是全的：官方 API 拉回了全部 **8 条提交记录**（6 AC + 2 WA）和整张榜单。官方题解截至发稿还没发布，等出了再补对比。

<details class="tl-fold">
<summary>做题情况（提交时刻来自 CF 评测记录）—— 点开展开</summary>

- 0:04:50 A WA（过 1/2 个 pretest）→ 0:08:03 A 过（第二发）
- 0:16:11 B 一发过
- 0:41:03 C WA（**0 个测试点通过**）→ 0:51:43 C 过（第二发）
- 1:04:32 D 一发过
- 1:41:49 E 一发过
- 2:13:59 F 一发过
- G1 / G2 / H：三个空模板，零提交

</details>

## A - Three Piles
https://codeforces.com/contest/2290/problem/A

> **题意**：三堆石子数量 $a, b, c$。必须做**恰好一次**移动：从一堆拿一颗放到另一堆。问能否使三堆相等。

**代码**（0:08:03 过，第二发）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxx = 110;
int t,n;

//比赛总用时23min 唐还写错了一开始
inline bool check(int a,int b,int c){
	int tmp[4];
	tmp[0] = a,tmp[1] = b,tmp[2] = c;
	sort(tmp,tmp+3);
	return (tmp[0] + 1 == tmp[1] && tmp[1] == tmp[2] - 1);
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		int a,b,c;
		cin>>a>>b>>c;
		if(check(a,b,c)) cout<<"YES"<<'\n';
		else cout<<"NO"<<'\n';
	}
	return 0;	
}
```

### 解读

设目标和为 $3T$，一次移动后三堆要变成 $T, T, T$：捐石子的那堆必须是 $T+1$、收石子的必须是 $T-1$、第三堆恰好是 $T$——所以排序后必须**恰好是连续三数** $\{x, x+1, x+2\}$。第一发（0:04:50）判据写岔了没留档，被第二个 pretest 打回；修正后排三下判连续，8 分钟收工。

## B - Stubborn Pen
https://codeforces.com/contest/2290/problem/B

> **题意**：一支笔红蓝两色，每写一个字母自动换色；写每个字母前可以手动换色。写定串 $s$（`R`/`B`），求最少手动换色次数。

**代码**（0:16:11 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxx = 110;
int t,n;
string s;

//比赛总用时30min 唐

int check(){
	int ans = 0,p = 0;
	for(int i=0;i<n;i++){
		int now = 0;
		if(s[i] == 'R') now = 0;
		if(s[i] == 'B') now = 1;
		if(now == p) p = 1 - p;//唐 一开始写的是 now & p 怎么不对？
		else ans++;
	}
	return ans;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n;
		cin>>s;
		cout<<check()<<'\n';
	}
	return 0;	
}
```

### 解读

维护「不手动换色时下一笔的颜色」$p$：字母要的颜色正好是 $p$ 就白写（笔自动翻面，$p$ 翻转），否则手动换一次（$ans{+}{+}$，$p$ 落在要写的颜色上不动）。注释里那句「唐 一开始写的是 now & p 怎么不对？」——`&` 和 `==` 一字之差，状态机整个反了。

## C - Books on a Shelf
https://codeforces.com/contest/2290/problem/C

> **题意**：$n$ 本书排成一排。一本书「从左可见」当且仅当严格比左边所有书高，「从右可见」同理。求「至少一侧可见」的书数的最大值，并给出一个取得最大值的排列。

**代码**（0:51:43 过，第二发；第一发 0:41:03 交了个 **0 个测试点通过** 的裸奔）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n,k;
int h[maxn],ans[maxn];
bool b[maxn];

//比赛总用时50min 有点唐 网络还有问题叫不上
//shit唐了 边界条件判断有问题 我他妈是个傻逼吧样例都过不了为啥要交 1h
//直接排序的数量是 n-1 最大的书的数量是 n 
//哦我唐了 直接排序就是最好的 样例是因为有重复的元素 不对 放两边也是可以的 烫完了

void solve2(){
	int tot = 0;
	k = 0;
	sort(h+1,h+1+n);
	int last = 0;
	for(int i=1;i<=n;i++) if(last != h[i]) b[i] = 1,k++,last = h[i],ans[++tot] = h[i];
//	last = ans[tot];//唐了 会漏边界
	last = 0;
	for(int i=n;i>=1;i--){
		if(b[i]) continue;
		ans[++tot] = h[i];
		if(last != h[i]) k++,last = h[i];
	}
	return;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n;
		for(int i=1;i<=n;i++) cin>>h[i],b[i] = 0;
		solve2();
		cout<<k<<'\n';
		for(int i=1;i<=n;i++) cout<<ans[i]<<' ';
		cout<<'\n';
	}
	return 0;	
}
```

### 解读

升序铺开：每个**互异值**各有一本从左可见（$k$ = 互异值个数）；重复的书按降序补在右侧——每种值的第一本补位书天然从右可见（右边没有比它高的），同值的第二本开始就隐身。注释里那段「我他妈是个傻逼吧样例都过不了为啥要交 1h」就是第一发的案底：边界没判对、样例都没跑，41 分钟把一分都送了。第二发冷静下来把样例过完才交，51 分钟收工。对拍以外官方样例 5 组全对（排列不唯一，判分器取任意合法解）。

## D - Letters Down
https://codeforces.com/contest/2290/problem/D

> **题意**：每次操作选一个非 `a` 字母 $x$，把 $s$ 里**所有** $x$ 替换成字母表前一个字母。求把 $s$ 变成回文的最少操作次数。

**代码**（1:04:32 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
string s;
bool a[27];

//比赛总用时1h20min
//很简单 答案不会超过 26*26？哦不对就是26 而且只需要注意每一个字母的下标就行了 如果这个字母已经是回文的就不用变 否则就变到底
//然后燃油一点 不用每一个n都重复的扫 直接扫一遍字母表就行了
//为了 保证题目有解 可以简单证明 最好的操作就是 一直对 两个对称的位置操作直到变对对称为止 因为一直在表笑所以一定有解
//同时 不需要真的对字符串操作 因为每一次重复标记 只会带来26n 在字符串上模拟感觉会很麻烦

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		string s;
		cin>>n;
		cin>>s;
		for(int i=0;i<26;i++) a[i] = 0;//唐 忘清空了
		for(int i=0;i<n/2;i++){
			if(s[i] == s[n-1-i]) continue;
			int l = min(s[i]-'a',s[n-1-i]-'a'),r = max(s[i]-'a',s[n-1-i]-'a');
			for(int j=l+1;j<=r;j++) a[j] = 1;
		}
		int ans = 0;
		for(int i=0;i<26;i++) if(a[i]) ans++;
		cout<<ans<<'\n';
	}
	return 0;	
}
```

### 解读

对称位置不相等时，把较大字母降到较小字母，途中 $(min, max]$ 的每个字母都至少被一次操作覆盖——对每对取并集，答案就是被标记的字母数。不用真在字符串上模拟（注释：每次重复标记只会带来 $26n$），一遍配对 + 一遍数标记，$O(26n)$。注释「唐 忘清空了」——多测不清空标记数组，第一组数据之外的组全废。

## E - Avalanche
https://codeforces.com/contest/2290/problem/E

> **题意**：$n$ 堆石子。轮流取石：选非空堆 $i$ 拿走一颗，同时给 $[\\max(1, i-k), i-1]$ 的每堆各补一颗新石子。无法行动者输。Alice 先手，双方最优，问谁赢。$a_i$ 可达 $10^9$。

**半成品**（E.cpp，00:08 落盘——**这版是错的**）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n,k,ans;
int a[maxn];

//比赛总用时1h32min
//我是猪吗 1h44min
//实际上 就是模拟 删一个数值到删完 同时还对前面 k个数加上他自己 同时 累加a[i] 去看看最后的操作是否为偶数

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		ans = 0;
		cin>>n>>k;
		for(int i=1;i<=n;i++) cin>>a[i],a[i] %= 2;
		for(int i=1;i<=n;i++){
			int r = min(n,i+k);
//			int len = r - i - 1;
			int len = r - i;
//			a[i] = (a[i] + k) % 2;//我是个傻逼吧 几把都写上lne了
			a[i] = (a[i] + len) % 2;
		}
		for(int i=n;i>=1;i--){
			if(!a[i]) continue;
//			int r = max(1,i-k);
//			for(int j=i-1;j>=r;j--) a[j] = (a[j] + 1) % 2;//可以优化 因为只影响ans的奇偶性 所以 直接对 ans 加k是等价的其实
//			ans = (ans + k) % 2;//不太对，，再想想 有后有效性 想一想 不管 a[i] 是否多大 总有奇偶性 所以 a[j] + 1 or 0 是必然的 不在乎a[i] % 2 == 0?或者 a[i] == 0
//那么 不妨一开始的时候直接用一个差分来预处理？或者用滑动窗口？因为如果长度无限 某一点a[i] + (q) % 2是确定的 q == k - 1 只有两端的元素会受到影响
//说的没问题
			ans = (ans + 1) % 2;
		}
		if(ans&1) cout<<"Alice"<<'\n';
		else cout<<"Bob"<<'\n';
	}
	return 0;	
}
```

**赛后重写版**（E重写.cpp，1:48 落盘——**这版才是对的**）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n,k,ans;
int a[maxn],g[maxn];

//我是猪吗 1h57min
//需要一个思路转化 其实 就是等价于什么神秘拿石头博弈 直接异火就行了 因为 每一次产生的新石头数量是确定的 所以可以直接写他的奇偶新来一伙
//本质不能预处理的原因 sg函数有后有效型 但是 sg在这种情况下 只有 0 或者 1的取值

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		ans = 0;
		cin>>n>>k;
		for(int i=1;i<=n;i++) cin>>a[i],a[i] %= 2;
		int p = 0;                       
		for(int i=1;i<=n;i++){
			if(!p) g[i] = 1;
			else g[i] = 0;     
			if(a[i]) ans ^= g[i];
			p ^= g[i];
			if(i > k) p ^= g[i-k];
		}
		if(ans) cout<<"Alice"<<'\n';
		else cout<<"Bob"<<'\n';
	}
	return 0;	
}
```

### 解读：一桩「AC 版本失踪案」

这题的复盘差点被自己骗过去。事实链：

1. 比赛 **1:41:49 E 一发 AC**——AC 的那版思路是对的；
2. 但留在 `E.cpp` 里的落盘版（00:08 存盘，注释「我是个傻逼吧 几把都写上len了」）是个半成品：**官方样例第 3 组都过不去**（$n=4, k=1, a=[0,0,1,0]$ 输出 Bob，期望 Alice）；
3. 写了个暴力博弈当裁判，小数据 300 组随机对拍：落盘 E.cpp **错 152 组（一半）**，E重写.cpp **0 组错**——两个文件名正好把「赛时 AC 的思路」和「落盘的废稿」对调了。

重写版的思路（注释原话：「等价于什么神秘拿石头博弈 直接异或就行了 因为每一次产生的新石头数量是确定的」）：每颗石子的贡献可以拆成独立的 0/1——位置 $i$ 的权 $g_i$ 满足滑动窗口异或递推（$g_i = 1 \Leftrightarrow$ 前$k$个 $g$ 的异或为 0，即 $g$ 在 $i \\equiv 1 \\pmod{k+1}$ 处为 1），把奇数堆的权全部异或起来就是胜负。$a_i$ 只留奇偶，$10^9$ 也不怕。教训：**AC 的版本要当场归档**——比赛里交出去的代码和硬盘上的文件不是一回事，赛后复盘先 `git diff` 再说话。

## F - Value Counters
https://codeforces.com/contest/2290/problem/F

> **题意**：对排列 $p$ 定义 $b$：对每个满足 $x < y$ 且 $x$ 在 $p$ 中位于 $y$ 左边的数对 $(x, y)$，$b_x$ 减一、$b_y$ 加一（$b$ 按**值**索引）。给定 $b$，构造一个生成它的排列 $p$，不存在输出 -1。

**代码**（2:13:59 一发过，全场通过率 9%，713 / 7771）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
int ans[maxn],b[maxn];
bool v[maxn];
bool pd = 0;

//比赛总用时 2h 28min
//神秘构造 吓尿了
//逆序对 有关 感觉 应该是个什么转化 打表看样例试试
//逆序代表的是 后面有一个比他小的 
//感觉这个bi有点像差分？
//-1 就是后面有个 比他小的 +1 就是 前面有个比他大的
//观察一下  一个真诚工行的序列会有什么
/*
2 1 3
-1 -1 2
3 1 4 2
-2 1 -1 2
*/
//很明显的 一个是 sum (bi) == 0 的时候才有解
//考虑 原来的排列 
/*
1 2 3 4
3 1 4 2
想想能不能用一方方式映射这个pos
pos - 1 == (正序) + (逆序)
！！！！！可以拆贡献
pos 在 1 - n

*/

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>b[i];
		pd = 0;
		for(int i=1;i<=n;i++) v[i] = 0;
		for(int i=1;i<=n;i++){
			int pos = b[i] + n - i + 1;//惊人的恒等式！！！
			if(pos < 1 || pos > n || v[pos]){
				pd = 1;
				break;
			}
			v[pos] = 1,ans[pos] = i;
		}
		if(pd){
			cout<<-1<<'\n';
			continue;
		}
		for(int i=1;i<=n;i++) cout<<ans[i]<<' ';
		cout<<'\n';
	}
	return 0;	
}

```

### 解读

一个恒等式撑起整道题：若值 $i$ 位于位置 $pos(i)$，则 $b_i = pos(i) - (n - i + 1)$——一行推导：$b_i = $（前面比它小的）$-$（后面比它大的）$= (pos-1-A_1) - ((n-i)-A_1) = pos - 1 - n + i$，容差项 $A_1$（前面比它大的个数）在相减时抵消。所以 $pos(i) = b_i + n - i + 1$，注释里自己都标了「惊人的恒等式！！！」。构造就是逐值算出 $pos$：越界或重复判 -1，否则把 $i$ 放进 $pos$。前置校验：$\sum b_i = 0$（正逆序对总数相等）在变换下自动成立，无需单独判。

## G1 / G2 / H（未开题）

三个空模板零提交——F 收工在 2:14，距离终场还有 21 分钟，全躺在椅子上等结束。一句话挂号：

- **G1 / G2 Lakeside Trail**：环形步道只能加土不能挖，$k$ 单位土最小化相邻段最大高差（easy：$n \le 500$；hard：$n \le 2 \times 10^5$）。tag：二分 + 贪心。
- **H Extra Road**：树上先加一条新边，随后对手**任意**关掉一条路（含新边），最大化最坏情况下从 1 号首都可达的城市数。tag：dfs + 贪心，全场只 77 人通过。

---

## 赛后总结

**成绩**：6 / 9（A–F），rank **686 / 7771**，罚时 383，8 条提交 6 AC 2 WA。rating 尚未发布（截至 11-13，`contest.ratingChanges` 还是空的，等 CF 出了再补）。官方题解同样未发布，本文各题解读为赛后独立复盘，等官方出了再对照。

**做得好的**：

- **F 一发过**：通过率 9%（713 人）的分水岭构造题，从「神秘构造 吓尿了」到「惊人的恒等式」——打表观察样例、发现 $\\sum b_i = 0$ 的必要条件、再从注释里那句「pos − 1 == (正序) + (逆序)」拆出贡献，整条链路是自己走出来的。
- **E 一发过**：拿石头博弈的异或转化赛时就走通了（虽然事后归档出了乌龙，见下）。
- **C 二发收敛**：裸奔 WA 之后没有继续裸奔，把样例跑通才交第二发。

**不足**（这场的账，笔笔是自己欠的）：

1. **C 的裸奔提交**：0:41 交了一发 **0 个测试点通过** 的代码——自己的注释写得最狠：「我他妈是个傻逼吧样例都过不了为啥要交」。 WA 一分不冤：样例没跑就交，是把判分器当许愿池。
2. **E 的归档事故**：AC 的正确思路没有当场存盘，留在 `E.cpp` 里的是半成品——被自己赛后的暴力对拍判错 152 / 300 组，连官方样例第 3 组都过不去。两个文件名（`E.cpp` / `E重写.cpp`）把废稿和正解正好对调，复盘第一眼差点被骗。规矩：**过题的那一版立刻另存归档**，废稿改名 `bak`。
3. **A 的首发抢跑**：4:50 交了一发判据写岔的（过 1/2），「连续三数」的判定想清楚也就多花 3 分钟。
4. **最后 21 分钟躺平**：F 收工后 G1/G2/H 三个空模板零提交——G2 全场 145 人过、H 77 人过，这两分在榜上 198 个 ≥7 题选手手里，不在自己这。哪怕只读题面，也该把「没开题」换成「读了没想出来」。

下一场的清单：提交前跑样例（C 的账）、过题版本当场归档（E 的账）、收工前把剩余题面读一遍（G/H 的账）。
