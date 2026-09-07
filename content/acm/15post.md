---
title: "Codeforces Round 1119 (Div. 3)"
date: 2026-09-05
draft: false
comments: true
---

![CF1119_div3](/img/acm/CF1119_div3.png)
![CF1119_div3_submit](/img/acm/CF1119_div3_submit.png)

先是VP了24年的河南大学新生赛，在几道特别简单的模拟上面卡了半天，调试一坨，3h只做出 6 / 11，一坨粪。
军训熬夜打的，后面直接开始犹如蟒蛇缠绕般的窒息感，调了半天发现思路想复杂了。
还发现很多问题：比如调试能力差，模拟边界条件处理不清，题目读题总是出问题等等，要加强对水题的秒杀能力

## A. 数组游戏
https://codeforces.com/contest/2259/problem/A

> 给定长度为 $n$ 的 01 字符串 $s$ 和整数 $k$，将字符串分成若干段，每段长度恰好为 $k$。定义一段是"好段"当且仅当该段内所有字符都为 $1$。求最多能分出多少个好段。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。

每个测试用例第一行包含两个整数 $n$ 和 $k$（$1 \le k \le n \le 2 \cdot 10^5$）。

第二行包含一个长度为 $n$ 的 01 字符串 $s$。

所有测试用例的 $n$ 之和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出一个整数表示最多能分出的好段数量。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxx = 22;
int t,n,k;
int sum[maxx];
string s;
//比赛总用时14min
int solve(){
	int cnt = n/k;
	for(int i=0;i<n;i++) sum[i+1] = sum[i] + (s[i] - '0');
	if(sum[k] != k) cnt--;
//	for(int i=2;i<=n/k;i++) if(sum[i*k] - sum[(i-1)*k-1] != k) cnt--;
	for(int i=2;i<=n/k;i++) if(sum[i*k] - sum[(i-1)*k] != k) cnt--;
	return cnt;
}
int main(){
	cin>>t;
	while(t){
		t--;
		cin>>n>>k;
		cin>>s;
		cout<<solve()<<endl;
	}
	return 0;	
}
```
/*
比赛时 14 分钟完成。贪心地每 k 个一组，用前缀和快速检查每组是否全为 1，统计满足条件的组数。
*/

## B. 最大频率
https://codeforces.com/contest/2259/problem/B

> 给定长度为 $n$ 的数组 $a$。每次操作可以选择一个数，若它为偶数则除以 $2$，若为奇数则减 $1$ 后除以 $2$（即 $a_i \gets \lfloor a_i / 2 \rfloor$）。求经过任意次操作后，数组中**出现次数最多**的数最多能出现多少次。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。

每个测试用例第一行包含整数 $n$（$1 \le n \le 2 \cdot 10^5$）。

第二行包含 $n$ 个整数 $a_i$（$1 \le a_i \le 10^9$）。

所有测试用例的 $n$ 之和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出一个整数表示答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
long long a[maxn];
//比赛总用时34min 叫的时候忘记把排序注释掉...
//发现一直减a[]肯定是正数 而且要么是1要么是0 同时注意到是一块减2(糖逼了一开始没看懂) 所以偶数（2 -> 0）轮流出现 即便a[]一开始是负数也不影响 最后都会回到1或0
int solve(){
	int cnt1 = 0,cnt2 = 0,cnt3 = 0;
//	sort(a+1,a+1+n);
	for(int i=1;i<=n;i++){
		if(a[i] & 1) cnt1++;
		else if((a[i]/2)&1) cnt2++;
		else cnt3++;
	}
	return max(cnt1,max(cnt2,cnt3));
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i];
		cout<<solve()<<'\n';
	}
	return 0;	
}
```
/*
比赛总用时 34 分钟，第一次提交时忘记把排序删了。
通过观察发现，每个数经过不断除以 2 后，最终只会变成 0 或 1。而答案取决于奇数个数、偶数中一半为奇数的个数、其余个数，三者取最大值。注意即使初始有负数，最后也会回到 1 或 0。
*/

## C. 最大化距离
https://codeforces.com/contest/2259/problem/C

> 给定长度为 $n$ 的数组 $a$，其中只包含 $-1, 0, 1$。你可以将任意一个 $0$ 改为 $1$ 或 $-1$（也可以不改）。求操作后，数组中两个**非零**元素之间的最大距离（即下标差）。如果数组中非零元素少于 $2$ 个，输出 $0$。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。

每个测试用例第一行包含整数 $n$（$1 \le n \le 2 \cdot 10^5$）。

第二行包含 $n$ 个整数 $a_i$（$-1 \le a_i \le 1$）。

