---
title: "牛客小白月赛138（重现赛 VP）"
tags: [nowcoder, 题解]
date: 2026-10-09T22:22:00+08:00
draft: false
comments: true
upsolve:
  - problem: "D"
    name: "Light up the Graph"
    url: "https://ac.nowcoder.com/acm/contest/141859/D"
    status: "wrong"
    note: "计时结束后才写完的贡献法（与官方一致、样例过），自标需补"
  - problem: "E"
    name: "Rock-Paper-Scissors String Game"
    url: "https://ac.nowcoder.com/acm/contest/141859/E"
    status: "skip"
    note: "题面看了没写；官方结论：存在左端胜右端的子串则 Alice 必胜"
  - problem: "F"
    name: "Permutation of RBS"
    url: "https://ac.nowcoder.com/acm/contest/141859/F"
    status: "wrong"
    note: "剩 10 分钟写完的 n!/∏sz（与官方方法相同、样例手推全过），计时边缘未确认，自标需补"
---

比赛时间：2026-10-09 22:22 ~ 00:22（重现赛 VP，共 2h）｜正赛当晚先围观了一会儿榜，然后开重现赛打

**做题情况**

- 22:23 A 过（开局，剩 1h58）
- 22:53 B 过（剩 1h30）
- 23:59 C 过（剩 22min，B 到 C 卡了一个多小时）
- 00:24 F 写完（剩 10min，计时边缘）
- 00:33 D 写完（剩 1min，实际已经超出 VP 计时）
- E 题面看了没动手
- 赛后下了官方 Editorial 核对，D/F 的写法和题解一致、F 的样例手推全过，但都没在计时内确认，自标需补

VP 没有分数变动，主打一个检验状态。

## A. Sleeping Time
https://ac.nowcoder.com/acm/contest/141859/A

> CuteCube 在 $x$ 点开始睡觉，一共睡了 $t$ 小时，问几点起床（24 小时制）。

**输入**

一行两个整数 $x, t$（$0 \le x \le 23$；$1 \le t \le 50$）。

**输出**

一行一个整数 $y$（$0 \le y \le 23$），表示起床时刻。

**思路**：

时间超过 24 小时自动减掉 24，输出 $(x+t) \bmod 24$ 完事。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int x,t;

//总时间 2h 剩余时间 1h 58 min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>x>>t;
	cout<<(x+t)%24;

	return 0;	
}
```
/*
22:23 过，开局签到。
*/

## B. Is it Palindrome?
https://ac.nowcoder.com/acm/contest/141859/B

> 给出只含小写字母和 `?` 的字符串 $s$，把每个 `?` 替换成任意小写字母。判断：不论如何替换**一定是**回文串（输出 `certainly`）；不论如何替换**一定不是**回文串（输出 `impossible`）；还是**两种都可能**（输出 `possible`）。

**输入**

第一行整数 $t$（$1 \le t \le 10^4$）。
每组第一行整数 $n$（$1 \le n \le 5 \times 10^5$），第二行字符串 $s$。单个文件 $n$ 总和不超过 $5 \times 10^5$。

**输出**

对于每组数据，输出 `certainly` / `impossible` / `possible`。

**思路**：

把 s 反转成 p，逐位对比 s[i] 和 p[n-i-1]（也就是和自己镜像位比）：

- **certainly**：所有镜像位都没有 `?` 且字符相等。奇数长度时正中间那个位置自己配自己，可以是 `?`（自己跟自己永远相等）——这个点一开始写错成 n/2+1 跳过位了，改过来。
- **impossible**：存在某对镜像位是**两个不同的小写字母**——怎么替换都救不回来。
- 其余情况：某对镜像位至少一边是 `?`（且没有必死位），那这对既能填成相等也能填成不等——`possible`。注意两个都是 `?` 的也是 possible，因为可以填两个不同字符。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t;
int n;
string s,p;

//总时间 2h 剩余时间 1h 30 min

inline bool check1(){//唐
	if(n&1){
		for(int i=0;i<n;i++){
//			if(i == n/2+1) continue;//唐逼点出现了！
			if(i == n/2) continue;
			if(s[i] == '?' || p[i] == '?') return 0;//唐炸了
			else if(s[i] != p[i]) return 0;
		}
	}else{
		for(int i=0;i<n;i++){
			if(s[i] == '?' || p[i] == '?') return 0;
			else if(s[i] != p[i]) return 0;
		}
	}
	return 1;//唐
}

inline bool check2(){
	for(int i=0;i<n;i++){
		if(s[i] == '?' || p[i] == '?') continue;
		else if(s[i] == p[i]) continue;
		return 1;//唐
	}
	return 0;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n;
		cin>>s;
		p = s;
		reverse(p.begin(),p.end());
//		for(int i=0;i<n;i++) p[n-i-1] = s[i];
		if(check1()) cout<<"certainly"<<'\n';//唐
		else if(check2()) cout<<"impossible"<<'\n';
		else cout<<"possible"<<'\n';
	}

	return 0;	
}
```
/*
22:53 过。中间那个跳过位一开始手滑写成 n/2+1，样例直接把我打醒。
*/

