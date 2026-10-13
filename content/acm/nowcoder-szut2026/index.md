---
title: "苏州工学院 2026 ACM 新生赛（同步赛）"
tags: [nowcoder, 题解]
aliases: ["/acm/21post/"]
date: 2026-10-10
draft: false
comments: true
upsolve:
  - problem: "M"
    name: "无尽咔咔（Hard Version）"
    url: "https://ac.nowcoder.com/acm/contest/141092/M"
    status: "wrong"
    note: "2h59 分三分 Wa 了没时间了；赛后确认 a(t) 有平台不是严格单峰，官方是两候选点公式，文中已补"
---

比赛时间：2026-10-10 18:00 ~ 21:00（共 3h，13 题）

**排名情况**：958 人参与，第 95 名（前 10%），12/13，罚时 603 分钟

**做题情况**

- 18:00 A 过（开局 1 分钟内，零失败）
- 18:02 B 过（2min）
- 18:05 C 过（5min）
- 18:09 D 过（9min）
- 18:11 E 过（11min）
- 18:14 F 过（14min）
- 18:23 G 过（23min）
- 18:28 H 过（28min）
- 19:06~19:32 I：第一版（3 方向 + 和式剪枝 BFS）连错 4 发，19:32 换四方向四维状态版才过
- 19:36 J 过（一发）
- 19:53 K 过（一发）
- 20:07 提交 L 的代码，判题状态一直不动；20:20 才发现是封榜了 + 这份代码还交错到了 M（Hard）上，白送 M 一发 WA
- 20:09 L 过
- 20:52 / 20:59 M 三分两连 WA，比赛结束

前 28 分钟 8 题全清且全部一发过，是打到现在开场最顺的一场。心态波动全在下半场：I 题的等价性一分钟就想明白了（两行迷宫的堵路只有同列、斜对两种形态），第一版也是照着它写的单调向右 BFS，结果 4 发全摔在实现细节上（else-if 顺序吃标志位、push 漏分支），硬是拉锯了 26 分钟；然后 20:07 那波"判题状态为什么不动"的困惑直接把节奏打断——盯着页面反复刷新怀疑 OJ 炸了，十几分钟后才把"封榜"和"交错题"两件事同时想明白，那一刻是又好气又好笑。最后 50 分钟全押在 M 上：打表确认了"先回血后攻击"的形态，推出 $a(t)$ 近似开口向下的抛物线，三分收尾，两发 WA 之后时间到。赛后暴力对拍找到了反例——是单峰性这个前提本身错了，不是代码细节。

## A - Hello,SZUT!
https://ac.nowcoder.com/acm/contest/141092/A

> 欢迎参加苏州工学院 2026 ACM 新生程序设计竞赛！从这里开始你的编程之旅吧~

**输入**

本题无输入。

**输出**

输出一行字符串 `Hello,SZUT!`（不用带引号）。

```cpp
#include <bits/stdc++.h>
using namespace std;

//1min
int main(){
	cout<<"Hello,SZUT!";
	return 0;
}
```

### 官方题解对比

**官方做法**：直接输出。

**我的思路解读**：开局签到，1 分钟过。

## B - 请勿食用胀罐棉花糖
https://ac.nowcoder.com/acm/contest/141092/B

> 距离本轮探索结束还有 $t$ 分钟。每拜访一位旅行者需要先花 $a$ 分钟驾驶、再花 $b$ 分钟观察，两步都完成才算一次完整拜访。问剩余时间内最多还能完成多少次拜访。

**输入**

一行三个整数 $t,a,b$（$0 \le t \le 10^9$，$1 \le a,b \le 10^9$）。

**输出**

最多能完成的拜访次数。

```cpp
#include <bits/stdc++.h>
using namespace std;
long long t,a,b;

//2min
int main(){
	cin>>t>>a>>b;
	cout<<t/(a+b);
	return 0;
}
```

### 官方题解对比

**官方做法**：每次拜访耗时 $a+b$，只能计完整次数，答案即 $\lfloor t/(a+b) \rfloor$。

**我的思路解读**：和官方一致。唯一要小心的是 $a+b$ 最大 $2 \times 10^9$，`int` 会爆，所以直接上了 `long long`。

## C - 红石比较器
https://ac.nowcoder.com/acm/contest/141092/C

