---
title: "AtCoder Beginner Contest 476"
date: 2026-09-19
draft: false
comments: true
---

![ABC476](/img/acm/ABC476.png)
![ABC476_submit](/img/acm/ABC476_submit.png)

Rating 728 → 803 (+75)，Rank 2335/9614，Performance 1184，Grading 7 Kyu → 6 Kyu。上绿名了！
惊心动魄，abc 全是模拟，快速写过，中间说了会话写的慢了有些可惜。看了 50 分钟 D题想了各种贪心思路，
想不出来全局贪心，去想了二分，想办法转化一下答案判定来写出来可行的二分贪心，在尝试无果后索性先去看后面的 efg，
发现 e 可以用线段树板子解决（虽然应该有更优雅的做法），（n+m） logn 应该是能过，常数可能比较大，但是可能数据比较水，
直接快速的解决出 e 题，看了看 fg 感觉不是能写出来的，索性继续回去看 d，剩 17 分钟到剩 7 分钟，一直没有思路，
但是最后在玩一组样例的时候突然发现可以通过枚举一层候选点来解决贪心不好写的问题，枚举之后强制控制了一层变量，
这样的话贪心策略是非常简单的，但是此时是 n^2 的，但是同时可以预处理前缀和每个情况剩余的钱，这样是递增的，
可以二分来快速找到下一个最优候选点，这样答案就是 nlogn的，写完代码再调了一会边界，最后 2 分钟交了一发，竟然过了！
虽然道路比较曲折，但是最后还是成功上绿名[亲亲]

## A - Appender
https://atcoder.jp/contests/abc476/tasks/abc476_a

> 给定一个由小写英文字母组成的字符串 $S$。请按以下规则确定并输出字符串 $T$：
> - 如果 $S$ 的最后一个字符是 `e`，则 $T$ 为在 $S$ 末尾追加 `r` 后得到的字符串。
> - 如果 $S$ 的最后一个字符不是 `e`，则 $T$ 为在 $S$ 末尾追加 `er` 后得到的字符串。

**输入**

输入一行字符串 $S$。

**数据范围**

- $S$ 仅由小写英文字母组成，长度在 $1$ 到 $10$ 之间。

**输出**

输出字符串 $T$。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
string s;

//1h40min 剩余时间 1 h 38 min
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>s;
	int n = s.length() - 1;
	if(s[n] == 'e') cout<<s<<"r";
	else cout<<s<<"er";
	
	return 0;
}
```

### 官方题解对比

**官方做法**：直接检查 `s.back()` 是否为 `'e'`，是则输出 `s + "r"`，否则输出 `s + "er"`。时间复杂度 $O(|S|)$。

**我的思路解读**：签到题，1 小时 40 分钟时开写，剩余时间 1 小时 38 分钟。思路和官方完全一致，用 `s[n]` 取最后一个字符判断即可。这题没啥好说的，注意读题时看清是追加 `r` 还是 `er` 就行。

## B - Wild Card
https://atcoder.jp/contests/abc476/tasks/abc476_b

> 给定两个长度为 $N$ 的字符串 $S$ 和 $T$，其中 $S$ 由小写英文字母组成，$T$ 由小写英文字母和 `*` 组成。
> 当且仅当将 $T$ 中的每个 `*` 替换为某个小写英文字母后，$T$ 能与 $S$ 相等时，我们称 $S$ 与 $T$ 匹配。
> 请判断 $S$ 是否与 $T$ 匹配。

**输入**

第一行输入整数 $N$。
第二行输入字符串 $S$。
第三行输入字符串 $T$。

**数据范围**

- $1 \le N \le 100$

**输出**

如果匹配，输出 `Yes`；否则输出 `No`。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
string s,t;
int n;

//1 h 40 min 剩余时间 1 h 33 min 在说话 读题慢了

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	cin>>s>>t;
	bool ans = 1;
	for(int i=0;i<n;i++){
		if(t[i] == '*') continue;
		if(t[i] != s[i]){
			ans = 0;
			break;
		}
	}
	if(ans) cout<<"Yes";
	else cout<<"No";
	return 0;
}
```

