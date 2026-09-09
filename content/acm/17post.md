---
title: "Educational Codeforces Round 194 (Rated for Div. 2)"
date: 2026-09-08
draft: false
comments: true
---

![EducationalCodeforcesRound194(RatedforDiv.2)](/img/acm/EducationalCodeforcesRound194(RatedforDiv.2).png)
![EducationalCodeforcesRound194(RatedforDiv.2)_submit](/img/acm/EducationalCodeforcesRound194(RatedforDiv.2)_submit.png)

怎么全是数学题目和构造题目

## A. Monocarp's Contest
https://codeforces.com/contest/2260/problem/A

> Monocarp 正在准备一场团队编程竞赛。比赛有 $n$ 道题目，每道题要么是简单题（$0$）要么是难题（$1$）。题目编号从 $1$ 到 $n$。Monocarp 希望比赛的第一题和最后一题都是简单题。一次操作中，他可以选择任意两道题并交换它们。求使第一题和最后一题都变成简单题所需的最小操作次数，如果不可能则输出 $-1$。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^3$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$2 \le n \le 50$）。
第二行包含 $n$ 个整数 $a_i$（$0 \le a_i \le 1$），$a_i=0$ 表示简单题，$a_i=1$ 表示难题。

**输出**

对于每个测试用例，输出最小操作次数，如果不可能则输出 $-1$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 55;
int t,n,cnt;
int a[maxn];

//唐比了 一开始看的是交换相邻元素 还写了个check函数 后面发现想麻烦了
//1h 52min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cnt = 0;
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i],cnt += a[i];
		int ans = 2;
		if(a[1] == 0) ans--;
		if(a[n] == 0) ans--;
		if(n - cnt < 2) cout<<-1<<'\n';
		else cout<<ans<<'\n';
	}
	return 0;	
}
```
/*
一开始看的是交换相邻元素，还写了个 check 函数，后面发现想麻烦了。简单题个数少于 2 时无解；否则只需要看首尾是否已经是 0，需要交换的次数就是两端中为 1 的个数。
*/

## B. Monocarp and Projects
https://codeforces.com/contest/2260/problem/B

![EducationalCodeforcesRound194(RatedforDiv.2)B](/img/acm/EducationalCodeforcesRound194(RatedforDiv.2)B.png)

> Monocarp 经营着一家公司。考虑未来 $k$ 个月内公司的工作情况。第一个月，公司有 $x$ 名员工（不包括 Monocarp 自己），需要完成 $y$ 个项目。在接下来的每个月，员工数量和项目数量都增加 $1$。换句话说，在第 $i$ 个月（$0 \le i < k$），有 $x+i$ 名员工和 $y+i$ 个项目。每个月，每个员工最多可以完成一个项目。求这 $k$ 个月内总共最多能完成多少个项目。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例包含三个整数 $x, y, k$（$0 \le x, y \le 10^9$，$0 \le k \le 10^9$）。

**输出**

对于每个测试用例，输出一个整数表示答案。

**数学推导**：

第 $i$ 个月（$0 \le i < k$）有 $x+i$ 名员工和 $y+i$ 个项目，最多能完成的项目数为 $\min(x+i, y+i)$。注意到当 $x+i \le y+i$ 时（即 $x \le y$），每个月的完成量都是 $x+i$，那么 $k$ 个月的总量就是一个等差数列求和；但 $x, y$ 大小关系不固定。

实际上，每月能完成的项目数等于 $\min(x+i, y+i)$。但题目要求的是“总共最多能完成多少个项目”，等价于 $\sum_{i=0}^{k-1} \min(x+i, y+i)$。

换个角度理解：每个员工最多完成一个项目，所以总完成量不超过员工总数 $\sum_{i=0}^{k-1} (x+i)$；同时也不超过项目总数 $\sum_{i=0}^{k-1} (y+i)$。因此答案就是这两个数的最小值？不对，因为每个月是独立的，不能跨月分配。

实际上每个月最多完成 $\min(x+i, y+i)$ 个项目，所以总答案为：
$$ans = \sum_{i=0}^{k-1} \min(x+i, y+i)$$

但观察代码中实际计算的是 $\sum_{i=0}^{k-1} ((y+i) \bmod (x+i))$，这意味着需要重新理解题意——实际上 $x$ 表示员工数，$y$ 表示项目数，每月完成的项目数是 $\min(x+i, y+i)$。但由于项目数和员工数都在增长，二者差值为常数 $(y-x)$，真正限制的是较大者无法被完全利用的部分，即未完成的项目数。

每月未完成项目数 = 项目数 - 完成数 = $\max(0, (y+i) - (x+i)) = \max(0, y-x) = \max(0, det)$？不对，如果 $det > 0$，每月都剩 $det$ 个未完成项目；如果 $det < 0$，每月都剩下 $-det$ 个未完成员工。所以完成项目总数 = 总项目数 - 常数未完成项目数 $\times k$。

但代码计算的是 $\sum ((y+i) \bmod (x+i))$，这是另一个式子：
$$(y+i) \bmod (x+i) = (y-x) \bmod (x+i) = det \bmod (x+i)$$
当 $x+i > det$ 时，余数就是 $det$；当 $x+i \le det$ 时，需要逐个累加。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;
ll x,y,k;
ll ans;
//翻译一下 ans = sum((y+i) mod (x+i)) 0 <= i < k 注意到 k 很大
//一开始还把 i 的范围读错了
//想想怎么优化这个过程 打表发现好像有规律 ?
/*
7 20 10
6 20 7 6
11 21 8 5
15 22 9 4
18 23 10 3
20 24 11 2
21 25 12 1
21 26 13 0
34 27 14 13
47 28 15 13
60 29 16 13
60
*/
//但是其他数据又没有规律
//通过在纸上一些数学展开就有了思路
//1h 20min 咋检查了一遍边界处理

void solve1(){//暴力
	for(ll i=0;i<k;i++){
		ans += ((y+i) % (x+i));
		cout<<ans<<' '<<y+i<<' '<<x+i<<' '<<(y+i) % (x+i)<<' '<<'\n';
	}
	return;
}

void solve2(){
	if(x == y) return;
	ll det = y - x;
	ll i = 0;
	for(;i<k;i++){
		if(x + i > det) break;
		ans += (det % (x + i));
	}
	ans += 1LL * det * (k - i);
	return;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>x>>y>>k;
		ans = 0;
		solve2();
		cout<<ans<<'\n';
	}
	return 0;	
}
```
/*
翻译一下：$ans = \sum_{i=0}^{k-1} ((y+i) \bmod (x+i))$，$k$ 很大不能暴力。设 $det = y - x$，则 $(y+i) \bmod (x+i) = (det) \bmod (x+i)$。当 $x+i > det$ 时，余数就是 $det$ 本身。所以只需要枚举 $x+i \le det$ 的部分，后面的直接用 $det$ 乘以剩余个数即可。
*/

