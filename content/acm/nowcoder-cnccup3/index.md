---
title: "南昌大学软件学院第三届雏鸟杯程序设计竞赛"
tags: [nowcoder, 题解]
aliases: ["/acm/22post/"]
date: 2026-10-12
draft: false
comments: true
upsolve:
  - problem: "N"
    name: "小h的地毯(hard)"
    url: "https://ac.nowcoder.com/acm/contest/141369/N"
    status: "wrong"
    note: "剩 1min 提交 25/30，最后一个点 TLE；文中已补「行并查集」修复版"
  - problem: "O"
    name: "小h的实验"
    url: "https://ac.nowcoder.com/acm/contest/141369/O"
    status: "skip"
    note: "比赛没来得及看；赛后自推了一个 O(N) 公式做法，已通过样例与暴力对拍，见文中补题节"
---

比赛时间：正赛 2026-10-11 14:00 ~ 17:00（学校限定）；我打的是 2026-10-12 20:45 ~ 23:45 的**重现赛**（打星，共 3h，15 题）
官方题解帖：<https://www.nowcoder.com/discuss/938846423225786368>

**排名情况**：重现赛 255 / 290 分，13/15（N 题 25/30 部分分），重现赛榜单第 1（发稿时榜上唯一记录）。正赛未报名；若把这份分数折到正赛榜（193 人）大约在第 11 位，再往前的就全是 14~15 题的强校选手了。

**做题情况**（重现赛时钟）

- 20:46 A 过（1min）
- 20:48 B 过（3min）
- 20:51 C 过（6min）
- 21:10 D 过（25min）
- 21:18 E 过（33min）
- 21:22 F 过（37min）
- 21:29 G 过（44min）
- 21:38 H 过（53min）
- 21:49 I 过（1h04）
- 21:56 J 过（1h11）
- 22:01 K 没有思路先跳过，转头 L
- 22:16 L 过（1h31）
- 22:22 K 有了差分的方向，但复杂度上一直想不通
- 22:57 K 依旧卡着（此时还在纠结 n、m 是 1e6 的问题）
- 23:07 发现题目是 $n \cdot m \le 10^6$，K 过（2h22）
- 23:20 M 过（2h35）
- 23:28 N 开写（2h43，剩 17min）
- 23:44 N 剩 1min 提交，25/30，最后一个点 TLE
- O 没来得及看

13 题 AC 全部一发过，整场的失败都发生在"想"而不是"交"。节奏的转折点在 K：前 1h11 顺风 10 题，之后整整 1 小时耗在"$n, m$ 都是 1e6 这怎么做"的错误前提上——反应过来是 $n \cdot m \le 10^6$ 之后 5 分钟写完。被 K 吃掉的这一小时直接决定了结局：N 只剩 15 分钟赶工（框架对了但少跳一维，25/30），O 连读题的时间都没有。

## A - 输出第一个字符
https://ac.nowcoder.com/acm/contest/141369/A

> 输入一个仅由小写字母构成的字符串，输出它的第一个字符。

**输入**

一行一个字符串，长度不超过 100。

**输出**

一行一个字符。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
string s;

//1min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>s;
	cout<<s[0];
	return 0;
}
```

### 思路解析

签到，`s[0]` 完事，1 分钟。官方做法：读入字符原样输出，完全一致。

## B - 小h是雨
https://ac.nowcoder.com/acm/contest/141369/B

> 小h去云南旅游吃了菌子出现幻觉，说出了很有哲理的话"我是雨!"。按给定图案打印雨滴。

**输入**

无。

**输出**

九行由 `#` 和空格组成的雨滴图案（见样例，行尾注意：最后一行不带换行）。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;

//3min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout<<"   #"<<'\n';
	cout<<"  ###"<<'\n';
	cout<<" #####"<<'\n';
	cout<<"#######"<<'\n';
	cout<<"#######"<<'\n';
	cout<<"#######"<<'\n';
	cout<<" #####"<<'\n';
	cout<<"  ###"<<'\n';
	cout<<"   #";
	return 0;
}
```

### 思路解析

输出题。行数少直接硬打，注意别手滑把空格数量打错、以及最后一行不要多输出换行。官方做法一致。

## C - 判断三角形
https://ac.nowcoder.com/acm/contest/141369/C

> 输入三个正整数 $a,b,c$ 表示三边。先判断能否构成三角形；能则按三边关系输出 `Equilateral`（等边）/ `Isosceles`（等腰）/ `Scalene`（普通），否则输出 `Not a triangle`。

**输入**

一行三个正整数 $a,b,c$（$1 \le a,b,c \le 1000$）。

**输出**

按题目要求输出对应字符串。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int a,b,c;

//6min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>a>>b>>c;
	if(a + b <= c || a + c <= b || b + c <= a) cout<<"Not a triangle";
	else if(a == b && a == c) cout<<"Equilateral";
	else if(b == c || a == b || a == c) cout<<"Isosceles";
	else cout<<"Scalene";
	return 0;
}
```

### 思路解析

先三角形不等式（任意两边之和大于第三边，等价于最短两边之和大于最长边），再按相等关系分类。注意判断顺序：先排除 `Not a triangle`，否则 `1 1 1` 之类的会先掉进等腰分支。官方做法一致，并特别提醒等边要在等腰之前判，否则等边会被误判成等腰。

