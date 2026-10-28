---
title: "Codeforces Round 1130 (Div. 2)"
tags: [codeforces, div-2, 题解]
aliases: ["/acm/25post/"]
date: 2026-10-26T23:12:00+08:00
draft: false
comments: true
upsolve:
  - problem: "D"
    name: "Connecting the Conflicts"
    url: "https://codeforces.com/contest/2272/problem/D"
    status: "skip"
    note: "剩 31 分钟读题——森林连树 + 最大独立集构造，图论盲区，跳过"
  - problem: "E"
    name: "Memory Cell Interception"
    url: "https://codeforces.com/contest/2272/problem/E"
    status: "skip"
    note: "只剩模板——「看起来是什么数据结构 / 神秘拆贡献？？」方向没锁死"
---

比赛时间：2026-10-26 22:35 ~ 00:50（UTC+8，共 2h15min）｜[Codeforces Round 1130 (Div. 2)](https://codeforces.com/contest/2272)｜赛后 rating 1344（Pupil）

**做题情况**

- 23:12 A 过（一发；「想了半天」才盯上 $n$ 很小的暴力，落笔 8 分钟写完）
- 23:38 B 过（一发；B.cpp 第一版「连通块」方向写了开头就弃掉，收敛到奇偶）
- 00:13 C 过（一发；前面在 BIT/区间加的弯路里绕了 20 分钟才转向二分贪心）
- 00:19 D 读题——图论盲区，剩 31 分钟跳过
- 00:26 E 只剩模板（「看起来是什么数据结构 / 神秘拆贡献？？」），没落笔

A/B/C 三发全 AC，D/E 赛时未提交。

## A. Maximize One MEX
https://codeforces.com/contest/2272/problem/A

> **题意**：给定 $0 \sim n-1$ 的排列 $a$。你可以**至多一次**交换任意两个位置，然后定义 $f_i=\operatorname{mex}(a_1,\dots,a_i)$。给定 $k$，选择交换（或不交换，输出 $-1$），使 $f_1,\dots,f_n$ 中第 $k$ 大的值最大。多测，$\sum n \le 100$。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int n,t,k,x,y;
int a[maxn];

//总时间 2h15min 剩余时间 1h 45min 1h 37min
//其实想了半天 注意到 n 很小 所以直接写暴力就行了

inline int kmex(){
//	int len = r - l + 1;
//	vector<int> b(n);//唐了 对STL不熟悉 最唐的地方出现了
	vector<int> b;
	vector<int> c(n+1);
//	for(int i=0;i<=n;i++) c[i] = 0;//唐对STL不熟悉 默认就是0
	for(int i=1;i<=n;i++){
		c[a[i]] = 1;
		bool is = 0;
		for(int j = 0;j <= n;j++){
			if(c[j] == 0){
				is = 1;
				b.push_back(j);
				break;//唐
			}
		}
		if(!is) b.push_back(n);
	}
	sort(b.begin(),b.end());
//	cout<<"the size is "<<b.size()<<'\n';
//	for(auto it : b) cout<<it<<' ';
//	cout<<'\n';
	return b[n-1-(k-1)];
}

void solve1(){
	int nx = 0,ny = 0,p = kmex();
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			swap(a[i],a[j]);
			int tmp = kmex();
			if(tmp > p) nx = i,ny = j,p = tmp;
			swap(a[i],a[j]);
		}
	}
	x = nx,y = ny;
	return;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n>>k;
		for(int i=1;i<=n;i++) cin>>a[i];
		x = 0,y = 0;
		solve1();
		if(x == 0 && y == 0) cout<<-1<<'\n';
		else cout<<x<<' '<<y<<'\n';
	}
	
	return 0;	
}
```

### 解读

题目明示 $n \le 100$ 且 $\sum n \le 100$——就是让你暴力：枚举所有 $O(n^2)$ 种交换，每次 $O(n^2)$ 重算前缀 mex 序列取第 $k$ 大，总量 $O(n^4)$ 在 $\sum n \le 100$ 的约束下毫无压力。无数值改善就输出 $-1$。

要点是 `kmex()` 的写法：全局标记 `c[a[i]] = 1` 逐前缀累积，每轮找第一个未出现的值——前缀 mex 天然递增不减，不用重算整个集合。

## B. Frogs Jump
https://codeforces.com/contest/2272/problem/B

> **题意**：$2 \times n$ 网格，每列至少一只蛙（`f` 有蛙 / `o` 空）。移除最少的 $k$ 只蛙，使得剩下的蛙**同时各跳一步**（上下左右、不出界）后，每一行、每一列的蛙数都保持不变。多测，$\sum n \le 2 \times 10^5$。

**代码**（B2.cpp，赛时的 B.cpp 第一版写了「连通块」方向就弃了）

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
string s1,s2;

//总时间 2h15min 剩余时间 1h 12min
//想想一下，每一列青蛙上下横跳 先保证了列的数量不变 
//但是仔细想想 如果左右的变化，一定需要更左面或更右面的青蛙来补充,总忽悠补充不上的，醉意为什么一开始在想想连通块
//但是这样一定最优吗 没错 因为首先要合法
//所以答案就是s1 - s2??这和案例对不上啊
//再想想
/*
2
ff
oo

0
*/
//n=2 两列全上 对跳一下答0 但差=2
//横跳成对 行不变列不变 纯废物 只把竖跳变没
//所以只看竖跳 上单列只能下 下单列只能上 双列换 净0
//我的发 注意到 p个上单 q个下单 差 p - q
//如果是偶横跳抵消 答0
//如果是奇横跳偶数步补不上 删1只 答1
//横跳够不够 就是一开始想的连通块 但被奇偶吸了
//所以 答案就是 （p-q）%2+2 %2 

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    while(t--){
        cin>>n;
        cin>>s1>>s2;
        int p = 0,q = 0;
        for(int i=0;i<n;i++){
            bool u = (s1[i] == 'f');
            bool d = (s2[i] == 'f');
            if(u && !d) p++;
            if(!u && d) q++;
        }
        cout<<(((p - q) % 2 + 2) % 2)<<'\n';
    }
    return 0;
}
```