### 官方题解对比

**官方做法**：逐位比较，若 $T_i$ 为 `*` 则跳过，否则要求 $S_i = T_i$。时间复杂度 $O(N)$。

**我的思路解读**：1 小时 40 分钟时开写，剩余 1 小时 33 分钟，中间在说话导致读题慢了。思路和官方完全一致——遍历一遍，遇到 `*` 就跳过，否则严格比较。签到题，注意 `*` 可以匹配任意字符，所以直接跳过即可。

## C - Third Largest Number
https://atcoder.jp/contests/abc476/tasks/abc476_c

> 给定一个不小于 $3$ 的整数 $N$，以及一个长度为 $N$ 的正整数序列 $A = (A_1, A_2, \dots, A_N)$。
> 对于每个 $k = 3, 4, \dots, N$，请解决以下问题：
> - 将 $A_1, A_2, \dots, A_k$ 降序排序，然后输出排在第三位的数。

**输入**

第一行输入整数 $N$。
第二行输入 $N$ 个整数 $A_i$。

**数据范围**

- $3 \le N \le 5 \times 10^5$
- $1 \le A_i \le 10^9$

**输出**

对于每个 $k = 3, 4, \dots, N$，输出一行，表示前 $k$ 个数中第三大的数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 5e5+1;
int n;
int a[maxn];
priority_queue<int> qp;

//1h40min 剩余时间 1h18min

