---
title: "AtCoder Beginner Contest 463"
date: 2026-07-07
draft: false
---

## A
https://atcoder.jp/contests/abc463/tasks/abc463_a
#### 问题陈述

有一幅宽度为 $X$ 像素，高度为 $Y$ 像素的图像。请判断宽度与高度之比是否为 $16$ 与 $9$ ，即是否为 $X:Y=16:9$ 。
- $1 \leq X \leq 1000$
- $1 \leq Y \leq 1000$
- 所有输入值均为整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
double x,y,tempa = 16.0,tempb = 9.0;
double a = double(tempa/tempb),b;
int main(){
	cin>>x>>y;
	b = double(x/y);
	if (a == b) cout<<"Yes";
	else cout<<"No";
	return 0;
}
```
## B
https://atcoder.jp/contests/abc463/tasks/abc463_b
#### 问题陈述

高桥正在尝试预订火车座位。

他考虑预订的候选列车有 $N$ 列，编号为 $1, 2, \dots, N$ 。每列火车有五列座位，分别称为 A 列、B 列、C 列、D 列和 E 列。

每列火车的当前座位可用性信息为字符串 $S_1, S_2, \dots, S_N$ 。这里， $S_1, S_2, \dots, S_N$ 的长度都是 $5$ ，列车 $i$ 的 A 列至 E 列分别对应 $S_i$ 的第一至第五个字符。如果该字符为 `o` ，则相应列中有空位；如果该字符为 `x` ，则相应列中没有空位。

高桥希望在第 $X$ 列保留一个座位，其中 $X$ 是 `A` ， `B` ， `C` ， `D` ， `E` 中的一个。求至少一列火车的 $X$ 列中是否有空位。

- $N$ 是介于 $1$ 和 $100$ （含）之间的整数。
- $X$ 是 `A` 、 `B` 、 `C` 、 `D` 、 `E` 中的一个。
- $S_i$ 是长度为 $5$ 的字符串，由 `o` 和 `x` 组成。

```cpp
#include <bits/stdc++.h>
using namespace std;
int n;
char a;
string s;
bool ans = 0;
int main(){
	cin>>n>>a;
	for(int i=1;i<=n;i++){
		cin>>s;
		if(a == 'A' && s[0] == 'o') ans = 1;
		if(a == 'B' && s[1] == 'o') ans = 1;
		if(a == 'C' && s[2] == 'o') ans = 1;
		if(a == 'D' && s[3] == 'o') ans = 1;
		if(a == 'E' && s[4] == 'o') ans = 1;
	}
	if(ans == 1) cout<<"Yes";
	else cout<<"No";
	
	return 0;
}
```

## C
https://atcoder.jp/contests/abc463/tasks/abc463_c
#### 问题陈述

目前，会议室里有 $N$ 个高桥（Takahashi）。高桥在一间会议室里。身高为 $H _ i$ 的 $i$ （ $(1\le i\le N)$ ）高桥将于 $L _ i$ 离开会议室。高桥的身高为 $H _ i$ ，将在 $L _ i$ 分钟后离开会议室。高桥一旦离开会议室，就再也不会回来了。

你有 $Q$ 个问题，请按顺序回答。对于 $i$ \-th $(1\le i\le Q)$ 查询，你会得到一个整数 $T _ i$ ，所以请找出从现在起 $T _ i+\dfrac12$ 分钟后在房间里的高桥的最大身高。在这个问题的约束条件下，可以保证从现在起 $T _ i+\dfrac12$ 分钟后，至少有一个高桥在房间里。

- $1\le N\le3\times10 ^ 5$
- $1\le H _ i\le10 ^ 9\ (1\le i\le N)$
- $1\le L _ 1\le L _ 2\le\cdots\le L _ N\le10 ^ 9$
- $1\le Q\le3\times10 ^ 5$
- $0\le T _ i\lt L _ N\ (1\le i\le Q)$
- 所有输入值均为整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const unsigned int maxx = 300001;
struct gaoqiao{
	ll h,l;
}a[maxx];
int n,q;
double t[maxx];
ll tall[maxx];
bool gaoqiaotall(const gaoqiao &a,const gaoqiao &b){
//	if(a.h != b.h) return a.h < b.h;
//	else return a.l < b.l;
	if(a.l != b.l) return a.l < b.l;
	else return a.h < b.h;
}

bool check(int temp,double t){
	return double(a[temp].l) > (t + 0.5);
}
void pre(){
	tall[n] = a[n].h;//答案在右面 倒序处理 
	for(int i=n-1;i>=1;i--) tall[i] = max(tall[i+1],a[i].h);
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i].h>>a[i].l;
	sort(a + 1,a + n + 1,gaoqiaotall);
//	for(int i=1;i<=n;i++) cout<<a[i].h<<' '<<a[i].l<<endl;
	cin>>q;
//	for(int i=1;i<=q;i++) cin>>t[i];
////	int r = n,l = 0,mid = 0;
//	for(int i=1;i<=q;i++){
//		for(int j=n;j>=1;j--){
//			if(double(a[j].l) > (t[i] + 0.5)){
//				cout<<a[j].h<<endl;
//				break;
//			}		
//		}
//	}
	pre();
	//二分可以优化查找 到 qlog n 的 复杂度  对下标二分 
	//因为 两个变量只能保证其中一个有序 所以要提前处理身高便于快速获取 temp 之后的 最大身高 
	for(int i=1;i<=q;i++) cin>>t[i];
	int r = n,l = 0,mid = 0,temp = 0;
	ll ans = 0;
	for(int i=1;i<=q;i++){
		r = n,l = 1,mid = 0,temp = n;
		while(l <= r){
			mid = (l + r) / 2;
			if(check(mid,t[i])) temp = mid,r = mid - 1;
			else l = mid + 1;
		}
		ans = tall[temp];
		cout<<ans<<endl;
	}
	return 0;
}
```