## D - 乘积等于和
https://ac.nowcoder.com/acm/contest/141369/D

> 构造一个长度为 $n$ 的正整数数组，元素 $\le 10^8$，满足所有元素的乘积等于所有元素的和（和不超过 $10^{18}$）。保证有解，输出任意一组。

**输入**

一行一个整数 $n$（$1 \le n \le 10^6$）。

**输出**

一行 $n$ 个正整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
ll n;
ll a,b;

//25min

//x^n == x*n ?
//哦 想到一个简单的构造 可以做转换为枚举
//	a + b + (n - 2) == a * b ?
//  假设 a 确定 那么 b == (n - 2 + a) / a + 1
//  保证两个数一定有解？？
//  不想了 程序帮我验证一下
//  应该是对的

void solve1(int x){
	vector<ll> v;
	if(x == 1) return;
	for(a=1;a<=10000000;a++){
		b = (x - 2 + a)	/ a + 1;
		if(a + b + (x - 2) == a * b){
			return;
		}
	}
	cout<<"qwqq";
	return;
}


int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	
	if(n == 1){
		cout<<1;
		return 0;
	}
	for(a=1;a<=10000000;a++){
		b = (n - 2 + a)	/ a + 1;
		if(a + b + (n - 2) == a * b){
			cout<<a<<' '<<b<<' ';
			for(int i=3;i<=n;i++) cout<<1<<' ';
			return 0;
		}
	}
	
	
	return 0;
}
```

### 思路解析

多填一个 1：乘积不变、和加一。所以设最终数组是 `a, b, 1, 1, ..., 1`，条件就化成 $a + b + (n-2) = a \cdot b$，两个未知数一条方程，固定 $a$ 就能解出 $b$ 直接验证。枚举 $a$ 从小到大，找到就输出。

官方做法更直接——**把这个解拍在你脸上**：输出 $n-2$ 个 $1$、再输出 $2$ 和 $n$（$2n = (n-2)+2+n$），$n=1$ 特判。出题人在题解里自己标注"低估了这个题的难度"。

不担心找不到的另一个角度：$a = n,\ b = 2$ 恒为解（$2n = n + 2 + (n-2)$），所以我的枚举一定会在 $a = n$ 前停下来，$n \le 10^6 \ll 10^7$ 的上限只是保险。$n=1$ 时直接输出 `[1]`（$1=1$ 自洽）。

赛时在这里花了 25 分钟，事后看有点奢侈——不过"列方程 + 让程序验证"的路径至少每一步都踩实了。

## E - 买文具
https://ac.nowcoder.com/acm/contest/141369/E

> 带了 $N$ 元，买三种文具每种至少 1 件：钢笔 5 元、笔记本 3 元、橡皮 1 元。求正好花完的方案数。

**输入**

一行一个整数 $N$（$1 \le N \le 200$）。

**输出**

方案总数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 201;
int n;
//ll dp[maxn];
ll ans;

//32min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
//	dp[9] = 1;//注意审题 每种至少买一件
//	for(int i=10;i<=n;i++){
//		if(i - 1 >= 9) dp[i] += dp[i-1];
//		if(i - 3 >= 9) dp[i] += dp[i-3];
//		if(i - 5 >= 9) dp[i] += dp[i-5];
//	}
//	cout<<dp[n];
	//发现 dp 会多计 因为会多统计一个顺序
	if(n <= 8){
		cout<<0;
		return 0;
	}
	for(int i=1;i<=200;i++){
		for(int j=1;j<=99;j++){
			for(int x=1;x<=40;x++){//我靠我是个傻逼 一开始写小了
				if(n == i + j * 3 + x * 5) ans++;
			}
		}
	}
	cout<<ans;
	return 0;
}
```

### 思路解析

这题里埋了个经典陷阱：第一版的 `dp[i] = dp[i-1] + dp[i-3] + dp[i-5]` 数的是"购买顺序序列"，同样的三种文具买不同顺序会被算成不同方案，把组合问题做成了排列问题。发现多计之后干脆放弃 dp——$N \le 200$，直接三重循环枚举橡皮（$\le 200$）、笔记本（$\le 99$（应为 66，写 99 也无所谓））、钢笔（$\le 40$）验证 $i + 3j + 5x = N$，$8 \times 10^5$ 次循环轻松通过。官方做法更省一层循环：只二重枚举钢笔和笔记本，橡皮由剩余钱数直接确定（$z = N - 5x - 3y \ge 1$ 即合法）。

教训记一笔：**计数 dp 必须让"状态"与顺序无关**（按物品种类分层转移），否则就是排列数。数据范围小的时候暴力永远是最保底的正确方案。

## F - 西瓜投手
https://ac.nowcoder.com/acm/contest/141369/F

> $5 \times 9$ 草坪，西瓜投手在最左列，可以随时（无耗时）换到任意行，同一时刻场上最多一个僵尸。给定按顺序到来的僵尸所在行 $c_1,\dots,c_n$，投手初始在行 $a$，求击杀全部僵尸的最少移动次数。

**输入**

第一行 $n, a$（$1 \le n \le 100$，$1 \le a \le 5$），接下来 $n$ 行每行一个 $c_i$（$1 \le c_i \le 5$）。

**输出**

最少移动次数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int n,a;
int c[maxn];
int ans;