> 主输入端信号 $a$，左右侧输入端信号 $b,c$，只在意更强的侧输入，即 $s=\max(b,c)$。比较模式（$m=0$）：$s \le a$ 时输出 $a$，否则输出 $0$；作差模式（$m=1$）：输出 $\max(a-s,0)$。

**输入**

第一行一个整数 $m \in \{0,1\}$，第二行三个整数 $a,b,c$（$0 \le a,b,c \le 15$）。

**输出**

对应的红石信号强度。

```cpp
#include <bits/stdc++.h>
using namespace std;
long long s,m,a,b,c;

//6min
int main(){
	cin>>m>>a>>b>>c;
	s = max(b,c);
	if(m == 0){
		if(s <= a) cout<<a;
		else cout<<0;
	}
	else{
		cout<<max(a-s,1LL * 0);
	}
	return 0;
}
```

### 官方题解对比

**官方做法**：先取 $s=\max(b,c)$，再按两种模式分类计算。

**我的思路解读**：和官方完全一致，纯模拟签到。

## D - 阿克西斯的共鸣
https://ac.nowcoder.com/acm/contest/141092/D

> $n$ 台 MS 顺时针围成一个环。每台 MS 的推力等于自身功率加上左右相邻两台功率的一半。求所有 MS 的推力之和。

**输入**

第一行一个整数 $n$（$3 \le n \le 200$），第二行 $n$ 个整数 $v_i$（$0 \le v_i \le 10^4$）。

**输出**

所有推力之和（保证是整数且小于 $10^6$）。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 220;
long long n,ans;
long long a[maxn];

//9min
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i],ans += a[i];
	
	cout<<ans*2;
	return 0;
}
```

### 官方题解对比

**官方做法**：每台功率既完整贡献给自己，又各以一半借给左右两位邻居，合计被计入两次，答案即 $\sum v_i \times 2$。

**我的思路解读**：和官方一致。读题时画了个三项小环验证了一下"自己 + 左右各一半"，加起来恰好每份功率出现两次，直接求和乘 2。

## E - 找呀找呀找朋友
https://ac.nowcoder.com/acm/contest/141092/E

> $n$ 名同学排成一排，第 $i$ 人喜欢的番剧为 $a_i$。喜欢的番剧相同的两人称为一对好朋友，求所有好朋友对 $(i,j)$（$i \lt j$）的距离 $j-i$ 之和。

**输入**

第一行一个整数 $n$（$1 \le n \le 100$），第二行 $n$ 个整数 $a_i$（$1 \le a_i \le 100$）。

**输出**

所有好朋友之间距离的总和。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
long long n,ans;
long long a[maxn];

//11min
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			if(a[i] == a[j]){
				ans += j - i;
			}
		}
	}
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：$O(n^2)$ 枚举所有数对，相等就累加 $j-i$。

**我的思路解读**：和官方一致。$n \le 100$ 没有任何优化必要。

## F - 晨跑打卡
https://ac.nowcoder.com/acm/contest/141092/F

> $a_i \ge k$ 的天算打卡成功，求最长的一段连续打卡成功的天数。

**输入**

第一行两个整数 $n,k$（$1 \le n \le 100$，$0 \le k \le 5\times10^4$），第二行 $n$ 个整数 $a_i$（$0 \le a_i \le 5\times10^4$）。

**输出**

最长连续打卡天数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxm = 5e4+1,maxn = 110;
long long n,ans,k;
long long a[maxn];

//14min
int main(){
	cin>>n>>k;
	for(int i=1;i<=n;i++) cin>>a[i];
	long long tmp = 0;
	for(int i=1;i<=n;i++){
		if(a[i] < k){
			tmp = 0;
			continue;
		}
		tmp++;
		ans = max(tmp,ans);
	}
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：从左到右扫描，维护当前连续成功天数，失败清零，取最大值。

**我的思路解读**：和官方一致，最标准的滑窗计数签到。

## G - 寻找数字之神
https://ac.nowcoder.com/acm/contest/141092/G

> 数字之神本体是两位数 $n$（$10 \le n \le 99$），伪装后会往左右添加任意多位数字。给定 $m$（$100 \le m \le 10^9$），判断 $n$ 是否为 $m$ 的连续子串。

**输入**

一行两个整数 $n,m$。

**输出**

可能输出 `YES`，否则 `NO`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxm = 5e4+1,maxn = 110;
string n,m;
int len1,len2;
bool ans;

//24min
int main(){
	cin>>n>>m;
	len1 = n.length();
	len2 = m.length();
	ans = 1;
	
	for(int i=0;i<len2 - len1 + 1;i++){
		ans = 1;
		for(int j=0;j<len1;j++){
			if(n[j] != m[i+j]){//唐 没加j来了
				ans = 0;
				break;
			}
		}
		if(ans) break;
	}
	
	if(ans) cout<<"YES";
	else cout<<"NO";
	
	return 0;
}
```

