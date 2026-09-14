---
title: "Codeforces Round 1120 (Div. 2)"
date: 2026-09-12
draft: false
comments: true
---

![CF1120Div2](/img/acm/CF1120Div2.png)
![CF1120Div2_submit](/img/acm/CF1120Div2_submit.png)

超级熬大夜

## A. Min Max Game
https://codeforces.com/contest/2263/problem/A

> Bessie 和 Elsie 在一个二进制数组 $a$ 上玩游戏。Bessie 先手，两人轮流操作。每回合，玩家选择两个相邻的元素 $x$ 和 $y$，将它们替换为单个值 $\max(x, y)$（Bessie 的回合）或 $\min(x, y)$（Elsie 的回合）。当数组只剩下一个元素时游戏结束。如果最终元素为 $1$ 则 Bessie 获胜，如果为 $0$ 则 Elsie 获胜。假设双方都采取最优策略，判断谁获胜。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$2 \le n \le 50$）。
第二行包含 $n$ 个整数 $a_i$（$0 \le a_i \le 1$）。

**输出**

对于每个测试用例，输出获胜者：`Bessie` 或 `Elsie`。


**数学推导**：

如果数组中不存在 $0$，则 Bessie 显然获胜；如果不存在 $1$，则 Elsie 显然获胜。

当 $0$ 和 $1$ 同时存在时，轮到 Bessie 时她可以移除一个 $0$，轮到 Elsie 时她可以移除一个 $1$。因此，如果 $1$ 的数量 $\ge$ $0$ 的数量，Bessie 将获胜，因为她总能确保 $1$ 的数量 $\ge$ $0$ 的数量。如果 $1$ 的数量 $<$ $0$ 的数量，那么无论 Bessie 做什么，游戏都会翻转到 Elsie 拥有同样的获胜局面，因此她将输掉比赛。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 110;
int n,t;
int a[maxn];
bool ans;

//总时间 3h 剩余时间 2h 33min
//怎么上来就是神秘博弈论 对于A 肯定要尽可能保住尽可能多的 1 以及减少 0（看图分析结果来源） B则是相反
//同是分析这个先后手是否和序列长度有关？你不能简单地看作只和数量有关 必胜局面就是全是0 或 全是1 （全是0多一个1或多个1可以转变为全是0）
//对于A 操作的时候 只要有 0 和 1 就可以减少一个0 和序列长度 和位置无关
//唐逼了 竟然想了这么久