## C. AND and OR
https://ac.nowcoder.com/acm/contest/141859/C

> 给定长度为 $n$ 的数组 $a$ 和非负整数 $k$，判断是否存在二元组 $(i,j)$（$1 \le i < j \le n$）满足 $(a_i \,\&\, a_j) + (a_i \,|\, a_j) = k$。存在则输出任意一组 $i, j$，否则输出 $-1$。

**输入**

第一行整数 $t$（$1 \le t \le 10^4$）。
每组第一行 $n, k$（$2 \le n \le 2 \times 10^5$；$0 \le k \le 10^9$），第二行 $n$ 个非负整数 $a_i$（$0 \le a_i \le 10^9$）。单个文件 $n$ 总和不超过 $2 \times 10^5$。

**输出**

存在则输出两个正整数 $i, j$（任意一组），否则输出 $-1$。

**思路**：

先按位看：某一位上 $(1,1)$ 与出来 $1$、或出来 $1$，贡献 $2$（两个 $1$ 都在这两个数里）；$(1,0)/(0,1)$ 与出来 $0$、或出来 $1$，贡献 $1$（加起来正好一个 $1$）；$(0,0)$ 贡献 $0$。所以**每一位的结论都是 $(a \& b) + (a | b)$ 等于该位上 $1$ 的总个数乘位权**——加起来就是 $(a \,\&\, b) + (a \,|\, b) = a + b$。感性理解：与是不进位加法，或处理进位，加法 = 不进位 + 进位。

于是问题变成：找两个数和恰好等于 $k$——两数之和。先写了个 $O(n^2)$ 暴力保底（solve1 注释掉了），然后 set 存 $\{$值, 下标$\}$，枚举 $i$ 查 $k - a_i$，查到的是自己就 `++it` 再看下一个。$O(n \log n)$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n,k,x,y;
int a[maxn];
bool ans;

//总时间 2h 剩余时间 22 min


//我是一头猪
//肯定跟二进制有关 设a[i] a[j]某一位二进制为xi,xj
//(0,0) (0,1) (1,0) (1,1)
//注意到 (1,1) & -> 2^k | -> 2^k     (1,0) (0,1) & -> 0 | -> 2^k       (0,0) & -> 0 | -> 0
//(1,1) -> 2^(k+1)
//惊人的注意力 注意到 (a & b) + (a | b) = a + b
//我是个傻逼吧 几把开始打个标观察一下不会发现ai + aj 正好等于 k 吗？？？？？

void solve1(){
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			if((a[i] & a[j]) + (a[i] | a[j]) == k){
				x = i,y = j;
				return;
			}
		}
	}
	return;
}