## D
https://atcoder.jp/contests/abc463/tasks/abc463_d
#### 问题陈述

在一条数线上有 $N$ 块布。 $i$ /-- $(1\le i\le N)$ 块布覆盖了直线上的区间 $\lbrack L _ i,R _ i\rbrack$ 。直线上的一点可能被两块或更多块布覆盖，也可能没有被任何一块布覆盖。

如果直线上的某一点同时被两块布覆盖，则称两块布重叠。

对于不重叠的两块布，其**距离**定义如下：

- 一块布覆盖的所有点 $p$ 和另一块布覆盖的所有点 $q$ 上 $|p-q|$ 的最小值。

对于没有两块布重叠的 $K$ 块布，将其**分**定义为所有这些布对之间的最小距离。从 $N$ 块布中选择 $K$ 块布，使所选的布中没有两块重叠，求可能的最大得分。

如果无法选择 $K$ 这样的布，则输出 `-1` 。

- $2\le K\le N\le2\times10 ^ 5$
- $0\le L _ i\lt R _ i\le10 ^ 9\ (1\le i\le N)$
- 所有输入值均为整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const unsigned int maxx = 200001;
int n,k;
struct cloth{
	ll l,r;
}a[maxx];
//经典的二分 + 贪心构造判断是否可以满足这个分数 
bool cmp (const cloth &a,const cloth &b){
	if(a.r != b.r) return a.r < b.r;
	else return a.l < b.l;
}
bool check(ll d){
	int cnt = 1,temp = 1;
	for(int i=2;i<=n;i++){
		if(a[i].l - a[temp].r >= d) cnt++,temp = i;
	}
	return cnt >= k;
}