void solve(){
	int cnt1 = 0,cnt0 = 0,lenwho = n & 1;
	for(int i=1;i<=n;i++){
		if(a[i] == 1) cnt1++;
		else cnt0++;
	}
//	if(cnt1 > cnt0) ans = 1;
//	else if(cnt1 < cnt0) ans = 0;
//	else if(lenwho) ans = 0;
//	else ans = 1; 
	if(cnt1 >= cnt0) ans = 1;
	else ans = 0;
	return;	
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i];
		ans = 0;
		solve();
		if(ans) cout<<"Bessie"<<'\n';
		else cout<<"Elsie"<<'\n';
	}
	
	return 0;	
}
```
/*
比赛时 3 小时剩余 2 小时 33 分钟完成。核心结论：若 $1$ 的数量 $\ge$ $0$ 的数量，Bessie 必胜，否则 Elsie 必胜。
*/

## B. Min Matrices
https://codeforces.com/contest/2263/problem/B

> 给定两个整数 $n$ 和 $k$。构造一个 $n \times n$ 的矩阵，填入 $1$ 到 $n^2$ 的所有整数，使得每一行和每一列的最小值构成的集合大小恰好为 $k$。如果不存在，输出 $-1$。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例包含两个整数 $n$ 和 $k$（$1 \le n \le 1000$，$1 \le k \le n^2$）。

**输出**

对于每个测试用例，如果存在合法矩阵，输出 $n$ 行，每行 $n$ 个整数；否则输出 $-1$。

**数学推导**：

每个数最多只能是一行和一列的最小值。因此，行最小值有 $n$ 个，列最小值有 $n$ 个，它们的并集大小 $k$ 必须满足：

- $k \ge n$：因为 $1$ 一定是某行和某列的最小值，交集至少为 $1$，所以并集大小 $k = 2n - |\text{交集}| \le 2n - 1$。
- 同时并集大小至少为 $n$（因为行最小值集合本身就有 $n$ 个元素）。

因此必要条件为 $n \le k \le 2n-1$。

构造时令 $x = k - n + 1$（$1 \le x \le n$），将 $1, 2, \dots, x$ 填入第一行，$x+1, \dots, 2x-1$ 填入第一列，$2x, \dots, k$ 填入对角线，空白处填入 $k+1, \dots, n^2$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t,k;
bool pd = 1;
int a[1005][1005];

//B 和 C1 双开 头痛有如蟒蛇缠绕般的窒息感
//总时间 3h 剩余时间 
//题意很明了 把1-n^2的数字填入矩阵 并让每一行和列的最小值恰好等于k只出现一次
//n<=1000不能暴力搜索
//布豪怎么又是构造 我是真力竭了
//怎么感觉比C1还好写一些呢？ 只需要考虑什么时候无解
//并且有一种猜测 那就是只有k<1||k>n^2的时候才无解 其他时候一律有解？
//1h 32min 跳.过去看其他题目
//妈的 刚刚那个猜测是错的
//重新想想 行最小有n个 列最小有n个 它们的并集大小是k
//全局最小1 一定同时是某行最小和某列最小 所以交集至少是1
//并集 = 2n - 交集 所以 k <= 2n-1
//同时交集最多是n 所以 k >= 2n-n = n
//所以 k 必须在 n 到 2n-1 之间 妈的 这么简单的上下界我看了半天
//然后构造 令 m = 2n-k 就是交集大小 恰好是最小值!!
//发现对角线填 1..m 这些同时是行最小和列最小？
//不妨定义第1列剩下的位置填 m+1-n 只是列最小
//第1行剩下的位置填 n+1-2n-m 只是行最小
//剩下的位置随便塞大数字 反正都比已经放的最小值大 影响不了最小值
//3 5
/*
1 4 5
2 6 7
3 8 9
*/
//并起来1 2 3 4 5 大小5
//我日 这么简单 我前面在干嘛
//1h 09min 要昏迷了 太困了

void solve(){
	if(k < n || k > 2*n - 1){
		pd = 0;
		return;
	}
	int m = 2*n - k;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			a[i][j] = 0;
		}
	}
	for(int i=1;i<=m;i++) a[i][i] = i;
	for(int i=m+1;i<=n;i++) a[i][1] = i;
	for(int j=m+1;j<=n;j++) a[1][j] = n + j - m;
	int cur = 2*n - m + 1;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(a[i][j] == 0){
				a[i][j] = cur++;
			}
		}
	}
	pd = 1;
	return;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n>>k;
		pd = 1;
		solve();
		if(pd){
			for(int i=1;i<=n;i++){
				for(int j=1;j<=n;j++){
					cout<<a[i][j]<<' ';
				}
				cout<<'\n';
			}		
		}
		else cout<<-1<<'\n';
	}
	
	return 0;	
}
```
/*
1 小时 32 分钟完成。关键结论：$k$ 必须在 $[n, 2n-1]$ 范围内。构造方法：令 $m = 2n-k$，对角线填 $1..m$，第一列下方填 $m+1..n$，第一行右侧填 $n+1..2n-m$，其余位置填大数字。
*/

## C1. Floor of MEX (Easy Version)
https://codeforces.com/contest/2262/problem/A1

> 给定一个长度为 $n$ 的数组 $a$，其中 $a_k = \text{mex}(B / k)$（即对数组 $B$ 中每个元素除以 $k$ 向下取整后得到的集合的 MEX）。构造一个可行的数组 $B$（可以为空），使得对于所有 $k$，$\text{mex}(B / k) = a_k$。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$1 \le n \le 10^5$）。
第二行包含 $n$ 个整数 $a_i$。

**输出**

对于每个测试用例，第一行输出 $m$（数组 $B$ 的大小），第二行输出 $m$ 个整数表示 $B$。

**数学推导**：

设 $f(A, k) = x$。我们知道 $S$ 在每个区间 $[0, k-1], [k, 2k-1], \dots, [k(x-1), kx-1]$ 中至少包含一个数，但在区间 $[kx, k(x+1)-1]$ 中没有数——称这个最后区间为“坏区间”。

对于每个 $k$，被踢掉的 $y$ 满足 $a[k] \cdot k \le y \le (a[k]+1) \cdot k - 1$。用差分标记这些坏区间，未被标记的 $y$ 就是可以加入 $B$ 的。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t,m;
int a[maxn],b[maxn];
int diff[maxn];

//总时间 3
//神秘构造题
//注意到是构造可行的 B 就行了 
//注意到 对于 k 而言 f(B,k) 是的单减的
//首先 B 不需要有重复的元素 可以考虑人为的 让 B 单增
//那么现在就是要确定f(B,k) = mex(B[i]/k)的转化方式
//保证 B 一定有解 
//我日 我好像不会 2h 1min
//反过来想一想 若已确定 m 那么对于每一个k 可以确定他的 b[i]/k 情况 (mex一定在[0,m]!!)
//所以我们可以通过 a[](mex)的最大值来确定m的大小 当然 这不是一个严格的上界
//卧槽了 完全没有头绪啊 妈的 昨天不应该熬夜的 太几把困了
//注意到如果 m 一定 那么对于每
//1h42min跳题