//37min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>n>>a;
	for(int i=1;i<=n;i++) cin>>c[i];
	
	if(a != c[1]) ans++;
	for(int i=2;i<=n;i++) if(c[i] != c[i-1]) ans++;
	cout<<ans;
	
	return 0;
}
```

### 思路解析

贪心：答案 $= [c_1 \ne a] + \sum_{i=2}^{n}[c_i \ne c_{i-1}]$。因为换行是免费的、瞬时的，唯一的花费出现在"需要的行发生变化"的时刻：初始行不对付第一个僵尸要挪一次，之后每相邻两只僵尸行数不同就必然挪一次，行数相同就连着打。这个下界显然可以构造达成。官方做法一致（维护当前行，不同就计数换行）。

## G - 小h的飞机
https://ac.nowcoder.com/acm/contest/141369/G

> 砍价模拟。共 $n$ 轮对话，每轮两个字符串 $s, t$。$s$ 为 `zaipainyidian`（继续砍）或 `maile`（买了，后续忽略）；$t$ 为 `keyi,danzhinengpainyiXyuan`（便宜 X 元，价格减 X 继续）或 `xiangdemei`（谈崩，按当前价成交）。求最终价格。

**输入**

第一行 $n, x$（$1 \le n \le 100$，$1 \le x \le 100$）；接下来 $n$ 行每行两个字符串。保证最终价格非负。

**输出**

最终成交价。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,x;
string s,t;

//44min

int main(){
//	ios::sync_with_stdio(false);
//	cin.tie(0);
	cin>>n>>x;
	for(int i=1;i<=n;i++){
		cin>>s>>t;
		if(s == "zaipainyidian"){
			if(t == "xiangdemei"){
				cout<<x;
				return 0;
			}
			else{
				int len = t.length();
				int cnt = t[21] - '0';
				for(int j=22;j<len;j++){
					if(t[j] < '0' || t[j] > '9') break;
					cnt = cnt * 10 + (t[j] - '0');
				}
//				keyi, danzh ineng painy i X yuan
				x -= cnt;
			}
		} 
		else if(s == "maile"){
			cout<<x;
			return 0;
		}
	}
	cout<<x;
	return 0;
}
```

### 思路解析

纯模拟，唯一的技术点是解析 `keyi,danzhinengpainyi`：这个前缀长 21 个字符（下标 0~20），所以 $X$ 从 `t[21]` 开始逐位读，读到非数字为止——要按多位数处理，不能只取一位。官方做法的取巧点是四个关键字首字母互不相同，直接按 `s[0]`、`t[0]` 分派，数字提取用 ASCII 范围判断后逐位还原；比我的下标定位更防手滑。

## H - 阶梯数
https://ac.nowcoder.com/acm/contest/141369/H

> 各位数字从左到右非递减的正整数称为阶梯数（如 1、9、12、123、112、555；而 10、21、120 不是）。求 $[A,B]$ 内阶梯数的个数。

**输入**

一行两个正整数 $A, B$（$1 \le A \le B \le 10^5$）。

**输出**

区间内阶梯数的个数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int a,b;

//54min
//数位dp 但是数据范围很小 不用

//inline check(int x){//?????? 怎么能运行的
inline bool check(int x){
	if(x >= 1 && x <= 9) return 1;
//	int now = 0;
	int now = 10;
	while(x){
		if(now < x % 10) return 0;
		now = x % 10,x /= 10;
	}
	return 1;
}

inline ll get(int x){
	if(x == 0) return 0;
	ll cnt = 0;
	for(int i=1;i<=x;i++) if(check(i)) cnt++;
	return cnt;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>a>>b;
	cout<<get(b) - get(a - 1);
	return 0;
}
```

### 思路解析

$B \le 10^5$，直接逐个检查 + 前缀相减，$O(6 \cdot 10^5 \cdot 6)$ 随便过，数位 dp 都不用上。官方做法一致：暴力逐个判断，数位比较（`prev` 从 10 起步）或转字符串排序后比对都行。

`check` 里有个小故事：`now`（上一位数字）必须初始化成 $10$，让首位不受任何约束；注释里那行 `int now = 0` 的旧版本会把所有多位数全判成 false——`now=0` 时第一位数字只要非零就 `0 < d` 直接返回 false。顺手还留了个 `inline check(int x)` 没写返回类型的翻车现场（"?????? 怎么能运行的"），好在后来改成 `inline bool` 了。

## I - 小h的能量球
https://ac.nowcoder.com/acm/contest/141369/I

> $n$ 个能量球排成一排，融合后能量为全部球的最大公约数。回收操作：从左至右选 $2k+1$ 个球（$k \ge 1$，不要求连续），回收正中间那个。任意次操作后，求剩余球融合能得到的最大能量。多测。

**输入**

第一行测试组数 $t$（$1 \le t \le 500$）；每组第一行 $n$（$1 \le n \le 100$），第二行 $n$ 个整数 $\alpha_i$（$1 \le \alpha_i \le 10^9$）。

**输出**

每组一个整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int t,n;
int a[maxn];

//1h 3min 写注释花了点时间

//不妨这么想 终结条件是长度为 2 首尾两个是不可能被去掉的 想想 如果长度不是 2而是更长 答案可能更大吗？不会 所以直接求首尾两个的gcd就行了
//为什么想到这个 因为分析可得 正面的去模拟 会发现删除伪任意（与现在长度有关） 且对后续有影响（会影响相对下标）
//所以倒着这想很简单 其实也是想到了 gcd多加一个数只可能变小 不会变大的性质

int gcd(int a,int b){return a%b==0? b:gcd(b,a%b);}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i];
		cout<<gcd(a[1],a[n])<<'\n';
	}
	return 0;
}
```