inline void add(int x){
	qp.push(x);
	int tmp[3];
	for(int i=0;i<3;i++) tmp[i] = qp.top(),qp.pop();
	qp.pop();
	for(int i=0;i<3;i++) qp.push(tmp[i]);
	return;
}
inline int get(){
	int tmp[3];
	for(int i=0;i<3;i++) tmp[i] = qp.top(),qp.pop();
	for(int i=0;i<3;i++) qp.push(tmp[i]);
	return tmp[2];
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=3;i++) qp.push(a[i]);
	cout<<min(min(a[1],a[2]),a[3])<<'\n';
	for(int i=4;i<=n;i++) add(a[i]),cout<<get()<<'\n';
	return 0;
}
```

### 官方题解对比

**官方做法**：用三个变量 `mx1, mx2, mx3` 动态维护前三大的值。每加入一个数，按大小关系更新这三个变量。时间复杂度 $O(N)$。

**我的思路解读**：1 小时 40 分钟时开写，剩余 1 小时 18 分钟。我用的是优先队列（大根堆）来维护，每次 `add` 时弹出前三大的值再放回去，`get` 时再弹出一次取第三个。思路本质和官方一致，但代码写得过于繁琐——官方三个变量 $O(1)$ 更新，我非要开优先队列做 $O(\log N)$ 的弹出插入。这题暴露了一个问题：**看到"动态维护前 $k$ 大"就条件反射用堆，其实 $k$ 固定为 3 时直接三个变量更简单更快**。

## D - Automat
https://atcoder.jp/contests/abc476/tasks/abc476_d

> 在 AtCoder 王国中，流通着两种面额的纸币：$1$ 美元纸币和 $K$ 美元纸币。
> 甜点自动售货机售卖 $N$ 种甜点，甜点 $i$ 售价 $A_i$ 美元。饮料自动售货机售卖 $M$ 种饮料，饮料 $j$ 售价 $B_j$ 美元。
> 付款规则：
> - 甜点售货机同时接受 $1$ 美元纸币和 $K$ 美元纸币。
> - 饮料售货机只接受 $K$ 美元纸币。
> - 两台售货机找零时均只使用 $1$ 美元纸币找零。
> - 每种商品最多只能购买一件。
>
> 高桥带着 $X$ 张 $1$ 美元纸币和 $Y$ 张 $K$ 美元纸币。求最多可以购买的商品总件数。

**输入**

第一行输入 $N, M, K$。
第二行输入 $X, Y$。
第三行输入 $N$ 个整数 $A_i$。
第四行输入 $M$ 个整数 $B_j$。

**数据范围**

- $1 \le N, M \le 2 \times 10^5$
- $1 \le K \le 10^9$
- $1 \le X, Y \le 10^9$
- $1 \le A_i, B_j \le 10^9$

**输出**

输出最多可以购买的商品总件数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int n,m,k,nowa = 1,nowb = 1;
ll a[maxn],b[maxn];
ll x,y;
ll sa[maxn],sb[maxn],kc[maxn];

//可以想到一个简单的局部贪心策略：把 A[i]和 B[i]混排 优先买 B[i]吗？
//但是全局来看 好像难以确定全局的解 
//想到昨天打得牛客竞赛 也是相似的 尝试往贪心二分的方向看 昨天也是栽在全局贪心的做法上的
//那么想一想 怎么把物品个数转换为 确定性贪心？
//突然想到一个简单贪心 不管如何 可以先排序 然后把 1 块钱全部用来买 A[i] 买完为止
//那么 接下来 就可以把 所有的一块钱视为一堆钱 注意到 A[i] B[i] 均单增 
//感性的想 为了获得尽可能多的商品 我们希望钱尽可能花完
//是否有每一次购买的时候 只需要看当前选到的 min(A[nowa],B[nowb])？
//关键在于1块钱的限制 需要想明白
//不对 好像不能一开始把一块钱全部用完？
//奶奶的 我讨厌贪心 先尝试把那个简单的思路实现一下
//40min 跳过下一题
//剩余时间 17min 全力攻克这道
//剩余时间 7min 依旧写不出来
//不怼
//可以枚举买 j 个 B 商品 剩下的钱尽量全买 A 商品
//关键在于想清楚 B 商品只能用 K 元买 找零回来的 1 元可以拿来买 A 商品
//这样买完 j 个 B 之后 剩余总价值就是 X + Y*K - sum_b[j] 然后二分找最多买几个 A
//但注意 B 用掉的 K 元个数不能超过 Y

bool check(int x){
	bool pd = 1;
	
	return pd;
}
int solve1(){
	int l=0,r=maxn*2,mid=0,ans=0;
	while(l <= r){
		mid = l + (r - l) / 2;
		if(check(mid)) ans = mid,l = mid + 1;
		else r = mid - 1;
	}
	return ans;
}
inline int pre(){
	int cnt = 0;
	while(x >= a[nowa]) x -= a[nowa++],cnt++;
	if(nowa > 1) nowa--; 
	return cnt;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n>>m>>k;
	cin>>x>>y;
	for(int i=1;i<=n;i++) cin>>a[i];
	sort(a+1,a+1+n);
	for(int i=1;i<=m;i++) cin>>b[i];
	sort(b+1,b+1+m);
	for(int i=1;i<=n;i++) sa[i] = sa[i-1] + a[i];
	for(int i=1;i<=m;i++){
		sb[i] = sb[i-1] + b[i];
		kc[i] = kc[i-1] + (b[i] + k - 1) / k;
	}
	ll tot = x + y * k;
	ll ans = 0;
	for(int j=0;j<=m;j++){
		if(kc[j] > y) break;
		ll rem = tot - sb[j];
		int i = upper_bound(sa, sa+n+1, rem) - sa - 1;
		if((ll)i + j > ans) ans = (ll)i + j;
	}
	cout<<ans<<'\n';
	return 0;
}
```

### 官方题解对比

**官方做法**：先把所有 $K$ 元纸币换算成 $1$ 元（$X + Y \times K$），然后枚举购买的饮料数量 $j$（$0 \le j \le M$），用前缀和计算买 $j$ 个最便宜饮料的花费 `sb[j]` 和需要的 $K$ 元纸币数量 `kc[j]`。若 `kc[j] <= Y`，则剩余钱数为 `tot - sb[j]`，二分查找最多能买几个最便宜的甜点。时间复杂度 $O(M \log N)$。