void solve2(){
//	unordered_map<int,int> pd;
	set<pair<int,int>> pd;
	for(int i=1;i<=n;i++) pd.insert({a[i],i});
	for(int i=1;i<=n;i++){
        int check = k - a[i];
//		auto it = pd.lower_bound({check, n+1});
        auto it = pd.lower_bound({check, 0});
        if(it == pd.end() || it->first != check) continue;
        if(it->second == i) {//唐
            ++it;
            if(it == pd.end() || it->first != check) continue;
        }
        x = i,y = it->second;
        return;
    }
	return;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n>>k;
		for(int i=1;i<=n;i++) cin>>a[i];
		ans = 1;
		x=-1,y=-1;
		
//		solve1();//O(n^2)
		solve2();//O(nlogn)
		//O(n)
		
		if(x==-1 || y==-1 || x == y) ans = 0;
		if(ans) cout<<x<<' '<<y<<'\n';
		else cout<<-1<<'\n';
	}

	return 0;	
}
```
/*
23:59 过，剩 22 min。这题从 B 过完开始磨了一个多小时——位运算按位分类的表早就打出来了，但"与+或=和"这个等式愣是绕了半天才敢信。剩最后 22 分钟才把两数之和的 set 写完。
*/

## D. Light up the Graph
https://ac.nowcoder.com/acm/contest/141859/D

> 给定 $n$ 个点 $m$ 条边的简单无向图（可能不连通），01 串 $s$ 表示点颜色（0 白 1 黑）。可以点亮若干个点（可以不点）。一个点的**价值** = 与它直接相连的**被点亮**的点数；整张图的**价值** = 白点总价值 − 黑点总价值。给出一种点亮方案使图的价值最大，输出点亮的点。

**输入**

第一行整数 $t$（$1 \le t \le 10^4$）。
每组第一行 $n, m$（$1 \le n \le 2 \times 10^5$；$0 \le m \le \min(\binom{n}{2}, 2 \times 10^5)$），第二行 01 串 $s$，之后 $m$ 行每行一条边 $u_i, v_i$。单个文件 $n$、$m$ 总和均不超过 $2 \times 10^5$。

**输出**

每组两行：第一行点亮的点数 $k$，第二行 $k$ 个点编号（任意一组最优解；$k=0$ 输出一行空行）。

**思路**：

贡献法换视角：点亮一个点 $v$，对总价值的贡献是确定的——每条 $(v, u)$ 边，$u$ 是白点就 $+1$、黑点就 $-1$，所以 $v$ 的贡献 = 白邻居数 − 黑邻居数，跟别人点不点、点什么完全无关。那把贡献为正的点全点上一口气就是最大值，贡献为 0 的点不点（样例输出也是不点的版本）。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int n,m,t;
string s;
vector<int> adj[maxn];

//剩 1 Min
//需要补题

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
	
	cin>>t;
    while(t--){
	    cin>>n>>m;
	    cin>>s;
	    for(int i=0;i<n;++i) adj[i].clear();
	    for(int i=0;i<m;++i){
	    	int u,v;
	    	cin>>u>>v;
	    	--u,--v;
	    	adj[u].push_back(v);
	    	adj[v].push_back(u);
		}
		
		vector<int> ans;
		for(int i=0;i<n;++i){
			int white = 0, black = 0;
			for(int j : adj[i]){
				if(s[j] == '0') ++white;
				else ++black;
			}
			// gain[i] = 白邻居 - 黑邻居 大于 0 就点亮
			if(white - black > 0) ans.push_back(i+1);
		}
		
		cout<<ans.size()<<'\n';
		for(int i=0;i<(int)ans.size();++i){
			if(i) cout<<' ';
			cout<<ans[i];
		}
		cout<<'\n';
	}

    return 0;
}
```
/*
剩 1 分钟写完，实际已经过了 VP 计时。赛后拿官方 Editorial 核对：贡献法，点一个点的贡献 = 白邻居 − 黑邻居，正的全选——和这份代码完全一致，样例也对。没在计时内确认，自标需补。
*/

## E. Rock-Paper-Scissors String Game
https://ac.nowcoder.com/acm/contest/141859/E