### 思路解析

答案就是 $\gcd(\alpha_1, \alpha_n)$，两步论证：

1. **两端的球永远删不掉**：想回收某个球，它必须是被选中的 $2k+1$ 个球的正中间，左右都得有球——第一个和最后一个球永远不满足。
2. **gcd 越融越小**：最终集合一定包含 $\alpha_1$ 和 $\alpha_n$，而往 gcd 里多加一个数只会让结果整除性更强、值不增，所以上界是 $\gcd(\alpha_1,\alpha_n)$；反过来每次选 3 个球删中间，就能把中间全删光，达到这个上界。

官方做法同一结论（"必须保留两边的数，中间可要可不要"）。

## J - 增高垫（Easy Version）
https://ac.nowcoder.com/acm/contest/141369/J

> 一排学生身高 $a_i$，只能垫增高垫不能变矮、不能换位置，让第 $i$ 人长高 1 花费 1 元。求最少花费使身高严格递增。$1 \le n \le 10^6$，$1 \le a_i \le 10^9$。

**输入**

第一行 $n$，第二行 $n$ 个整数 $a_i$。

**输出**

最少花费。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e6+1;
int n;
ll a[maxn];
ll ans;

//1h 12min
//很简单的贪心 思路证明这里不写了 注意开long long 即可

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=2;i<=n;i++){
		if(a[i] > a[i-1]) continue;
//		ans += a[i] - a[i-1] + 1;//唐
		ans += a[i-1] - a[i] + 1;
		a[i] = a[i-1] + 1;
	}
	cout<<ans;
	return 0;
}
```

### 思路解析

从左往右扫，每个人至少站到前一个人身高 $+1$：若 $a_i \le a_{i-1}$ 就把他垫到 $a_{i-1}+1$，花费 $a_{i-1}+1-a_i$。交换论证一下就知道这是最优的（把后面的人抬更高不会让前面更省）。官方做法一致。两个坑：注释里那行写反方向的"唐"式提交痕迹，以及 $n=10^6$、$a_i=10^9$ 时答案最大约 $10^{15}$，必须 `long long`。

## K - 小h的地毯(easy)
https://ac.nowcoder.com/acm/contest/141369/K

> $n \times m$ 大堂（$1 \le n \cdot m \le 10^6$），依次铺 $q$ 个矩形地毯（左下角、右上角、颜色），每次铺完回答一个询问：$(x,y)$ 处现在叠了几层地毯。$1 \le q,k \le 10^5$。

**输入**

第一行 $n,m,q,k$；接下来 $q$ 行 $x_1\ y_1\ x_2\ y_2\ c$；接下来 $k$ 行 $x\ y$。

**输出**

每个询问一行，该位置的地毯层数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e6+1;
int n,m,q,k;
struct kua{
	int nx,ny,mx,my,c;
}a[maxn];

//1h 16min 并没有什么合理的思路（时间复杂度太高） 先写下一题 下一题有思路
//1h 37min 哦我唐比了 这个不用修改 所以直接二维前缀和就行了
//不对 得再想想 我在说什么 这个数据范围是很大的
//嘶 既然更新(x1,y1)到(x2,y2)的点全部加1时间复杂度很大 能不能差分？
//但是差分就会有一个问题 你差分的对象是谁？以及单点访问的时候怎么计算？
//往暴力方面再想想 万一是优化暴力就能过呢
//2h 12min了 依旧没有什么思路
//n m不是10^6么 这不可能做出来吧????????????
//算了 不管了 先写个差分暴力试试
//卧槽我是个傻逼 人家说的是n*m<=1e6又糖了我
//2h 21min

vector<int> diff;
int w;

int idx(int x, int y){return x * w + y;}
int check(int x,int y){return diff[idx(x,y)];}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n>>m>>q>>k;
	
	w = m + 2;
	diff.assign((n + 2) * w, 0);
	
	for(int i=1;i<=q;i++){
		cin>>a[i].nx>>a[i].ny>>a[i].mx>>a[i].my>>a[i].c;
		int x1 = a[i].nx, y1 = a[i].ny;
		int x2 = a[i].mx, y2 = a[i].my;
		diff[idx(x1,y1)]++;
		diff[idx(x1,y2+1)]--;
		diff[idx(x2+1,y1)]--;
		diff[idx(x2+1,y2+1)]++;
	}
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			diff[idx(i,j)] += diff[idx(i-1,j)] + diff[idx(i,j-1)] - diff[idx(i-1,j-1)];
		}
	}
	
	while(k--){
		int x,y;
		cin>>x>>y;
		cout<<check(x,y)<<'\n';
	}
	
	return 0;
}
```

### 思路解析

本题的时间几乎全花在心态上：1h16 觉得"矩形加、单点查"复杂度太高跳去写 L；1h37 想到差分又怀疑查询代价；2h12 还在纠结"$n, m$ 各是 $10^6$ 那数组都开不下"；2h21 终于看清题目写的是 $n \cdot m \le 10^6$——**二维矩阵压成一维存，总格子数就是 $10^6$**，二维差分 $O(1)$ 修改、$O(nm)$ 前缀和、$O(1)$ 查询，全部毫无压力。官方做法一致（题解里还用面积法把二维差分从头教了一遍）。