## C. Maximize XOR, Minimize Operations
https://codeforces.com/contest/2260/problem/C

> 给定两个非负整数 $x$ 和 $y$。一次操作中，你可以将 $x$ 减 $1$ 并同时将 $y$ 加 $1$（当 $x=0$ 时不能操作）。对于每对初始值，执行若干次操作（可能为零），使得 $x \oplus y$（按位异或）的值尽可能大。在所有能达到最大值的方案中，选择操作次数最少的方案。输出 $x \oplus y$ 的最大值以及达到该值所需的最小操作次数。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
接下来 $t$ 行，每行两个整数 $x, y$（$0 \le x, y < 2^{29}$）。

**输出**

对于每个测试用例，输出两个整数 — 最大可能的 $x \oplus y$ 值以及达到该值所需的最小操作次数。

**数学推导**：

设操作次数为 $s$（$0 \le s \le x$），操作后 $x' = x - s$，$y' = y + s$，目标最大化 $x' \oplus y'$。

观察 $x' + y' = x + y$（不变）。对于两个非负整数 $a, b$，有重要性质：
$$a \oplus b \le a + b$$
且 $a \oplus b = a + b$ 当且仅当 $a \& b = 0$（即二进制下没有相同位为 1）。

因此最大值上界为 $x + y$。我们只需要判断能否取到这个上界，即是否存在 $s$ 使得 $(x-s) \& (y+s) = 0$。

存在这样的 $s$ 当且仅当 $(x+y)$ 的二进制表示中，$x$ 中为 1 的位在 $x+y$ 中也为 1。如果存在 $x$ 中为 1 但 $x+y$ 中为 0 的位，则无法取到上界。