//我日 想了想 其实很简单
//注意到 a[k] = mex(b[i]/k) 说明 a[k] 本身不在这个集合里
//也就是说 对于原来的 A 里任意 y 和任意 k 都有 floor(y/k) != a[k]
//那么 我们构造 B 的时候 只要把所有会让 floor(y/k)=a[k] 的 y 全部踢掉
//剩下的 y 全塞进 B 里 就一定满足
//为什么？因为原来的 A 一定在这些剩下的 y 里（A 的元素不会产生 a[k]）
//所以所有小于 a[k] 的商都还在 B 里 同时 a[k] 不会出现 所以 mex 就是 a[k]
//妈的 就这么简单 我是笨猪 下次不要再熬夜写比赛了 力竭了
//对于每个 k 被踢掉的 y 满足 a[k]*k <= y <= (a[k]+1)*k-1
//直接差分标记 没被标记的就是答案

//1h 24min

void solve(){
	
	for(int i=0;i<=n;i++) diff[i]=0;
	for(int k=1;k<=n;k++){
		ll L=1LL*a[k]*k;
		if(L>n-1) continue;
		ll R=1LL*(a[k]+1)*k-1;
		if(R>n-1) R=n-1;
		diff[(int)L]++;
		diff[(int)R+1]--;
	}
	m = 0;
	int cur = 0;
	for(int y=0;y<=n-1;y++){
		cur += diff[y];
		if(cur == 0) b[++m]=y;
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i];
		solve();
		cout<<m<<'\n';
		for(int i=1;i<=m;i++) cout<<b[i]<<' ';
		cout<<'\n';
	}
	return 0;	
}
```
/*
1 小时 42 分钟跳题，1 小时 24 分钟在提示下完成。核心洞察：$a[k] = \text{mex}(B/k)$ 意味着 $a[k]$ 本身不在 $B/k$ 中，所以只需排除所有使 $\lfloor y/k \rfloor = a[k]$ 的 $y$，剩下的就是答案。
*/

## C2. Floor of MEX (Hard Version)
https://codeforces.com/contest/2262/problem/A2

> 题意与 C1 相同，但要求统计合法数组 $B$ 的数量（对 $998244353$ 取模）。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1,mod = 1e9+7;
int n,t;


//把题目都看了一遍 决定c2和D双开 E和F看了之后碰都不想碰
//看起来两个的暴力都比较好实现 但是优化上面就要费脑子了
//思考什么会限制B的上下界 在C1里面我们只是说B存在解的时候是个什么样子
//这个B不是任意的吗？？？还是我理解有问题 比如B可以通过出现重复的元素来达到一直扩张的情况啊
//嘶 好像和每一个k而言要计算什么东西？禁用一个区间？ 这样似乎对于每一个k会限制可行的m的范围以及b[i]的具体数值？
//妈的 真想不出来了

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
			
	}
	
	return 0;	
}
```

## D. Culling Game
https://codeforces.com/contest/2262/problem/B

> 有 $n$ 个对手，第 $i$ 个对手的技能值为 $a_i$。游戏按顺序进行 $n$ 轮，每轮移除一个对手。你的角色初始技能为 $0$。每当你的角色遇到一个对手，如果当前技能值小于该对手的技能值，则你的技能值变为该对手的技能值；否则你的技能值保持不变。求每轮移除后，你的角色最终技能值。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$1 \le n \le 2 \times 10^5$）。
第二行包含 $n$ 个整数 $a_i$。
第三行包含 $n$ 个整数 $p_i$，表示每轮移除的对手编号。
所有测试用例的 $n$ 之和不超过 $2 \times 10^5$。

**输出**

对于每个测试用例，输出 $n$ 个整数，表示每轮移除后的最终技能值。

**数学推导**：

将移除操作反过来变成插入。维护一个集合 $S$，存储当前冠军（即被吸收的对手）的下标。当在位置 $i$ 插入一个对手时，找到 $S$ 中最大的 $j < i$。如果从 $j$ 到 $i-1$ 的所有活跃对手的技能值之和小于 $a_i$，则将 $i$ 插入 $S$。否则，当前冠军会吸收这个对手。

用线段树维护区间和，支持快速查询和插入。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+5;
int n,t;
ll a[maxn];
int p[maxn];