### 官方题解对比

**官方做法**：把 $m$ 当数字，每次 `m % 100` 取末两位与 $n$ 比较、`m /= 10` 去掉末位，直到 $m < 10$。

**我的思路解读**：我用的是字符串暴力匹配：枚举 $m$ 的每个起点 $i$，逐位比 $n[j]$ 与 $m[i+j]$。这里还留了个翻车注释——第一遍把内层比较写成了 `m[i]`，忘了加 `j`，样例直接挂掉才改过来。本质和官方等价，只是官方用数位取模更省事。

## H - 第五人格模仿者启动！
https://ac.nowcoder.com/acm/contest/141092/H

> 每位玩家属于侦探团（永远说真话）或模仿者（永远说假话），保证至少一位侦探。每人都说一句"我们中有 $x$ 位侦探团"。根据所有人说的 $x$ 确定侦探团人数，存在多种可能输出任意一个，保证有解。

**输入**

第一行一个整数 $n$（$2 \le n \le 1000$），第二行 $n$ 个整数 $x_i$（$1 \le x_i \le n$）。

**输出**

任意一个可行的侦探团人数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 1001;
int n,ans;
int a[maxn],cnt[maxn];

//28min
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i],cnt[a[i]]++;
	for(int i=n;i>=1;i--){
		if(cnt[i] == i){
			ans = i;
			break;
		}
	}
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：假设侦探数为 $i$，那么说"有 $i$ 位"的人全说真话、其余全说假话，所以 $i$ 成立当且仅当数字 $i$ 恰好出现 $i$ 次。统计每个数的出现次数，输出任意满足 $\text{cnt}[i]=i$ 的正整数 $i$。

**我的思路解读**：和官方一致。关键观察是"说真话的人的话必须完全一致"——所有侦探说的都是同一个数 $i$，而模仿者说的 $x \ne i$。于是 $i$ 当且仅当恰好出现 $i$ 次。我从大到小枚举找的第一个解，官方从小到大，等价（保证有解所以一定找得到）。

## I - 快速夺取
https://ac.nowcoder.com/acm/contest/141092/I

> $2$ 行 $n$ 列网格，部分格子有不可穿越的机器人。从 $(1,1)$ 出发四方向移动，判断能否先经过铂金条 $(r_1,c_1)$、再经过收集箱 $(r_2,c_2)$。

**输入**

第一行一个整数 $n$（$2 \le n \le 100$）；第二行四个整数 $r_1,c_1,r_2,c_2$；接下来两行每行 $n$ 个 0/1 表示是否为障碍。保证起点、金条、收集箱三格无机器人且金条与收集箱位置不同。

**输出**

存在路线输出 `YES`，否则 `NO`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
int n,r1,c1,r2,c2;
bool a[3][maxn];
bool b[3][maxn][2][2];
bool ans;

int dy[4] = {0,0,1,-1},dx[4] = {-1,1,0,0};

//1h 33min
struct node{
	int x,y,vlu1,vlu2;
};