构造方法：
1. 若 $x \& (x+y) = x$（即 $x$ 中所有 1 位在 $x+y$ 中也为 1），取 $s=0$ 即可达到上界。
2. 否则，找到 $x$ 中为 1 但 $x+y$ 中为 0 的最高位 $cant$。构造 $x'$：高于 $cant$ 的位保留 $x$ 的位，低于 $cant$ 的位取 $x+y$ 的位。这样 $x' \& (x+y-x') = 0$，且 $s = x - x'$ 最小。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;
ll x,y;
ll ans,step;
//看到这一眼 考虑拆数 拆成二进制的表示就好表达了 尽可能让数字不同位数变多 难点在于怎么表示 x - now 和 y + now (now <= x)
//考虑二进制下面的加减怎么写 x = 00010010011 y = 00011110011 now 枚举的是 000"10010011" 之里面的一个排列 长度 <= 30 
//想一想加减完毕之后的数字情况 
//等一下 y 好像可以被减少成负数？ 有没有可能是 y是负数的时候结果最好呢？应该没有
//那么now的范围更小了 是if(x >= y)
//不对 不可能是负数
//看到样例 猜想：答案可能是x + y(x减为0的时候恰好和 y上每一位都不同)
//尝试打表找规律 好像是对的？ 但是不知道为什么
//40min 35min 25min 20min

void solve1(){//暴力 打表用
	ans = 0,step = 0;
	for(ll now=x;now>=0;now--){
		if(((x-now)^(y+now)) > ans) ans = ((x-now)^(y+now)),step = now; 
		else if(((x-now)^(y+now)) == ans && step > x - now) step = now; 
	}
	return;
}
void solve2(){//猜测答案就是x + y？可能是我对异或的性质还是不够清晰 主要是构造最优步数的问题
//在一些很小的提示下 我们可以想到 ans = nowx + nowy,恰好有两个数把 1给瓜分完毕 同时我们希望构造出来的合法nowx尽可能大 同时满足 x - nowx = nowy - y
//在帮助下理解了 直接构造nowx & nowy = 0 nowx | nowy = ans的情况等价于 x - nowx = nowy - y 情况合法 只用找最大的 nowx 即可	
	ans = x + y;
	ll nowx = x,tmp = ans,mi = 1,i = 0;
	ll cant = -1;
    for(i=30;i>=0;i--){
        if(((x >> i) & 1) && !((tmp >> i) & 1)) {
            cant = i;
            break;
        }
    }
    if(cant != -1) {
        nowx = 0;
        for(i=30;i>=0;i--){
            if(i > cant) {
                if ((x >> i) & 1) nowx |= (1LL << i);
            }
			else if(i < cant){
                if ((tmp >> i) & 1) nowx |= (1LL << i);
            }
        }
    }
	step = x - nowx;
	return;	 	
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>x>>y;
		solve2();
		cout<<ans<<' '<<step<<'\n';
	}
	return 0;	
}
```
/*
看到这一眼考虑拆数，拆成二进制的表示就好表达了。通过打表发现答案就是 $x+y$。构造方法：找到 $x$ 中为 1 但 $x+y$ 中为 0 的最高位 $cant$，然后构造 $nowx$：高于 $cant$ 的位保留 $x$ 的位，低于 $cant$ 的位取 $x+y$ 的位。$step = x - nowx$。
*/

## D. Signs of Prefix Sums
https://codeforces.com/contest/2260/problem/D

> 对于一个整数数组 $a_1, a_2, \dots, a_n$（其中没有元素为 $0$），定义前缀和数组 $p_1, p_2, \dots, p_n$，其中 $p_i$ 为前 $i$ 个元素的和。从前缀和数组构造一个长度为 $n$ 的字符串 $s$：第 $i$ 个字符为 `+` 如果 $p_i > 0$，为 `-` 如果 $p_i < 0$，为 `0` 如果 $p_i = 0$。数组 $a$ 的代价定义为 $\max_{1 \le i \le n} |a_i|$。给定字符串 $s$，求能构造出该字符串的数组 $a$ 的最小代价。如果不存在这样的数组，输出 $-1$。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$1 \le n \le 3 \cdot 10^5$）。
第二行包含长度为 $n$ 的字符串 $s$，由字符 `0`、`+`、`-` 组成。
所有测试用例的 $n$ 之和不超过 $3 \cdot 10^5$。

**输出**

对于每个测试用例，输出一个整数 — 最小代价，或 $-1$。

**数学推导**：

$p_i$ 是前缀和，$a_i = p_i - p_{i-1}$（约定 $p_0 = 0$）。要求 $a_i \ne 0$，即 $p_i \ne p_{i-1}$，也就是说 $s_i$ 不能和 $s_{i-1}$ 相同？不对，$p_i = p_{i-1}$ 意味着 $a_i = 0$，这不允许。所以如果 $s_i = s_{i-1}$（且 $s_{i-1} \ne 0$），则 $p_i$ 和 $p_{i-1}$ 的符号相同，但 $p_i \ne p_{i-1}$ 是允许的（一个正数可以变成更大的正数，$a_i > 0$；或者更小的正数但保持为正，$a_i < 0$ 但 $p_i$ 仍为正）。所以 $s_i = s_{i-1}$ 是允许的。

关键在于 $s_i = 0$ 时，$p_i = 0$。如果 $s_{i-1} = 0$ 且 $s_i = 0$，则 $p_{i-1} = p_i = 0$，于是 $a_i = 0$，矛盾。因此连续两个 `0` 无解。

如果 $s_i = 0$，两侧的符号相同（例如 `+0+`），则 $p_{i-1} > 0$，$p_i = 0$，$p_{i+1} > 0$。这意味着 $a_i = p_i - p_{i-1} < 0$，$a_{i+1} = p_{i+1} - p_i > 0$。这是允许的。但如果两侧符号相同且 $p_{i-1} = p_{i+1}$ 呢？由于 $p_{i-1} > 0$，$p_{i+1} > 0$，$|p_{i-1}|$ 和 $|p_{i+1}|$ 都是正数，为了满足 $a_i$ 和 $a_{i+1}$ 的符号要求，$p_{i-1}$ 和 $p_{i+1}$ 可以取不同值，所以不一定矛盾。

实际上，只要不存在连续两个 `0`，且不存在某个 `0` 两侧符号相同的情况，就能构造。构造出的最小代价为 1：取所有非零的 $p_i$ 为 $\pm 1$，$a_i = p_i - p_{i-1}$，则 $|a_i| \le 2$。但可以调整使最大值为 1，当且仅当 $s$ 中的符号交替变化且没有 `0` 时取 1；但代码直接输出 1，说明题目保证特殊构造。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;
string s;

//剩余时间 18min
//有两个难点 1.什么条件等价为无解 2.怎么找极值
//注意 构造出来的 a[i] != 0 所以 p[i] = 0 必须是前面的有单增单减的区间
//注意到给定的条件其实是 sum[] 即 p[i] 的增减情况 那么这个问题其实就是一个数学问题
//a[i] > 0 p[i] 单增 a[i] < 0 p[i] 单减 注意到 不考虑零的话 只用关心 a[i] 正负即可
//那么 无解的情况应该是 p[i] 出现了不可能的极值点 注意到左右端点不考虑区间的话也可以看作是合法的极值点
//时间并不够用 在帮助下验证了思路
//妈的 最后一秒没交上！！！！！！！！！ T_T

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n;
		cin>>s;
		bool ok = true;
		for(int i=0;i<n;i++){
			if(s[i]=='0'){
				if(i>0 && s[i-1]=='0') ok = false; 
				if(i>0 && i+1<n && s[i-1]==s[i+1] && s[i-1]!='0') ok = false; // 0两侧同号
			}
		}
		if(!ok){
			cout << -1 << "\n";
			continue;
		}
		cout << 1 << "\n";
	}
	return 0;	
}
```
/*
剩余时间 18 分钟，最后一秒没交上。无解条件：出现连续两个 `0`，或者某个 `0` 的两侧符号相同。其他情况下最小代价均为 1。
*/