**我的思路解读**：40 分钟时跳去写下一题，剩余 17 分钟回来全力攻克，剩余 7 分钟依旧写不出来。这道题我陷入了**贪心局部最优**的陷阱——总想找一个“每次买最便宜”的贪心策略，但 $K$ 元纸币和找零的限制让局部贪心无法保证全局最优。看到官方题解才恍然大悟：**枚举 $j$ 这个维度直接消除了不确定性**。枚举买 $j$ 个饮料后，剩下的问题就是纯二分了。代码本身不难，难在想到“枚举一个维度”这个转化。这题的教训和昨天牛客 B 题一模一样——**全局最优解不确定时，枚举一个关键维度，剩下的用二分/双指针解决**。

## E - Min-Max Swap
https://atcoder.jp/contests/abc476/tasks/abc476_e

> 给定一个长度为 $N$ 的排列 $P = (P_1, P_2, \dots, P_N)$。
> 需要进行 $M$ 次操作，第 $i$ 次操作给定区间 $[L_i, R_i]$，交换该区间内的最小值和最大值。
> 请输出 $M$ 次操作后的排列。

**输入**

第一行输入 $N, M$。
第二行输入 $N$ 个整数 $P_i$。
接下来 $M$ 行，每行两个整数 $L_i, R_i$。

**数据范围**

- $1 \le N, M \le 2 \times 10^5$

**输出**

输出 $M$ 次操作后的排列 $P$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int n,m;
int p[maxn];
struct tree{
	int maxx,minn;
	int maxxunder,minnunder;
}t[maxn<<2];
inline int lx(int x){return x<<1;}
inline int rx(int x){return x<<1|1;}

//能不能用线段树来写 看起来可以 可以用线段树维护一段区间的最大值和最小值以及他们的下标 只需要处理交换这一个操作即可
//我觉得这个思路没啥问题 时间复杂度分析 O((m + n) log n) 应该是可以的 不需要时间戳来优化应该
//加上AI给我的板子 写出来的 一定要在赛后补一下线段树的写法
//应该是能用到一些排列的性质的 没有AI板子我肯定挑不出来这个代码 所以必须复盘!!
//1h40min 剩余时间 23min

void build(int x,int l,int r) {
	if(l == r){
		t[x].maxx = t[x].minn = p[l];
		t[x].maxxunder = t[x].minnunder = l;
		return;
	}
	int mid = (l + r) >> 1;
	build(lx(x), l, mid);
	build(rx(x), mid + 1, r);
	if(t[lx(x)].minn < t[rx(x)].minn){
		t[x].minn = t[lx(x)].minn;
		t[x].minnunder = t[lx(x)].minnunder;
	}else{
		t[x].minn = t[rx(x)].minn;
		t[x].minnunder = t[rx(x)].minnunder;
	}
	if(t[lx(x)].maxx > t[rx(x)].maxx){
		t[x].maxx = t[lx(x)].maxx;
		t[x].maxxunder = t[lx(x)].maxxunder;
	}else{
		t[x].maxx = t[rx(x)].maxx;
		t[x].maxxunder = t[rx(x)].maxxunder;
	}
}

tree query(int x, int l, int r, int ql, int qr) {
	if(ql <= l && r <= qr) return t[x];
	int mid = (l + r) >> 1;
	if(qr <= mid) return query(lx(x), l, mid, ql, qr);
	if(ql > mid) return query(rx(x), mid + 1, r, ql, qr);
	tree a = query(lx(x), l, mid, ql, qr);
	tree b = query(rx(x), mid + 1, r, ql, qr);
	tree c;
	if(a.minn < b.minn){
		c.minn = a.minn;
		c.minnunder = a.minnunder;
	}else{
		c.minn = b.minn;
		c.minnunder = b.minnunder;
	}
	if(a.maxx > b.maxx){
		c.maxx = a.maxx;
		c.maxxunder = a.maxxunder;
	}else{
		c.maxx = b.maxx;
		c.maxxunder = b.maxxunder;
	}
	return c;
}