void solve(){
	queue<node> q;
	node tmp;
	tmp.x = 1,tmp.y = 1,tmp.vlu1 = 0,tmp.vlu2 = 0;
	if(1 == r1 && 1 == c1) tmp.vlu1 = 1;

	if(1 == r2 && c2 == 1 && tmp.vlu1 == 1) tmp.vlu2 = 1;
	q.push(tmp);
	b[1][1][tmp.vlu1][tmp.vlu2] = 1;
	while(!q.empty()){
		int nx = q.front().x,ny = q.front().y,nv1 = q.front().vlu1,nv2 = q.front().vlu2;
		q.pop();

		if(nv1 == 1 && nv2 == 1){
			ans = 1;
			return;
		}

		for(int i=0;i<4;i++){
			node tmpp;
			int nxtx = nx + dx[i],nxty = ny + dy[i];
			if(nxtx < 1 || nxtx > 2 || nxty < 1 || nxty > n) continue;
			if(a[nxtx][nxty]) continue;
			tmpp.x = nxtx,tmpp.y = nxty,tmpp.vlu1 = nv1,tmpp.vlu2 = nv2;
			if(nxtx == r1 && nxty == c1) tmpp.vlu1 = 1;
			if(nxtx == r2 && nxty == c2 && tmpp.vlu1 == 1) tmpp.vlu2 = 1;
			if(b[nxtx][nxty][tmpp.vlu1][tmpp.vlu2]) continue;
			b[nxtx][nxty][tmpp.vlu1][tmpp.vlu2] = 1;
			q.push(tmpp);
		}
	}
}

int main(){
	cin>>n;
	cin>>r1>>c1>>r2>>c2;
	for(int i=1;i<=2;i++){
		for(int j=1;j<=n;j++){
			cin>>a[i][j];
		}
	}
	
	ans = 0;
	if(a[1][1]){
		cout<<"NO";
		return 0;
	}
	
	solve();
	
	if(ans) cout<<"YES";
	else cout<<"NO";
	
	return 0;
}
```

### 官方题解对比

**官方做法**：两行的迷宫里，堵路只有两种形态——同一列上下都是机器人，或相邻两列斜着相对的机器人；单个机器人总能从另一行绕过。所以只扫 $1..\max(c_1,c_2)$ 列，出现堵路形态输出 `NO`，否则 `YES`（允许往返，先拿金条再送收集箱即可）。$O(n)$。

**我的思路解读**：这题是上半场唯一的污点——榜单上挂着 4 发 WA，19:06 写第一版，19:32 才过。但要说清楚：**关键等价性（两行迷宫的堵路只有同列上下、相邻列斜对两种形态，其余都能从另一行绕过）我一开始就想对了**，第一版 I.cpp 就是照着它实现的——只保留上、下、右三个方向（起点在最左，有用的状态全在右边，永远不需要往左走），再用 $b[x][y] \ge \text{vlu}_1+\text{vlu}_2$ 的和把每格状态压成一个整数。思路层面没有走弯路，26 分钟全耗在实现细节上，注释里那几个"唐比点"很诚实：判 $\text{vlu}_2$ 时写成了 `else if`（同一格先触发金条就永远点不亮收集箱标志）、扩展出状态后 push 漏了分支、visited 初值没设对。错到第四发不想再跟压缩判重纠缠，重写成最保守的版本：四方向 + $b[x][y][v_1][v_2]$ 四维 visited，"拿到金条后才允许点亮收集箱标志"用 $\text{vlu}_1==1$ 显式卡住，一发过。官方的题解把等价性用得更彻底：直接扫 $1..\max(c_1,c_2)$ 列做形态判断，$O(n)$ 结束。教训：**等价性转化正确不等于落地无虞——压缩判重省下的那点内存，代价是把前提藏进了隐性问题里**。

## J - 争夺数字之神
https://ac.nowcoder.com/acm/contest/141092/J

> 一堆 $n$ 颗石子，两人轮流取 1 或 2 颗，取走最后一颗的人获胜。问先手是否存在必胜策略。

**输入**

一个整数 $n$（$1 \le n \le 10^5$）。

**输出**

先手必胜输出 `YES`，否则 `NO`。

```cpp
#include <bits/stdc++.h>
using namespace std;

//注意到和3取模有特殊性质 经典技巧
//1h 36min