> 给出只含 `R/P/S` 的字符串 $s$。Alice 先手轮流操作：选一个长度 $\ge 2$ 的子串 $s[l..r]$ 满足 $s_l$ 在剪刀石头布意义上**赢** $s_r$（R 胜 S、P 胜 R、S 胜 P），删掉这个子串。不能操作的人输。问最优策略下谁赢。

**输入**

第一行整数 $t$（$1 \le t \le 10^4$）。
每组第一行 $n$（$1 \le n \le 10^6$），第二行字符串 $s$。单个文件 $n$ 总和不超过 $10^6$。

**输出**

每组一行，输出 `Alice` 或 `Bob`。

**官方结论（赛后看的题解）**

题面看了没动手。官方结论意外地干净：**只要 Alice 能做第一次操作，她就能一步把串删到 Bob 无法操作，直接赢**。所以答案 = 判断串里是否存在 $l < r$ 使 $s_l$ 胜 $s_r$。分类讨论支撑这个结论：只有一种字符 Bob 赢；两种字符按 `RS`/`SR` 型分奇偶各有取法；三种字符时按最后出现的字符钦定讨论，Alice 总能清空或只留一种字符。连续相同字符先缩成一个。

## F. Permutation of RBS
https://ac.nowcoder.com/acm/contest/141859/F

> 给出长度 $2n$ 的合法括号序列 $s$（$n$ 对括号）。给每对括号赋值，满足：所有括号对的权值构成 $1 \sim n$ 的排列；括号对 $A$ 在 $B$ 内层时 $A$ 的权值必须**大于** $B$。计数赋值方案数，模 $10^9+7$。

**输入**

第一行整数 $t$（$1 \le t \le 10^4$）。
每组第一行 $n$（$1 \le n \le 5 \times 10^5$），第二行合法括号序列 $s$。单个文件 $n$ 总和不超过 $5 \times 10^5$。

**输出**

对于每组数据，输出方案数模 $10^9+7$。

**思路**：

合法括号序列对应一棵有根树：每个括号对是一个节点，直接套在它里面的括号对是它的孩子；「内层权值更大」就是「孩子权值大于父亲」。于是问题变成：把 $1 \sim n$ 填到树上、父亲比孩子大，计数——这是树的拓扑序计数，公式 $n! / \prod_i sz_i$，$sz_i$ 是每棵子树大小。

实现用一个栈：遇到 `(` 压 1，遇到 `)` 弹出累计值 $v$——$v$ 恰好就是这个括号对（连同它内部所有已完成的部分）的**子树大小**，记进答案；如果栈里还有外层，就把 $v$ 累加到新的栈顶上。最后 $ans = n! \cdot \prod_i sz_i^{-1}$，逆元用费马小定理。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 5e5+1,mod = 1e9 + 7;
string s;
int n,t;
ll fact[maxn];
//vector<int> sz;
//stack<int> st;   
ll modpow(ll a, ll k) {
    ll res = 1;
    while(k){
        if(k & 1) res = res * a % mod;
        a = a * a % mod;
        k >>= 1;
    }
    return res;
}

//剩余 10min
//需要补题

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
	fact[0] = 1;
	for(int i=1;i<maxn;++i) fact[i] = fact[i - 1] * i % mod;
	
	cin>>t;
    while(t--){
	    cin>>n>>s;
	    vector<int> sz;
		stack<int> st;   
	    for(char c : s) {
	        if(c == '(') st.push(1);
	        else{
	            int v = st.top();
				st.pop();
	            sz.push_back(v);
	            if(!st.empty()) st.top() += v;
	        }
	    }
	    
	    ll ans = fact[n];
	    for(int z : sz) ans = ans * modpow(z,mod-2) % mod;
	    cout<<ans<<'\n';
			
	}
    
    
    return 0;
}
```
/*
剩 10 分钟写完，计时边缘没确认。赛后拿官方题解核对：方法一就是 n!/∏sz（树拓扑序计数），栈弹出的累计值就是子树大小——和这份代码一致。五个样例手推：()()→2、(())→1、()(()())→8、()→1、最后一个→28350，全对。自标需补纯粹是因为没赶上计时。
*/