所有测试用例的 $n$ 之和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出 $n$ 个整数，第 $i$ 个表示若只考虑前 $i$ 个位置时的答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
int a[maxn];
//52 WA 一次 59minAC
//题意最大化两个1之间的距离 没有就输出0
//考虑答案有谁贡献：1 和 -1 那么我们只关注这俩数的下标就行了
//注意读题！！ 单个1也计入 注意不要忘记处理只有一个1或-1的情况
void solve(){
	int cnt = 0;
	for(int i=1;i<=n;i++) if(a[i] == 1 || a[i] == -1) cnt++;
	if(cnt == 0){
		for(int i=1;i<=n;i++) cout<<0<<' ';
		cout<<'\n';
		return;
	}
	if(cnt == 1){
		for(int i=1;i<=n;i++){
			if(a[i] == 0)cout<<0<<' ';
			if(a[i] == -1 || a[i] == 1) cout<<1<<' ';
		}
		cout<<'\n';
		return;
	}
	int l=1,r=n;
	while(l < n && a[l] == 0) l++;
	while(r > 1 && a[r] == 0) r--;
	a[l] = 1,a[r] = 1;
//	if(l < n && r > 1) a[l] = 1,a[r] = 1;
//	else{
//		for(int i=1;i<=n;i++) cout<<0<<' ';
//		cout<<'\n';
//		return;
//	}
	for(int i=1;i<=n;i++){
		if(a[i] == -1 || a[i] == 0) cout<<0<<' ';
		else cout<<1<<' ';
	}
	cout<<'\n';
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i];
		solve();
	}
	return 0;	
}
```
/*
第一次提交 WA，第二次 59 分钟 AC。题意是最大化两个非零元素之间的距离，因此只需要关注最左和最右的非零元素。将最左和最右的 0 改为 1，然后输出每个位置是否为非零（1 表示非零，0 表示零）。注意处理只有一个非零元素的情况。
*/

## D. MEX 分配
https://codeforces.com/contest/2259/problem/D

> 给定长度为 $n$ 的数组 $a$。有三个初始为空的集合 $A, B, C$。对于每个 $i$（$1 \le i \le n$），将 $a_i$ 放入 $A, B, C$ 中的恰好一个。判断是否存在一种分配方案，使得：
> $$MEX(A) + MEX(B) + MEX(C) \ge 2 \cdot \max(MEX(A), MEX(B), MEX(C))$$
> 如果存在，输出一种构造方案。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。

每个测试用例第一行包含整数 $n$（$3 \le n \le 2 \cdot 10^5$）。

第二行包含 $n$ 个整数 $a_i$（$0 \le a_i \le 10^9$）。

所有测试用例的 $n$ 之和不超过 $2 \cdot 10^5$。

**输出**

如果存在合法分配，输出 `YES` 和一个长度为 $n$ 的字符串 $s$（$s_i \in \{A, B, C\}$），表示第 $i$ 个元素放入哪个集合。否则输出 `NO`。

---

**解题思路（赛时）**：

当时想错了，以为要尽可能一样。先排序后三分轮流分配，其实根本不需要，答案远比想象中简单。

**代码一**：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
struct node{
	int vlu,id;
}a[maxn];
char tmp[maxn];
bool ans = 0;
bool cmp(const node &x,const node &y){return x.vlu < y.vlu;}
//比赛开始了 min
//思考： 题目条件可以写成 mex(最小的) + mex(中等的) >= mex(最大的)
//同时mex的性质有 长度为n的序列 mex必定落在 [0,n]之间 注意到a[]长度大于等于3
//所以要尽可能让最大值变小 最小值变大
//思考 变得平均是否可行 即尽可能让三个序列都一样
//思考 什么时候没有解
inline int mex(unordered_map<int,int> &now){
	int cnt=0;
	while(cnt<=now.size() && now.find(cnt) != now.end()) cnt++;
	return cnt;
}
void solve(){
	unordered_map<int,int> A;
	unordered_map<int,int> B;
	unordered_map<int,int> C;
	sort(a+1,a+1+n,cmp);
	for(int i=1;i<=n;i++){
		if(i%3==1) A.insert({a[i].vlu,1}),tmp[a[i].id] = 'A';
		else if(i%3==2) B.insert({a[i].vlu,1}),tmp[a[i].id] = 'B';
		else if(i%3==0) C.insert({a[i].vlu,1}),tmp[a[i].id] = 'C';
	}
	int mex1 = mex(A),mex2 = mex(B),mex3 = mex(C);
	if(mex1+mex2+mex3<2*max(mex1,max(mex2,mex3))) ans = 0;
	else ans = 1;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		ans = 0;
		t--;
		cin>>n;
		for(int i=1;i<=n;i++) cin>>a[i].vlu,a[i].id = i;
		solve();
		if(ans){
			cout<<"YES"<<'\n';
			for(int i=1;i<=n;i++) cout<<tmp[i];
			cout<<'\n';
		}
		else cout<<"NO"<<'\n';
	}
	return 0;	
}
```