教训：读题阶段把"数据范围约束"抄在纸上再看，$n \cdot m \le 10^6$ 和 $n,m \le 10^6$ 是完全不同的两道题。

## L - 增高垫（Hard Version）
https://ac.nowcoder.com/acm/contest/141369/L

> 与 Easy 的区别：只有一种操作——选一个后缀 $[i,n]$ 全部身高 $+1$，本次花费为后缀长度 $n-i+1$。$1 \le n \le 10^6$，$1 \le a_i \le 10^6$。求最少花费使身高严格递增。

**输入**

同 Easy，数据范围不同。

**输出**

最少花费。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e6+1;
int n;
ll a[maxn];
ll det,ans;

//1h 31min
//依旧是简单贪心 因为后缀的区间严格单减 所以可以轻松证明这个思路


int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	
//	for(int i=2;i<=n;i++){
//		if(a[i] + det > a[i-1]) continue;
//		ans += (a[i-1] - (a[i] + det) + 1) * (n - i + 1);
//		ll tmp = a[i-1] - (a[i] + det) + 1;
//		a[i] = a[i-1] - det + 1;
//		det += tmp;
//		cout<<i<<' '<<det<<' '<<ans<<'\n';
//	}
	for(int i=2;i<=n;i++){//唐 明明真没简单的东西写了这么久
		if(a[i] > a[i-1]) continue;
		ans += (a[i-1] - a[i] + 1) * (n - i + 1);
	}
	cout<<ans;
	return 0;
}
```

### 思路解析

设 $d_j$ 为最终第 $j$ 个人的身高增量。每次操作是后缀加一，所以"覆盖位置 $j$ 的操作次数"就是 $d_j$，而覆盖关系决定了 $d_1 \le d_2 \le \dots \le d_n$（后缀操作越往右覆盖越多）。于是约束是：$d$ 非降，且 $a_j + d_j$ 严格递增，最小化 $\sum d_j$。

递推：$d_j \ge d_{j-1}$ 且 $d_j \ge d_{j-1} + (a_{j-1}+1-a_j)$，即每一步至少要多垫 $\max(0,\ a_{j-1}+1-a_j)$ 层。把每个人的增量求和换算回操作花费（一次 $[i,n]$ 的操作贡献给 $d_i..d_n$ 各一，花费恰为长度 $n-i+1$）：

$$ans = \sum_{k=2}^{n} \max(0,\ a_{k-1}+1-a_k)\cdot(n-k+1)$$

正是代码里那一行。官方的讲法更直白：后缀操作同时作用于相邻两人，**不改变他们的原始身高差**，所以直接用原始身高逐对比较，垫高次数乘后缀长累加——与"增量非降"推导殊途同归。注释里被划掉的 `det` 版本是想维护"整体偏移量"的写法，写了一半发现根本不用——增量公式只用原数组的相邻差。这题单看比 J 还短，就是公式里乘的 $(n-i+1)$ 需要一步"增量求和 ↔ 后缀操作"的转换。

## M - 矩阵猎手
https://ac.nowcoder.com/acm/contest/141369/M

> 对手生成 $n \times m$ 矩阵，每格填 $[1,k]$ 的整数。你要提前选定 $n, m$，保证无论对手怎么填，都能从中删掉若干行、若干列（行列不要求连续）得到一个 $2$ 行 $b$ 列、全部数字相同的子矩阵。行数相同时选列数最少的。输出 $n, m$ 对 $10^9+7$ 取模的结果。$1 \le b,k \le 10^5$。

**输入**

一行两个整数 $b, k$。

**输出**

一行两个整数：$n \bmod (10^9{+}7)$ 和 $m \bmod (10^9{+}7)$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll mod = 1e9+7;
ll b,k,n,m;

//

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>b>>k;
	n = k + 1;
	ll p = (k * (k + 1) / 2) % mod;
	m = p * (k % mod) % mod * ((b - 1) % mod) % mod;
	m = (m + 1) % mod;
	cout<<n % mod<<' '<<m % mod;
	return 0;
}
```

### 思路解析

答案：$n = k+1$，$m = k \cdot \binom{k+1}{2} \cdot (b-1) + 1$。

**行数的下界**：若 $n \le k$，对手让每列的 $n$ 个数互不相同（$k$ 种颜色够用），任何一列内部都没有相等对，$2 \times b$ 的全相等子矩阵永远凑不出来。所以 $n \ge k+1$。

**$n=k+1$ 时 $m$ 的充分性**：每列有 $k+1$ 个格、只有 $k$ 种颜色，鸽巢原理保证每列至少有一对行 $(i,j)$ 取值相等，不妨说这列"贡献"了一个组合（行对，颜色）。这样的组合共 $k \cdot \binom{k+1}{2}$ 种；当列数 $m > k\binom{k+1}{2}(b-1)$ 时，必有某个组合被至少 $b$ 列贡献——这 $b$ 列在第 $i,j$ 两行上全都是同一个值，拼起来就是 $2 \times b$ 的全相等子矩阵。