int main(){
	int n;
	cin>>n;
	if(n%3 == 0) cout<<"NO";
	else cout<<"YES";
	return 0;
}
```

### 官方题解对比

**官方做法**：巴什博弈。$n$ 是 3 的倍数时先手必败；否则先手先取 1 或 2 颗把剩余凑成 3 的倍数，之后对手取 $k$ 我取 $3-k$，稳拿最后一颗。

**我的思路解读**：经典结论，$n \bmod 3$ 判定。注释里也写了"和 3 取模有特殊性质"，直接一行出答案。

## K - 三角符文扑克谜题
https://ac.nowcoder.com/acm/contest/141092/K

> 空序列上两种操作任意次：末尾插入 $1$，或把整个序列 0/1 全部翻转。构造给定 01 目标序列的最少操作次数。

**输入**

第一行一个整数 $n$（$1 \le n \le 100$），第二行 $n$ 个数字 $a_i \in \{0,1\}$。

**输出**

最少操作次数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
int n;
int a[maxn];
int ans;

//1h 51min
void solve1(){
	for(int i=1;i<=n;i++){
		if((1 + ans) % 2 == a[i]) continue;
		ans += 2;
	}
}

void solve2(){
	int now = a[1];
	if(a[1] == 0) ans++;
	for(int i=2;i<=n;i++){
		if(a[i] == a[i-1]) continue;
		ans += 2,now = 0;
	}
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	ans = n;
	int now = a[1];
	if(a[1] == 0) ans++;
	for(int i=2;i<=n;i++){
		if(a[i] == now) continue;
		if(now == 1) ans += 2,now = 0;
		else now = 1;
	}
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：插入必须恰好 $n$ 次。相邻两块图案不同，它们的插入之间至少要翻转一次；相同则不用。最后插入的永远是 $1$，若目标末位是 $0$ 还得再翻一次。答案 $= n + (a_n = 0) + \sum_{i \lt n}[a_i \ne a_{i+1}]$。

**我的思路解读**：公式形式和官方不一样，但可以证明等价。我的记法是：开头若第一位是 $0$ 记 $1$ 次翻转；每遇到一个 $1 \to 0$ 的下降沿记 $2$ 次。代入恒等式"$0\to1$ 的次数 $= 1\to0$ 的次数 $+$（首位为 0）$-$（末位为 0）"，官方式子 $n + [a_n{=}0] + \#(\text{相邻不同}) = n + 2\cdot\#(1\to0) + [a_1{=}0]$，正好就是我的式子。本质都是"段数计数"：翻转让插入的字符在 0/1 之间切换，切换次数由段数决定。

## L - 无尽咔咔（Easy Version）
https://ac.nowcoder.com/acm/contest/141092/L

> 玩家初始 $x$ 点生命值，与每回合伤害递增的咔咔交战，玩家先手。每回合开始选择：攻击（造成 1 点伤害）或回复（生命 $+y$，无上限）。设当前回合数为 $i$，行动结束后咔咔对玩家造成 $i$ 点伤害。生命 $\le 0$ 立即结束，即使本回合死亡，本回合攻击的伤害也计入答案。求最多能造成的伤害。

**输入**

一行两个整数 $x,y$（$1 \le x,y \le 10^5$）。

**输出**

最多伤害值。

```cpp
#include <bits/stdc++.h>
using namespace std;
long long x,y,ans;
#define ll long long

//2h 7min 交了为啥弄不上去 显示判题状态
//2h 20min 奥原来是封榜了 我好唐 还交错题目了 交到数据更强的版本了

//注意到回合数应该会很小 不管了直接搓个神秘枚举
//发现数学规律 需要 x + r*y > (t-1)*t/2 才能活到第 t 回合攻击