**代码二**：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+5;
int t,n;
struct node{
	int vlu,id;
}a[maxn];
char tmp[maxn];

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		int cnt0 = 0;
		for(int i=1;i<=n;i++){
			cin>>a[i].vlu;
			a[i].id = i;
			if(a[i].vlu == 0) cnt0++;
		}
		if(cnt0 == 1){
			cout<<"NO\n";
			continue;
		}
		cout<<"YES\n";
		int placed = 0; // 已经分配了0给A或B的数量
		for(int i=1;i<=n;i++){
			if(a[i].vlu == 0){
				if(placed == 0){
					tmp[i] = 'A';
					placed = 1;
				}
				else if(placed == 1){
					tmp[i] = 'B';
					placed = 2;
				}
				else{
					tmp[i] = 'A'; // 多余的0都扔给A，不影响MEX
				}
			}
			else{
				tmp[i] = 'C'; // 所有非零元素放入C，C没有0，所以MEX=0
			}
		}
		for(int i=1;i<=n;i++) cout<<tmp[i];
		cout<<"\n";
	}
	return 0;
}
```
/*
如果 0 的个数为 1，则只有一个集合的 MEX 大于 0，不等式无法满足。否则，将两个 0 分别放入 A 和 B，其余 0 放入 A，所有非零元素放入 C。这样 MEX(A)=2，MEX(B)=1，MEX(C)=0，满足 2+1+0 ≥ 2·2。
*/

## E. 宝藏猎人
https://codeforces.com/contest/2259/problem/E
D和E一块写的，压哨极限写完，这场比赛太猪了......

> 有 $n$ 个岛屿排成一行，编号 $1$ 到 $n$。有些岛屿上藏有宝藏。给定数组 $b_1, b_2, \dots, b_n$：
> - 如果 $b_i = -1$，表示第 $i$ 个岛屿上没有限制；
> - 如果 $b_i > 0$，表示从第 $i$ 个岛屿出发，距离它最近的宝藏岛屿与它的距离**恰好**为 $b_i$（即存在一个宝藏岛屿在 $i-b_i$ 或 $i+b_i$ 位置，且不存在宝藏岛屿在 $(i-b_i, i+b_i)$ 范围内）。
>
> 请构造一种宝藏放置方案，或判断无解。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。

每个测试用例第一行包含整数 $n$（$1 \le n \le 2 \cdot 10^5$）。

第二行包含 $n$ 个整数 $b_i$（$-1 \le b_i \le n$）。

所有测试用例的 $n$ 之和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，如果存在合法方案，输出一个长度为 $n$ 的 01 字符串，`1` 表示该位置有宝藏；否则输出 `-1`。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+5;
int t, n;
int b[maxn], st[maxn], df[maxn], cv[maxn];
char tmp[maxn];

bool solve() {
	for(int i=1;i<=n;i++) st[i]=df[i]=cv[i]=0;
	for(int i=1;i<=n;i++) if(b[i]==0) st[i]=1;
	for(int i=1;i<=n;i++) if(b[i]>0) {
		int k=b[i], L=i-k+1, R=i+k-1;
		if(L<1) L=1;
		if(R>n) R=n;
		if(L<=R) { df[L]++; df[R+1]--; }
	}
	int cur=0;
	for(int i=1;i<=n;i++) {
		cur += df[i];
		cv[i] = cur;
		if(st[i] && cv[i]) return false;
	}
	for(int i=1;i<=n;i++){
		if(b[i]>0) {
			int k=b[i], l=i-k, r=i+k;
			bool ok=false;
			if(l>=1 && cv[l]==0) { st[l]=1; ok=true; }
			else if(r<=n && cv[r]==0) { st[r]=1; ok=true; }
			if(!ok) return false;
		}
	}
	bool has=false;
	for(int i=1;i<=n;i++) if(st[i]) { has=true; break; }
	if(!has) {
		for(int i=1;i<=n;i++) if(cv[i]==0) { st[i]=1; has=true; break; }
		if(!has) return false;
	}
	const int INF=1e9;
	int ld[maxn], rd[maxn], last=-INF;
	for(int i=1;i<=n;i++) {
		if(st[i]) last=i;
		ld[i] = (last==-INF ? INF : i-last);
	}
	last=INF;
	for(int i=n;i>=1;i--) {
		if(st[i]) last=i;
		rd[i] = (last==INF ? INF : last-i);
	}
	for(int i=1;i<=n;i++) {
		int d = min(ld[i], rd[i]);
		if(b[i]!=-1 && d!=b[i]) return false;
	}
	for(int i=1;i<=n;i++) tmp[i] = st[i] ? '1' : '0';
	tmp[n+1] = '\0';
	return true;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> t;
	while(t--) {
		cin >> n;
		for(int i=1;i<=n;i++) cin >> b[i];
		if(solve()) cout << (tmp+1) << "\n";
		else cout << "-1\n";
	}
	return 0;
}
```
/*
先处理 b_i=0 的情况（该位置必须是宝藏）。对于 b_i>0，用差分数组标记 [i-b_i+1, i+b_i-1] 范围内不能有宝藏。
然后对于每个 b_i>0，尝试在 i-b_i 或 i+b_i 位置放置宝藏。最后检查每个位置到最近宝藏的距离是否与 b_i 匹配。
*/

## F
https://codeforces.com/contest/2259/problem/F

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxx = 100010;
int t;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n>>s;
		cout<<solve()<<'\n';
	}
	return 0;	
}
```

## G
https://codeforces.com/contest/2259/problem/G

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxx = 100010;
int t;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t){
		t--;
		cin>>n>>s;
		cout<<solve()<<'\n';
	}
	return 0;	
}
```