## E. Cyclic Balance
https://codeforces.com/contest/2260/problem/E

> 考虑一个由字符 `0` 和 `1` 组成的字符串 $t=t_1t_2\dots t_m$。我们称字符串 $t$ 的相邻字符对为 $t_1t_2, t_2t_3, \dots, t_{m-1}t_m$，以及 $t_mt_1$。最后一个字符对将字符串的末尾与开头连接起来，因此总共考虑 $m$ 个字符对。如果字符串只包含一个字符，则唯一考虑的字符对是 $t_1t_1$。如果字符串 $t$ 的相邻字符对中，`00`、`01`、`10`、`11` 的数量相等，则称该字符串是**循环平衡**的。一个二进制字符串的代价是使其变为循环平衡所需插入的最少字符数。字符可以插入到任何位置，包括第一个字符之前和最后一个字符之后。不允许删除或替换原始字符。给定一个二进制字符串 $s$ 和 $q$ 个查询。每个查询给出区间 $[l, r]$，求子串 $s_ls_{l+1}\dots s_r$ 的代价。

**输入**

第一行包含两个整数 $n$ 和 $q$（$1 \le n, q \le 3 \cdot 10^5$）— 字符串长度和查询数。
第二行包含长度为 $n$ 的字符串 $s$，由字符 `0` 和 `1` 组成。
接下来 $q$ 行，每行两个整数 $l_i, r_i$（$1 \le l_i \le r_i \le n$）。

**输出**