**$m$ 的下界**：对手给每列指定一个（行对，颜色）组合，让每个组合最多出现 $b-1$ 次；组合外的 $k-1$ 行从剩下 $k-1$ 种颜色里每行填互不相同的值，就不会产生额外的相等对。于是 $m = k\binom{k+1}{2}(b-1)$ 时可以躲掉，答案恰为 $+1$。官方题解把这半步的构造也写全了，并与我的推导完全一致；末尾还特意提醒"代码看起来很简单对不对，不要以代码取题"。

样例 $b=2,k=2 \Rightarrow n=3,\ m = 2\cdot 3\cdot 1+1 = 7$ 吻合。顺带一提，文件夹里躺着的另一版草稿数的是"行对"而漏乘了颜色维 $k$，得到 $\binom{k+1}{2}(b-1)+1$，代样例得 4，直接排除——**鸽巢时漏一个维度，答案就差一个数量级**。

取模注意：$k(k+1)$ 必为偶数，先除以 2 再取模。

## N - 小h的地毯(hard)
https://ac.nowcoder.com/acm/contest/141369/N

> 输入与 easy 完全一致，问法改为：$(x,y)$ 处**最早**铺的地毯是什么颜色（没有则输出 0）。

**输入**

同 K：$1 \le n\cdot m \le 10^6$，$1 \le q,k \le 10^5$。

**输出**

每个询问一行，最底层地毯的颜色（没有则 0）。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e6+10;
 
//2h 43min 剩17min
//嘶 我是真的不会 看起来二分查找点集来确认好像并不行？
//实施暴力优化？试试跳表？这个样可以快速的查找下一个矩阵边界在哪里
//但是如果分别在x y 方向上面进行跳跃似乎并不行？？因为没法判断是不是同一个矩阵？
//等一下 我只需要知道最先的这个点就行了 我们不用管是不是同一个矩阵 因为先铺的不能被后铺的覆盖
//所以只要按时间顺序铺 遇到还没被覆盖的格子就填色 覆盖过的就跳过！这样就像在维护一个不断扩大的不规则的块
//问题是怎么快速跳过已覆盖的格子??????
//等一下 我们的问题在于 无法判断是不是一个矩阵 
//或许我们可以 每行维护一个下一个未覆盖列的并查集？？？ 我去 好像可行啊 只要加个路径压缩
//返回第 i 行从 j 开始下一个没被覆盖的列
//覆盖完就把 nxt[id] 指向 j+1 路径压缩？ 应该是可以了每个格子只填一次 总复杂度 O(nm)
//妈的唐比又开始调试路径查询辩解了 我是个傻逼
//妈的怎么老是递归出问题样例都过不了 改成你腿试试
//不管了没时间了 恁过样例 先交一次试试
//剩1min
//最后一个点TLE 25/30

int n,m,q,k;
int gr[maxn];
int nx[maxn];
 
inline int id(int x,int y){return (x-1)*(m+1) + (y-1);}
 
int fd(int x,int y){
    int root = y;
    while(nx[id(x,root)] != id(x,root)){
        root = nx[id(x,root)] - (x-1)*(m+1) + 1;
    }
    int cur = y;
    while(cur != root){
        int nxt = nx[id(x,cur)] - (x-1)*(m+1) + 1;
        nx[id(x,cur)] = id(x,root);
        cur = nxt;
    }
    return root;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m>>q>>k;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m+1;j++){
            nx[id(i,j)] = id(i,j);
        }   
    }
 
    for(int t=1;t<=q;t++){
        int x1,y1,x2,y2,c;
        cin>>x1>>y1>>x2>>y2>>c;
        for(int i=x1;i<=x2;i++){
            int j = y1;
            while(1){
                j = fd(i,j);
                if(j > y2) break;
                gr[id(i,j)] = c;
                nx[id(i,j)] = id(i,j+1);
                j++;
            }
        }
    }
 
    while(k--){
        int x,y;
        cin>>x>>y;
        cout<<gr[id(x,y)]<<'\n';
    }
 
    return 0;
}
```

### 思路解析与补题

**赛时做法（25/30）**：按时间顺序铺地毯，每个格子只染"最早覆盖它的那块"，已覆盖的格子用并查集跳过——每行维护"从列 $j$ 开始下一个未覆盖列"的指针（路径压缩），单点染色时把指针指向下一列。每个格子至多被染一次，染色部分是 $O(nm\,\alpha)$。

**TLE 的原因**：除了染色，外层还要对每个矩形逐行访问 `for i = x1..x2`。染色次数有 $nm \le 10^6$ 的保证，**但"逐行访问"的总次数没有任何上界**——比如 $n=10^6, m=1$、$q=10^5$ 个全高矩形，第一块把所有格子染完之后，后面每个矩形仍要把 $10^6$ 行全部扫一遍，共 $10^{11}$ 次行访问。赛后本地构造了这组数据实测：原版 30 秒跑不完，正好对应最后一个点 TLE。

**补题修复**：出题人在官方题解里先承认了"数据有些弱，放过了优化过的暴力，在此致歉"，然后给出了官方补丁——**行列反转**：$n > m$ 时交换两维，保证行数不超过 $\sqrt{nm} \approx 1000$，单个矩形的行枚举就压到 $10^3$，总量回到 $10^8$ 级别。我的补法是另一个方向的补丁，且不依赖数据：再加一个"行并查集" `nrow[i]` = 第 $i$ 行之后第一个"还有未覆盖格子"的行。一行什么时候算铺满？`fd(i, 1) > m`（从第 1 列开始跳已经是界外）——此时把该行从 `nrow` 里 splice 掉。矩形枚举行时从 `frow(x1)` 起步，铺满的行 $O(\alpha)$ 跳过。两个补丁正交，任选其一都能救回最后那个点；行并查集版在上述极端数据下 0.05s，与原版在 30 组随机小数据上输出完全一致：

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e6+10;
int n,m,q,k;
int gr[maxn];
int nx[maxn];
int nrow[maxn]; // nrow[i]: 第 i 行之后第一个仍有未覆盖格子的行
inline int id(int x,int y){return (x-1)*(m+1) + (y-1);}
int fd(int x,int y){
    int root = y;
    while(nx[id(x,root)] != id(x,root)) root = nx[id(x,root)] - (x-1)*(m+1) + 1;
    int cur = y;
    while(cur != root){
        int nxt = nx[id(x,cur)] - (x-1)*(m+1) + 1;
        nx[id(x,cur)] = id(x,root);
        cur = nxt;
    }
    return root;
}
int frow(int x){
    if(nrow[x] == x){
        if(fd(x,1) > m) nrow[x] = x+1;   // 整行铺满，splice 掉
    }else nrow[x] = frow(nrow[x]);
    return nrow[x];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m>>q>>k;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m+1;j++) nx[id(i,j)] = id(i,j);
    for(int i=1;i<=n+1;i++) nrow[i] = i;
    for(int t=1;t<=q;t++){
        int x1,y1,x2,y2,c;
        cin>>x1>>y1>>x2>>y2>>c;
        int i = frow(x1);
        while(i <= x2){
            int j = fd(i, y1);
            while(j <= y2){
                gr[id(i,j)] = c;
                nx[id(i,j)] = id(i,j+1);
                j = fd(i, j+1);
            }
            i = frow(i+1);
        }
    }
    while(k--){
        int x,y;
        cin>>x>>y;
        cout<<gr[id(x,y)]<<'\n';
    }
    return 0;
}
```