### 解读

每一列三种形态：双蛙列（上下都有）、上单列、下单列。

- **竖跳是合法的主通道**：蛙在列内上跳/下跳不改变本列蛙数。方向由形态决定——上单列只能往下跳，下单列只能往上跳；双蛙列两只互换，行效应正好相消，净 0。
- **横跳必须成对**：一次横跳会同时改动两列的列计数，单独一次永远配不平；成对的横跳（两列各出一蛙对跳互换）行、列计数都不变，净效应 0——所以横跳只是配平工具，核心矛盾全在竖跳上。
- **行计数的账**：往下跳的只数必须等于往上跳的只数。上单列贡献 $p$ 个「下跳名额」，下单列贡献 $q$ 个「上跳名额」——$p = q$ 时全走竖跳，$k = 0$；差额为偶数时靠成对横跳消化，仍 $k = 0$；差额为奇数时怎么配都剩 1，删掉 1 只蛙补齐奇偶，$k = 1$。

于是结论只有一行：**答案就是 $(p-q) \bmod 2$**。第一版「连通块」方向是彻头彻尾的想多——被样例 `ff/oo → 0` 一巴掌拍醒后，三行收敛到奇偶性。

## C. Yet Another Black Cell Problem
https://codeforces.com/contest/2272/problem/C

> **题意**：数轴上格子从 $0$ 到 $10^9$。给定严格递增的 $n$ 个位置 $a$，要把这 $n$ 格涂黑。给定 $x$，可以额外涂黑 $y \le x$ 个**不在** $a$ 中的格子。操作：选两个格子 $i, j$（$1 \le |i-j| \le k$）涂黑。求最小的 $k$ 使涂黑方案可行。多测，$n \le 2 \times 10^5$。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int n,t;
ll x;
ll a[maxn];

//总时间 2h15min 剩余时间 37 min
//一眼开上去是变化一下统计贡献的方式 可能要进行区间加1这种操作 其实下意识再往bit上面靠
//但是 n 比较小 aj的范围却非常大 1e9
//呃呃呃 怎么搞
//不是 既然是选择 最小的 k还不能是把其他涂黑 那不就是 min(a[i] - a[i-1]) 然后再考虑0 <= y <= x的影响???
//我刚刚在想什么？？卧槽 我是个猪逼吧
//卧槽 等一下 那答案不就有了单调性和贪心验证的单调性吗
//因为 可以 原定一个 k 把它作为插入值 每次验证都是 O(n)
//O(nlog(1e9))的一个做法 卧槽春二分贪心 叫吧
//