int main(){
	cin>>x>>y;
	for(ll t=1;t<=1000000;t++){//改小了
		ll n = (t-1)*t/2 - x,r = 0;
		if(n >= 0) r = n / y + 1;//向上取整回血次数 其实先回血可能是更赚的 其实无所谓 因为我已经确定为回合数了
		if(t < r) break;//这后面肯定都不行了 回血回不上
		ans = max(ans,t - r);
	}
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：贪心模拟——维护攻击次数，每回合先更新 `ans = max(ans, attack+1)`（计入可能发生的致死一击），若当前生命能扛过本回合伤害就攻击，否则回复。交换论证可证该贪心最优，$O(\text{回合数})$。

**我的思路解读**：换了个角度——枚举总回合数 $t$。若前 $t-1$ 回合里回复了 $r$ 次，要活到第 $t$ 回合攻击就需要 $x + r\cdot y > \frac{(t-1)t}{2}$，解出最少回复次数 $r=\lceil \frac{(t-1)t/2 - x}{y} \rceil$，则攻击数 $t - r$，对所有 $t$ 取 max。这个"固定总回合数"的视角本来是为 Hard 版准备的（Easy 直接枚举就过了），Hard 版会再提到它。中间还闹了个乌龙：2h07 提交后一直显示不出判题状态，20 分钟后才反应过来是封榜了——而且手滑把这份代码交到了 Hard 的题上。

## M - 无尽咔咔（Hard Version）
https://ac.nowcoder.com/acm/contest/141092/M

> 与 Easy 唯一的区别：$1 \le x,y \le 10^{12}$。

**输入**

一行两个整数 $x,y$（$1 \le x,y \le 10^{12}$）。

**输出**

最多伤害值。

比赛时先用 `__int128` 写了个三重循环的打表程序（对小组 $x,y$ 暴力模拟找答案），确认了"先连续回复再连续攻击"的形态，然后写了三分的正式提交：

```cpp
#include <bits/stdc++.h>
using namespace std;
long long x,y,ans;
#define ll __int128

//2h 59min 极限！！
//WA 了 没时间了 充能面包

/*
打表打了半天没看出来有什么显著的做法
肯定和数学有关 一开始在想二分 但是性质不显然
再想想二分 我就觉得新生赛不会出太难的数据结构
这些刚刚分析的回合数 最小回血数 有没有什么数学性质？？
而且 回复越早 是不是更好？？感觉上是这样的？？
因为 如果回合数确定的话 其实回血啥时候回都一样 差不多
而且越早回血 一开始的攻击值是很少的 回合数应该会变多？
是否就有先回血一定最优？
打表了一下 发现应该确实如此
所以应该是 先连续回复 r 次 再连续攻击 a 次
前 k 回合的累计伤害是 k(k+1)/2
要完成第 t 回合的攻击 玩家必须在第 t 回合开始前还活着
x + r*y > (t-1)*t/2
注意是 t-1 t回合的伤害是在攻击之后才结算的 即攻击后死亡 (燃尽了
如果给定 t 显然能解出最少需要的回复次数
n = (t-1)*t/2 - x
n < 0   r = 0 说明不用回血
n >= 0  r = n / y + 1 向上取整

注意！！！现在如果不确定t 是否能表示出t？？
注意到！！ a = t - r 代入得到一个式子
a = t - r 想最大化 a
连续近似 a(t) ≈ -t^2/(2y) + t(1+1/(2y)) + x/y - 1
开口向下抛物线 顶点 t ≈ y + 0.5 单峰！
t 上界 2y 再多 r > t 攻击数为负 没意义
t 最大 2e12 算 t^2 爆 long long 必须 __int128
二分？？不对 要三分！！
*/

ll c(ll t){
	__int128 n = (__int128)(t-1)*t/2 - x;
	ll r = 0;
	if(n >= 0) r = (ll)(n / y) + 1;
	ll a = t - r;
	return a;
}

int main(){
	cin>>x>>y;
	ll l = 1,h = 2*y + 10;
	while(h - l > 2){
		ll m1 = l + (h - l) / 3;
		ll m2 = h - (h - l) / 3;
		if(c(m1) < c(m2)) l = m1;
		else h = m2;
	}
	ans = 0;
	for(ll t = l;t<=h;t++) ans = max(ans,c(t));
	cout<<ans;
	return 0;
}
```

### 官方题解对比

**官方做法**：不需要扫全部 $t$，峰值只在两个候选点出现：

1. $l+1$，其中 $l$ 是不回复时能活过的最大完整回合数（即最大的 $t$ 满足 $\frac{t(t+1)}{2} < x$），在 $l+1$ 回合硬冲一波然后死，拿到 $l+1$ 次攻击；
2. $y+1-heal$，其中 $heal = \max\left(0,\ \left\lceil\tfrac{y+1}{2}\right\rceil - q + [\,b > rem\,]\right)$，$q=\lfloor\frac{x-1}{y}\rfloor,\ rem=(x-1)\bmod y,\ b = \frac{y}{2}$（$y$ 为偶数时，否则记 0）——即"先回血再攻击"撑过第 $y+1$ 回合这个伤害峰值的方案。

二分求 $l$ 后两处取 max 即可，复杂度 $O(\log x)$。

```cpp
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    ll x, y;
    scanf("%lld%lld", &x, &y);
    ll l = 0, r = 2000000;
    // 找到不回复时，最多能活过多少个完整回合。
    while (l < r) {
        ll mid = (l + r + 1) / 2;
        if (mid * (mid + 1) / 2 < x) l = mid;
        else r = mid - 1;
    }
    ll ans = l + 1;
    // 计算第 y+1 回合之前所需的回复次数。
    ll q = (x - 1) / y, rem = (x - 1) % y;
    ll b = (y % 2 == 0 ? y / 2 : 0);
    ll heal = max(0LL, (y + 1) / 2 - q + (b > rem));
    ans = max(ans, y + 1 - heal);
    printf("%lld\n", ans);
    return 0;
}
```

**我的思路解读（赛后补）**：M 的三发 WA 里，第一发是 20:07 那份交错过去的 L 代码（白送的），后两发都是下面的三分。我的框架（先回血后攻击、固定 $t$ 解出 $r=\lceil\frac{(t-1)t/2-x}{y}\rceil$、攻击数 $t-r$）是对的，错在"三分找峰值"这最后一步。赛后写了暴力逐回合 DP 对拍，$x,y \le 59$ 范围内三分版错了 36 组——比如 $x=1,y=19$ 时正解是 10，我的程序输出 9。原因：$a(t)=t-r(t)$ 只是"近似"抛物线，实际带着平台和抖动，并不是严格单峰。上面这个反例里峰值出现在 $t=19,20$（都是 10），但三分在比较两侧值相等时朝错误方向收缩区间，把 19、20 这两个点剪掉了，最后扫出来的只有 9。

官方的做法漂亮在直接证明了最优值只会出现在两个特殊点上：要么不回血硬冲到死（候选 1），要么把回复全堆在最前面撑过第 $y+1$ 回合这个伤害峰值（候选 2）。从无需回复切换到需要回复时 $a$ 不会增加，且 $t \approx y+\frac12$ 附近增量的正负发生翻转，所以两处取 max 就是全局最优。教训和 ABC476 D 题一模一样：**想对函数做三分/二分之前，先证明它（严格）单峰，"连续近似看起来像抛物线"不算证明**。

---

## 赛后总结

**成绩**：958 人第 95 名（前 10%），12/13。前 28 分钟 8 题全清、5 题一发过的开局是本场最大亮点；I 题的 4 发和 M 的 3 发是全部损耗。

**做得好的**：

- A~H 签到段思路与官方完全一致，零失误，28 分钟打完给了后面充足的思考时间。
- L 的"固定总回合数、解最少回复次数"枚举是自己推出来的正确模型，Easy 秒杀。
- K 的段数计数公式与官方写法不同但等价（$0\to1$ 段数 $=1\to0$ 段数 $+$ 首零 $-$ 末零），推恒等式的过程比代码本身有意思。

**不足**：

1. **I 题（-4 发）**：等价性一开始就想对了（堵路只有同列/斜对两种，不需要往左走），第一版也是照着它做的单调向右 BFS——思路零分，实现扣满。`else if` 顺序吃掉标志位、push 漏分支、visited 初值，全是细节连环爆。教训：用压缩判重省内存的代价是把前提藏进隐性问题里，调试时根本想不到去查它；第 4 发换保守的四维状态一步到位。下次遇到"思路早就清楚但一直 WA"，优先把判重换成最笨的全状态版本，先让 AC 落袋再谈优化。
2. **交错题 + 封榜误判（-13 分钟心态）**：20:07 把 L 的代码交到 M 上，又恰逢封榜看不到判题结果，第一反应是"OJ 是不是炸了"，来回刷新浪费十几分钟才同时想明白两件事。以后判题状态不动，第一反应查封榜、第二反应核对提交的题号。
3. **M 题三分（-2 发）**：对 $a(t)$ 做"连续近似 ≈ 抛物线 → 单峰"的跳跃没有证明就上了三分。单峰性是三分的合法前提，不是观察结论——要么严格证，要么把两个候选点解出来（官方就是这么做的）。赛后对拍 36 组反例，教训扎实。
4. **收尾时间分配**：最后 50 分钟全押 M，没有留出哪怕 10 分钟扫一眼后面的题是否存在送分。

M 题赛后已按官方"两候选点 + 二分"补掉，见上文。总体是一场"开局漂亮、收尾翻车"的比赛，翻车的三处全是可复用的检查项。