复盘一句话：**"每个元素只处理一次"的结构（染色）不等于"每个矩形只扫必要的行"**——并查集跳格子的思路是对的，只是少建了一维，逐行的那层也要有东西帮它跳。

## O - 小h的实验
https://ac.nowcoder.com/acm/contest/141369/O

> 一棵 $N$ 个节点的树。对全部 $2^N-1$ 个非空点集 $S$：把 $S$ 中的点都变成物质 X，X 沿边移动并融合在一个节点上，移动方案取所有 X 经过边数总和最小者；每次经过一条边产生 1 能量。求所有场景的能量总和，对 $998244353$ 取模。$2 \le N \le 3\times10^5$。

**输入**

第一行 $N$，接下来 $N-1$ 行每行一条树边 $u, v$。

**输出**

总能量对 $998244353$ 取模。

（比赛时没有来得及看，交白卷。）

### 赛后补题（自推做法，对完官方题解确认同路线）

这题赛后推出来一个 $O(N)$ 的公式，先给结论再给推导。

**结论**：设 $G(s) = \sum_{k=0}^{N} |s-k|\binom{N}{k}$，$C = N \cdot 2^{N-1}$，则

$$ans = \frac{1}{2} \sum_{e} \bigl(C - G(s_e)\bigr) \bmod 998244353$$

其中 $s_e$ 是删掉边 $e$ 后某一侧连通块的点数（$G$ 关于 $s \leftrightarrow N-s$ 对称，取哪侧都行）。

**推导**：

1. 固定场景 $S$，最优融合点是 $S$ 的中位数。此时每条边 $e$（删掉后两侧为 $A_e, B_e$）被经过的次数恰为 $\min(|S\cap A_e|,\ |S\cap B_e|)$：少数侧的每个 X 都必须过河，而中位点站在多数侧让所有边同时达到这个下界。
2. 于是总能量 $= \sum_e \sum_{S} \min(u_S, v_S)$，$u_S = |S\cap A|,\ v_S = |S\cap B|$（空集贡献 0，直接对全部 $2^N$ 个子集求和）。
3. 用 $\min(u,v) = \frac{u+v-|u-v|}{2}$ 拆开。前一半好算：$\sum_S (|S\cap A|+|S\cap B|) = \sum_S |S| = N\cdot 2^{N-1}$（每个点出现在一半的子集里）。
4. 后一半 $\sum_S \bigl||S\cap A| - |S\cap B|\bigr| = \sum_{u,v} |u-v| \binom{s}{u}\binom{N-s}{v}$。由 Vandermonde 恒等式 $\sum_{u-v=d}\binom{s}{u}\binom{N-s}{v} = \binom{N}{s-d}$，把差值 $d$ 换元成 $k = s-d$ 求和，就得到 $G(s) = \sum_k |s-k|\binom{N}{k}$——它只依赖一侧的大小 $s$，与树的形状无关！
5. $G$ 可以 $O(N)$ 递推：$G(s+1) - G(s) = 2\sum_{k\le s}\binom{N}{k} - 2^N$（$s$ 右移一格，比它小的 $k$ 各多贡献 1，比它大的各少 1）。

树上做一遍子树大小统计，逐边套公式即可。

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll mod = 998244353;