//D题 暴力很好想 直接模拟这个过程就行了 但是o(n^2) 绝对超时
//我日 是真的不好想这个优化
//花了快半个小时 我jb是个猪吧 
//想到当时省队集训的时候一道线段树维护徐健查询的部分 可以用来优化修改动态取件模拟的问题
//每次删元素们 麻烦 那能不能用一下莫多分块的思路：离线处理？
//从空集开始 倒序把删掉的元素加回去 注意到每次问当前有几个冠军 可以反复被利用
//那么线段树维护每个节点存它这个区间的冠军列表
//反过来的时候 合并的时候 左儿子的最后一个冠军会去吸收右儿子前面的冠军
//如果左冠军的累计值 >= 右冠军的初始值 就能吸
//吸完之后累计值加上右冠军的累计值 继续往后吸
//吸不动了就把右边剩下的冠军接上来
//大分一半的调试代码过程 我jb要死了
//注意！！！！！！！！！！！左冠军能吸右冠军 是因为右冠军块里所有元素都 <= 右冠军的初始值
//而左冠军累计值已经 >= 右冠军初始值 所以一路都能吸过去
//妈的还有单调栈吗？我真力竭了 我真不想写了 也懒得写lazy了 眼睛疼头痛 要死了 应该是 O(n log n)
//也不想分析正确性了 就这么做吧 诡异优化的暴力模拟
//剩余时间 19min
//最后也没想出来C2怎么写
//TLE了 怀疑是找左冠军的时候每一次线性扫描导致的
//优化 每个节点只存每个冠军的初始值和 累计值的前缀和 发现都是单证的！！！！！！！
//可以二分！！！但是非常男鞋这个合并
//chv 严格递增是能用二分的根本原因！！！！！
//妈的这个代码是真的难调 又滑又重构了一次 C2基本是没时间了 早知道不报这一场了 要不是怕掉分谁会想在军训的时候熬夜调试代码 我真快死了要
//妈的还是tle 我放弃了 太基本难受了

struct node{
    vector<ll> chv;
    vector<ll> cps;
};

node tree[4*maxn];

node merge(node &lef, node &rig){
    if(lef.chv.empty()) return rig;
    if(rig.chv.empty()) return lef;
    node res;
    res.chv = lef.chv;
    res.cps = lef.cps;
    ll last = res.cps.back() - (res.cps.size() >= 2 ? res.cps[res.cps.size()-2] : 0);
    ll cur = last;
    int pos = upper_bound(rig.chv.begin(), rig.chv.end(), cur) - rig.chv.begin();
    if(pos > 0) cur += rig.cps[pos-1];
    while(pos < (int)rig.chv.size() && rig.chv[pos] <= cur){
        cur += rig.cps[pos] - (pos > 0 ? rig.cps[pos-1] : 0);
        pos++;
    }
    res.cps.back() = (res.cps.size() >= 2 ? res.cps[res.cps.size()-2] : 0) + cur;
    for(int i=pos;i<(int)rig.chv.size();i++){
        res.chv.push_back(rig.chv[i]);
        ll one = rig.cps[i] - (i > 0 ? rig.cps[i-1] : 0);
        res.cps.push_back(res.cps.back() + one);
    }
    return res;
}

void build(int id,int l,int r){
    if(l == r){
        tree[id].chv = {a[l]};
        tree[id].cps = {a[l]};
        return;
    }
    int mid = (l+r)/2;
    build(id*2,l,mid);
    build(id*2+1,mid+1,r);
    tree[id] = merge(tree[id*2], tree[id*2+1]);
    return;
}

void del(int id,int l,int r,int pos){
    if(l == r){
        tree[id].chv.clear();
        tree[id].cps.clear();
        return;
    }
    int mid = (l+r)/2;
    if(pos <= mid) del(id*2,l,mid,pos);
    else del(id*2+1,mid+1,r,pos);
    tree[id] = merge(tree[id*2], tree[id*2+1]);
    return;
}

void solve(){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++) cin>>p[i];
    
    build(1,1,n);
    
    for(int i=0;i<=n-1;i++){
        cout<<(int)tree[1].chv.size()-1<<' ';
        del(1,1,n,p[i+1]);
    }
    cout<<'\n';
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin>>t;
    while(t--){
        solve();
    }
    
    return 0;	
}
```
/*
剩余时间 19 分钟。线段树维护冠军列表，每个节点存储冠军的初始值和累计值前缀和。合并时左冠军吸收右冠军，但最终 TLE，未能优化到 O(n log n)。
*/

## E. Paired Bracket Sequences
https://codeforces.com/contest/2262/problem/E

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;


//总时间 3h 剩余时间 2h min
//

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
			
	}
	
	return 0;	
}
```

## F. Rank Removal
https://codeforces.com/contest/2262/problem/F

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;


//总时间 3h 剩余时间 2h min
//

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
			
	}
	
	return 0;	
}
```