//bool check(ll k){//过于严格 没有考虑有的不用插入点 直接暴力过就行了
//    ll p = 0;
//    for(int i=2;i<=n;i++){
//        ll d = a[i] - a[i-1];
//        p += (d - 1) / k;
//        if(p > x) return 0;
//    }
//    return p <= x;
//}

bool check(ll k){
    vector<ll> v;
    for(int i=1;i<=n;i++){
        bool l = (i > 1 && a[i] - a[i-1] <= k);
        bool r = (i < n && a[i+1] - a[i] <= k);
        if(!l && !r) v.push_back(a[i]);
    }
    int c = v.size(),d = 0;
    for(int i=0;i + 1 < c;){
        if(v[i+1] - v[i] <= 2*k){
			d++;
			i += 2;
		}
        else i++;
    }
    return c - d <= x;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>t;
    while(t--){
        cin>>n>>x;
        for(int i=1;i<=n;i++) cin>>a[i];
        ll l = 1,r = 1e9,ans = 1e9;
        while(l <= r){
            ll mid = (l + r) / 2;
            if(check(mid)){ 
				ans = mid;
				r = mid - 1;
			}
            else l = mid + 1;
        }
        cout<<ans<<'\n';
    }

    return 0;
}
```

### 解读

二分 $k$ + $O(n)$ 贪心 check。check 的语义：**孤立点**（与左右相邻 $a$ 格间距都 $> k$ 的格子）没法跟别的 $a$ 格直接配对，必须花 1 个额外格名额单独涂黑；间距 $\le k$ 的相邻 $a$ 格一次操作直接配对，零预算。**间距 $\le 2k$ 的两个孤立点可以共用一个中点额外格**——中点到两边都 $\le k$，两次操作各带它一次，两格就都涂上了，预算只花 1。贪心把能配对的孤立点两两配对，数出最少预算消耗与 $x$ 比较。

赛时弯路：一开始往 BIT/区间加的方向靠（被「涂黑」的表象带偏），后来意识到这题的形状就是「最小化最大值 → 二分答案 + 贪心判定」的模板题——转回来之后几分钟写完，一发过。

## D. Connecting the Conflicts（未提交）
https://codeforces.com/contest/2272/problem/D

> **简要题意**：$k$ 棵树组成的森林，加 $k-1$ 条边连成一棵树，使新树的最大独立集最大，输出加边方案。$\sum k, \sum n \le 2 \times 10^5$。

**现状**：剩 31 分钟读题，图论盲区（森林连树 + 最大独立集构造——代码注释原话「可能以前见过独立集最大化这种问题 但是我现在是真的一点点都不擅长」），文件里只留了读入骨架、没提交；E.cpp 同样只剩空模板——「看起来是什么数据结构 / 神秘拆贡献？？」方向没锁死。

---

## 赛后总结

**成绩**：A/B/C 三发全 AC（23:12 / 23:38 / 00:13），rating 1344（Pupil）。D/E 未提交。

**做得好的**：

- A 「想了半天」识破「$n$ 很小直接暴力」，落笔 8 分钟写完，一发过。
- B 第一版「连通块」方向写了个开头就察觉不对，收敛到奇偶结论只用了十几分钟——弃得果断。
- C 从 BIT 弯路转回「二分答案 + 贪心判定」后几分钟写完一发过，被划掉的过严 check 版本也留了案底（把每个大间隔独立按 $(d-1)/k$ 计费，没考虑一侧 $a$ 格能直接配对、间隔只需单侧插点的情况）。

**不足**：

1. **D 图论盲区**：森林连树使最大独立集最大——这类构造/贪心结论题（合并两棵子树的 MIS 增量是 $O(1)$ 可算的）完全没思路，31 分钟跳过不冤。列入补题。
2. **E 方向没锁死**：「拆贡献」的直觉对了但没推下去。相比 D 是彻底的盲区，E 更像「差一层窗户纸」——赛后值得独立补。
3. 两场连续（ABC481 + 本场）的共性：**中后段的题全部倒在知识储备而不是代码能力**——D/E/F/G 四道题里只有 F 是时间不够，其余都是方向问题。图论构造、多项式计数、线段树上的拆贡献，三个坑按序补。