void update(int x, int l, int r, int pos) {
	if(l == r){
		t[x].maxx = t[x].minn = p[l];
		t[x].maxxunder = t[x].minnunder = l;
		return;
	}
	int mid = (l + r) >> 1;
	if(pos <= mid) update(lx(x), l, mid, pos);
	else update(rx(x), mid + 1, r, pos);
	if(t[lx(x)].minn < t[rx(x)].minn) {
		t[x].minn = t[lx(x)].minn;
		t[x].minnunder = t[lx(x)].minnunder;
	}else{
		t[x].minn = t[rx(x)].minn;
		t[x].minnunder = t[rx(x)].minnunder;
	}
	if(t[lx(x)].maxx > t[rx(x)].maxx) {
		t[x].maxx = t[lx(x)].maxx;
		t[x].maxxunder = t[lx(x)].maxxunder;
	}else{
		t[x].maxx = t[rx(x)].maxx;
		t[x].maxxunder = t[rx(x)].maxxunder;
	}
}

void treeswap(int l, int r) {
	tree res = query(1, 1, n, l, r);
	int im = res.minnunder;
	int ix = res.maxxunder;
	if(im != ix) {
		swap(p[im],p[ix]);
		update(1,1,n,im);
		update(1,1,n,ix);
	}
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>p[i];
	build(1, 1, n);
	while(m--){
		int l,r;
		cin>>l>>r;
		treeswap(l,r);
	}
	for(int i=1;i<=n;i++) cout<<p[i]<<' ';
	
	return 0;
}
```

### 官方题解对比

**官方做法**：线段树维护区间最小值和最大值及其下标，每次操作查询区间最值后交换，再单点更新。时间复杂度 $O((N + M) \log N)$。

**我的思路解读**：1 小时 40 分钟时开写，剩余 23 分钟。思路和官方完全一致——线段树维护区间最值，交换后更新。但代码是**照着 AI 给的板子写的**，赛后必须复盘线段树的写法。这题暴露了一个严重问题：**线段树的 `build`、`query`、`update` 三个函数我无法独立写出**。虽然思路对了，但依赖 AI 板子才实现出来，等于没做。排列的性质（交换最值）在这个题里其实没用上，就是纯线段树模板题。赛后一定要把线段树的常见模板（区间最值 + 单点修改）默写几遍。

## F

https://atcoder.jp/contests/abc476/tasks/abc476_f

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 5e5+1;

//1h40min 剩余时间 1h18min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	return 0;
}
```

## G

https://atcoder.jp/contests/abc476/tasks/abc476_g

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 5e5+1;

//1h40min 剩余时间 1h18min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	return 0;
}
```

---

## 赛后总结

Rating 728 → 803 (+75)，Performance 1184，Grading 7 Kyu → 6 Kyu，Rank 2335/9614。5 题 AC，D 题没怼出来。

**A/B/C** 三题都是签到，思路和官方完全一致，但 C 题用优先队列写复杂了，三个变量就够了。

**D 题** 是这场比赛最大的教训。我陷入了“每次买最便宜”的局部贪心陷阱，但 $K$ 元纸币和找零的限制让局部贪心无法保证全局最优。官方题解的思路是**枚举买 $j$ 个饮料**，把这个维度确定后，剩下的就是纯二分问题。这和我昨天牛客 B 题的教训一模一样——**全局最优不确定时，枚举一个关键维度**。

**E 题** 思路对了，线段树维护区间最值 + 单点更新，但代码是照着 AI 板子写的。赛后必须复盘线段树的 `build`、`query`、`update` 三个函数的写法，不能再依赖板子了。

**F/G** 没时间看，下一场再战。