int main(){
	cin>>n>>k;
	for(int i=1;i<=n;i++) cin>>a[i].l>>a[i].r;
	sort(a+1,a+1+n,cmp);
	ll tl = -1,tr = 1000000000,mid = 0,ans = -1;
	while(tl <= tr){
		mid = (tl + tr)/2 ;
		if(check(mid)) ans = mid,tl = mid + 1;
		else tr = mid - 1;
	}
	if(ans > 0) cout<<ans;
	else cout<<-1;
	return 0;
}
```

后三题没有时间做了，感觉相当有挑战性，这真的是ABC吗？（害怕）

## E

https://atcoder.jp/contests/abc463/tasks/abc463_e 

类图论，加强的最短路

#### 问题陈述

AtCoder 国家有 $N$ 座城市和 $M$ 条道路。 $i$ 条道路 $(1\le i\le M)$ 双向连接 $u _ i$ 和 $v _ i$ 两个城市，从一个城市到另一个城市只需 $T _ i$ 分钟。

此外，每个城市都安装了曲速门，使用曲速门可以在 $X _ i+X _ j+Y$ 分钟内从城市 $i\ (1\le i\le N)$ 到达城市 $j\ (1\le j\le N)$ 。

国内没有其他城市之间的交通方式。

请为每个 $k=2,3,\ldots,N$ 解出下面的问题：

- 求从城市 $1$ 到城市 $k$ 所需的最短时间。

在同一城市，从一条道路或翘曲门到另一条道路或翘曲门所需的时间可以忽略不计。

- $2\le N\le2\times10 ^ 5$
- $0\le M\le2\times10 ^ 5$
- $1\le u _ i\lt v _ i\le N\ (1\le i\le M)$
- $1\le T _ i\le10 ^ 9\ (1\le i\le M)$
- $1\le X _ i\le10 ^ 9\ (1\le i\le N)$
- $1\le Y\le 10 ^ 9$
- 所有输入值均为整数。

## F

https://atcoder.jp/contests/abc463/tasks/abc463_f 

数论，看起来要分类讨论

#### 问题陈述
一场有 $2N$ 玩家参加的锦标赛正在举行。从现在开始，每个球员将只打一场比赛。

在剩余的 $N$ 场比赛中， $i$ 第 $(1\le i\le N)$ 场比赛在第 $(2i-1)$ 名和第 $2i$ 名玩家之间进行。

在每场比赛中，两名选手中的一名获胜，另一名失败。对于每场比赛，哪个玩家获胜是独立确定的，并且每个玩家获胜的概率为 $\dfrac12$ 。

在最后一场 $N$ 比赛开始之前，第 $i$ 名 $(1\le i\le2N)$ 玩家已经赢了 $A _ i$ 次。

所有比赛结束后，从获胜次数最多的选手中选出冠军。均匀地随机地并且独立于先前的匹配结果。

对于第一个、第二个、第 $\ldots$ 个、第 $2N$ 个玩家中的每一个，求出该玩家成为冠军的概率（模 $998244353$ ）。

##### 模 $998244353$ 的概率定义：
可以证明所求的概率总是一个有理数。

而且，在该问题的约束条件下，可以证明当有理数表示为不可约分数 $\frac{P}{Q}$ 时，我们有 $Q {{}\not\equiv{}} 0 \pmod{998244353}$ 。

因此，存在唯一的整数 $R$ 满足 $R \times Q \equiv P \pmod{998244353}, 0 \leq R \lt 998244353$ 。找到这个 $R$ 。

$1\le N\le2\times10 ^ 5$ - $0\le A _ i\lt2N\ (1\le i\le 2N)$ -所有输入值均为整数。

## G

https://atcoder.jp/contests/abc463/tasks/abc463_g 

数论加DP，好像还要求个组合数

#### 问题陈述
给定一个正整数 $N$ 和一个整数 $X$ 。

高桥位于一条数轴上的坐标 $0$ 处。

他现在将执行以下移动 $N$ 次:-当位于坐标 $x$ 时，以相等的概率选择坐标 $x-1$ 或坐标 $x+1$ 并移动到那里。

跨 $N$ 移动的目的地选择都是独立的。设 $x'$ 为所有 $N$ 移动后的坐标。求 $|x'-X|$ 的期望值，模 $998244353$ 。

您将获得 $T$ 个测试用例来解决每个问题。

##### 期望值模 $998244353$ 的定义
可以证明所求的期望值总是一个有理数。

此外，在该问题的约束下，可以证明当表示为不可约分数 $\frac{P}{Q}$ 时，我们有 $Q {{}\not\equiv{}} 0 \pmod{998244353}$ 。

因此，存在唯一的整数 $R$ 满足 $R \times Q \equiv P \pmod{998244353}, 0 \leq R &lt; 998244353$ 。找到这个 $R$ 。

$1 \leq T \leq 2 \times 10^5$ - $1 \leq N \leq 2 \times 10^5$ - $|X| \leq 2 \times 10^5$ -所有输入值均为整数。