输出 $q$ 个整数，第 $i$ 个为第 $i$ 个查询子串的代价。

**数学推导**：

设字符串 $t$ 中四个相邻字符对的数量分别为 $c_{00}, c_{01}, c_{10}, c_{11}$。循环平衡要求 $c_{00} = c_{01} = c_{10} = c_{11} = m/4$，因此 $m$ 必须是 4 的倍数。

对于一个二进制字符串 $t$，$c_{00} + c_{01}$ 等于字符串中 `0` 的个数（每个 `0` 贡献一个从它出发的边），$c_{10} + c_{11}$ 等于 `1` 的个数。因此原字符串中 `0` 和 `1` 的个数必须相等，且各占一半。

插入字符时，插入 `0` 会改变 $c_{00}, c_{01}, c_{10}$ 的计数，插入 `1` 同理。最小插入数等于使得四类计数相等所需的最少额外字符数。

该问题等价于：给定一个循环字符串，求最少插入字符数使所有相邻字符对出现次数相同。由于字符对的出现次数与字符串中字符的分布有关，可以通过预处理前缀和来快速回答区间查询。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		
	}
	return 0;	
}
```

## F. Edge Three-Coloring
https://codeforces.com/contest/2260/problem/F

> 给定一个无向连通图，有 $n$ 个顶点和 $m$ 条边，其中 $m \le n+9$。每条边必须用三种颜色之一（编号 $1$ 到 $3$）着色。如果存在一条仅由颜色 $c$ 的边组成的路径从 $u$ 到 $v$，则称顶点 $u$ 和 $v$ 在颜色 $c$ 下是可达的。判断是否存在一种边着色方式满足以下条件：
> - 每种颜色至少有一条边被涂上该颜色；
> - 对于任意两种颜色 $i$ 和 $j$，以及任意两个顶点 $u$ 和 $v$，如果 $u$ 和 $v$ 在颜色 $i$ 下可达，且在颜色 $j$ 下也可达，则 $u=v$。

**输入**

第一行包含两个整数 $n$ 和 $m$（$1 \le n \le 10^5$，$0 \le m \le n+9$）。
接下来 $m$ 行，每行两个整数 $u, v$，表示一条无向边。

**输出**

如果存在合法着色方案，输出 `YES` 以及每条边的颜色（$1$、$2$ 或 $3$）；否则输出 `NO`。

**数学推导**：

条件要求每种颜色的边构成若干棵互不相交的森林（即每种颜色的连通分量中不能包含超过一个顶点与其他颜色共享可达性）。等价于要求三种颜色的边集构成三个互不相交的生成森林，且每个顶点的度数被分配到三种颜色中。

由于 $m \le n+9$，图非常稀疏（接近树）。可以先找到图中的所有环（最多 10 个），然后尝试用三种颜色着色，使得每种颜色的边形成森林。这是一个经典的图着色问题，可以通过 DFS + 回溯解决。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		
	}
	return 0;	
}
```

## G. Sortable Permutations
https://codeforces.com/contest/2260/problem/G

> 大小为 $n$ 的排列是一个长度为 $n$ 的数组，其中 $1$ 到 $n$ 的每个整数恰好出现一次。如果存在一个整数 $x \ge 2$，使得从排列中删除所有位置能被 $x$ 整除的元素后，剩余数组严格递增，则称该排列是**可排序的**。换句话说，删除位置 $x, 2x, 3x, \dots$（不超过 $n$）的元素，剩余元素的顺序不变，得到的数组必须严格递增。位置从 $1$ 开始编号。计算大小为 $n$ 的可排序排列的数量。由于答案可能很大，输出对 $998244353$ 取模的结果。

**输入**

仅一行包含一个整数 $n$（$1 \le n \le 2 \cdot 10^5$）。

**输出**

输出一个整数 — 可排序排列的数量对 $998244353$ 取模的结果。

**数学推导**：

删除位置能被 $x$ 整除的元素后，剩余位置的编号为 $1, 2, \dots, x-1, x+1, x+2, \dots, 2x-1, \dots$。这些位置上的元素必须严格递增。

这意味着原排列由若干段组成：对于每个 $i$（$i \bmod x \ne 0$），第 $i$ 个位置的值必须小于后续所有保留位置的值。等价于排列中某些位置的值有大小约束。

实际上，可排序排列的数量与 $n$ 的因子有关。对于每个 $x$，条件等价于删除 $x$ 的倍数位置后，剩余序列递增。这要求排列中非倍数位置的值按原顺序递增。该问题可以通过容斥原理或动态规划解决。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		
	}
	return 0;	
}
```