ll pw(ll b, ll e){ ll r=1; b%=mod; while(e){ if(e&1) r=r*b%mod; b=b*b%mod; e>>=1; } return r; }

int main(){
    int n;
    scanf("%d",&n);
    vector<vector<int>> g(n+1);
    for(int i=0;i<n-1;i++){
        int u,v; scanf("%d %d",&u,&v);
        g[u].push_back(v); g[v].push_back(u);
    }
    // BFS 求父序，倒序累计子树大小
    vector<int> order; order.reserve(n);
    vector<int> par(n+1,0);
    vector<char> vis(n+1,0);
    order.push_back(1); vis[1]=1;
    for(int h=0;h<(int)order.size();h++){
        int u=order[h];
        for(int v: g[u]) if(!vis[v]){ vis[v]=1; par[v]=u; order.push_back(v); }
    }
    vector<ll> sz(n+1,1);
    for(int i=n-1;i>=1;i--){ int u=order[i]; sz[par[u]] += sz[u]; }

    // G(s) = sum_k |s-k| * C(N,k)，递推：G(s+1)-G(s) = 2*P(s) - 2^N
    ll N = n;
    ll powN = pw(2,N), C = N % mod * pw(2,N-1) % mod;
    vector<ll> G(n+1);
    G[0] = C;                      // G(0) = sum k*C(N,k) = N*2^(N-1)
    ll P = 1;                      // P(0) = C(N,0)
    vector<ll> binn(n+1);          // C(N,k)
    binn[0]=1;
    for(int k=1;k<=n;k++) binn[k] = binn[k-1] % mod * ( (N-k+1) % mod ) % mod * pw(k, mod-2) % mod;
    for(int s=0;s<n;s++){
        G[s+1] = ((G[s] + 2*P - powN) % mod + mod) % mod;
        P = (P + binn[s+1]) % mod;
    }
    ll total = 0;
    for(int u=2;u<=n;u++){
        ll s = sz[u] % mod;
        total = (total + (C - G[s] % mod + mod)) % mod;
    }
    printf("%lld\n", total * pw(2, mod-2) % mod);
    return 0;
}
```

验证：三组样例（6 / 70 / 43813）全部通过；另写了 $N \le 12$ 的"枚举所有子集 + 树上中位数暴力"对拍 200 组随机树零误差；$N = 3\times10^5$ 的链 0.19s 跑完，复杂度没有问题。

赛后回看这题，难点完全在"敢不敢相信答案能把 $2^N$ 个集合拆到每条边上算"——第 1 步的中位数性质是钥匙，后面全是组合恒等式的肌肉活。对完官方题解：路线完全一致（按边贡献 → 范德蒙德卷积 → 前缀和收尾），官方把 $\sum_k \binom{N}{k}\min(k, s-k)$ 用两个前缀和逐项累加，我用 $G(s)$ 的差分递推，是同一个恒等式的两种写法。比赛时没敢开这道题，补完发现它的组成模块（中位数、Vandermonde、前缀和）全都是认识的——下次遇到"对全部 $2^N$ 个子集求和"这种题面，第一反应就该是找拆边的贡献。

---

## 赛后总结

**成绩**：重现赛打星 255 / 290，13/15（N 题 25/30），13 题 AC 全部一发过；折算正赛榜（193 人）约第 11 位。

**做得好的**：

- 全场零失败提交，罚时压力为零——所有失误都被拦在"想清楚再交"这一关之前。
- D 的构造（填 1 化成二元方程，并确认 $a=n,b=2$ 恒为解兜底）、I 的"两端删不掉 + gcd 单调"、J/L 增高垫两连的增量推导，这些需要一小步证明的题全部一次写对。
- N 在 15 分钟内完成"首次覆盖染色 + 逐行并查集"的完整实现，方向和框架都是对的，输的只是复杂度的最后一维。

**不足**：

1. **K 题读题（-1 小时）**：把 $n \cdot m \le 10^6$ 看成 $n, m \le 10^6$，在"这不可能做得出来"的错误前提里耗了整整一小时。加上苏州场的"封榜 + 交错题"，连续两场的最大失误都出在信息核对上。规则升级：开题先把数据范围抄进注释，卡题超过 20 分钟时回头重读一遍题面。
2. **N 题复杂度论证只做了一半（-5 分）**：证明了"每个格子最多染一次"（有效工作量有界），没有检查"每个矩形逐行枚举"这个无效枚举量——它没有任何上界，高矩形堆起来就是 $10^{11}$。并查集类解法的通病：跳了一维忘了另一维。补题版加一个行并查集，0.05s 通过，见上文。
3. **O 题零提交**：被 K 吃掉的 1 小时恰好是读完 O、推出"按边独立贡献"所需要的时间（赛后补题见上文）。执行一条新规则：卡题 40 分钟仍无进展就跳走，先把后面所有题读一遍再回来。
4. **收尾没有验证余地**：N 落笔时只剩 15 分钟，交上去那一刻就结束了。hard 版本尽量在剩 25 分钟前动手，给极端样例和复杂度复查留出时间。

O 题赛后按"中位数拆边 + Vandermonde + 差分递推"补出了 $O(N)$ 做法并通过暴力对拍，是这两场里最满意的一段补题。总体上这是一场"手稳脑快、但读题和复杂度论证两个老毛病再次现形"的比赛——两场连着看，扣分点全在流程而不是算法，这本身就是最值得记录的结论。