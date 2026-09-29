---
title: "Codeforces Round 1123 (Div. 2)"
tags: [codeforces, div-2, 题解]
date: 2026-09-25T22:35:00+08:00
draft: false
comments: true
upsolve:
  - problem: "D"
    name: "Backrooms Hill"
    url: "https://codeforces.com/contest/2267/problem/D"
    status: "wrong"
    note: "压哨提交 WA on pretest 1：方向全对，贪心在集合内不该断链"
  - problem: "E"
    name: "Clean Substrings"
    url: "https://codeforces.com/contest/2267/problem/E"
    status: "skip"
    note: "题面都没开"
  - problem: "F1"
    name: "XOR Transformations (Easy)"
    url: "https://codeforces.com/contest/2267/problem/F1"
    status: "skip"
    note: "题面都没开"
  - problem: "F2"
    name: "XOR Transformations (Hard)"
    url: "https://codeforces.com/contest/2267/problem/F2"
    status: "skip"
    note: "题面都没开"
  - problem: "G"
    name: "New LRT"
    url: "https://codeforces.com/contest/2267/problem/G"
    status: "skip"
    note: "题面都没开"
---

![CF1123Div2](CF1123Div2.png)
![CF1123Div2_submit](CF1123Div2_submit.png)

比赛时间：2026-09-25 22:35 ~ 00:50（UTC+8，共 2h15min）｜排名 5631｜rating 1303 → 1279（−24）

熬大夜连打系列。C 花了四十多分钟，D 方向全对但是贪心写挂，剩一分钟压哨交了一发 WA on pretest 1，小掉 24 分。E 之后连题面都没开。

## A. Turn Into a Palindrome
https://codeforces.com/contest/2267/problem/A

> Ali 有一个长度为 $n$ 的小写字符串 $s$，还有一个固定的小写字母 $c$。花一枚硬币可以把任意一个位置的字符替换成 $c$。求把 $s$ 变成回文串所需的最少硬币数。

**输入**

第一行包含整数 $t$（$1 \le t \le 500$）— 测试用例数。
每个测试用例第一行包含整数 $n$ 和字母 $c$（$1 \le n \le 100$）。
第二行是长度为 $n$ 的字符串 $s$。

**输出**

对于每个测试用例，输出最少硬币数。

**数学推导**：

对每一对 $(i,\ n-i-1)$ 单独考虑：相等直接跳过；不相等时，若其中一个本来就等于 $c$，把另一个也改成 $c$ 花 $1$ 枚；否则两个都得改成同一个字符，花 $2$ 枚（都改成 $c$ 就行）。长度为奇数时中间那个字符不用管。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;
char c;
string s;
int ans;

//总时间 2h 15 min 剩余时间 1h 58 min

void solve(){
	for(int i=0;i<=((n&1)?n/2:n/2-1);i++){
		if(i == n-i-1) break;
		if(s[i] == s[n-i-1]) continue;
		if(s[i] == c || s[n-i-1] == c) ans += 1;
		else ans += 2;
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		cin>>c;
		cin>>s;
		ans = 0;
		solve();
	//	if(n & 1) for(int i=0;i<=n/2;i++) ans += ((s[i] == c || s[n-i] == c) ? ((s[i] == s[n-i]) ? 0 : 1) : ((s[i] == s[n-i]) ? 0 : 2));
	//	else for(int i=0;i<n/2;i++) ans += ((s[i] == c || s[n-i] == c) ? ((s[i] == s[n-i]) ? 0 : 1) : ((s[i] == s[n-i]) ? 0 : 2));
		cout<<ans<<'\n';
	}
	return 0;	
}
```
/*
22:51 AC，开局 16 分钟。
*/

## B. Fashionable Array
https://codeforces.com/contest/2267/problem/B

> 定义数组的**众数**为出现次数最多的数；若并列，取其中最大的那个（$[1,1,2]$ 的众数是 $1$，$[3,4]$ 的众数是 $4$）。给定数组 $a$，可以任意重排，使**所有前缀的众数之和**最大。输出一种最优的排列。

**输入**

第一行包含整数 $t$（$1 \le t \le 500$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$1 \le n \le 100$）。
第二行包含 $n$ 个整数 $a_i$（$1 \le a_i \le 100$）。

**输出**

对于每个测试用例，输出重排后的数组（任意一组最优解）。

**数学推导**：

把最大值放到第一位，之后每个前缀的众数都不会超过它。构造按「轮」来：每一轮把当前还剩的**所有不同值从大到小各放一个**。第一轮里每个值都只出现一次，前缀众数一直是已出现的最大值；后面每一轮大值先巩固出现次数，众数在并列时也取最大。$[1,1,2,3,4,4]$ 这样排成 $4\ 3\ 2\ 1\ 4\ 1$，每个前缀的众数全是 $4$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;
int a[maxn],b[maxn];
long long ans;

//总时间 2h 15 min 剩余时间 1h 32 min
//看错题目糖逼

void solve(){
//	map<int,int> check;
	int tot[101];
	memset(tot,0,sizeof(tot));
	for(int i=n;i>=1;i--){
//		check[a[i]]++;
//		auto it = check.lower_bound({101,101});
//		ans += it->second;
		tot[a[i]]++;
		int maxx = 0,tmp = 0;
		for(int i=1;i<=100;i++) if(maxx <= tot[i]) maxx = tot[i],tmp = i;
		ans += tmp;
	}
	return;
}

void solve2(){
	int cnt = 0,last = 0;
	int vis[101];
	memset(vis,0,sizeof(vis));
	for(int i=1;i<=n;i++){
		bool ok = 0;
		last = 0;
		for(int j=n;j>=1;j--){
//			if(vis[a[j]] <= i) ok = 1,b[++cnt] = a[j],vis[a[j]]++;
			if(vis[j] || last == a[j]) continue;
			ok = 1;
			vis[j] = 1;
			last = a[j];
			b[++cnt] = a[j];
//			cout<<a[j]<<' ';
		}
		if(!ok) break;
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
		sort(a+1,a+1+n);
//		ans = 0;
//		solve();
//		cout<<ans<<'\n';
		solve2();
//		for(int i=n;i>=1;i--) cout<<a[i]<<' ';
		for(int i=1;i<=n;i++) cout<<b[i]<<' ';
		cout<<'\n';
	}
	return 0;	
}
```
/*
23:02 交了一发 WA——把题看成了「输出最大的和」，solve() 就是那个错误理解下的产物。重读题发现要输出排列本身，23:17 重写成 solve2 过了。
*/

## C. GCD Treasury
https://codeforces.com/contest/2267/problem/C

> 有 $n$ 堆金币，第 $i$ 堆有 $a_i$ 枚；海盗 Dimash 手里还有一个数 $x$。不断重复：选一个满足 $a_i > 0$ 且 $\gcd(a_i, x) \ne 1$ 的堆，设 $g = \gcd(a_i, x)$，从这堆里**恰好偷走 $g$ 枚**，然后令 $x \leftarrow g$；不存在合法的堆时被迫停下。求最多能偷多少枚。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$ 和 $x$（$1 \le n, x \le 3 \times 10^5$）。
第二行包含 $n$ 个整数 $a_i$（$1 \le a_i \le 3 \times 10^5$），所有测试用例的 $n$ 之和不超过 $3 \times 10^5$。

**输出**

对于每个测试用例，输出最多能偷走的金币总数。

**数学推导**：

1. 每次偷走的都是当前 $x$（记作 $u$）的倍数，所以第 $i$ 堆的当前值与初始值模 $u$ 同余，于是新 $x = \gcd(\text{当前}a_i,\ u) = \gcd(\gcd(\text{初始}a_i,\ x),\ u)$。令 $g_i = \gcd(a_i, x)$ 预处理，之后的演化只和这些 $g_i$ 有关。
2. 可达的 $u$ 集合：从初始 $x$ 开始 BFS，每一步拿某个 $g_i$ 出来做 $\gcd$，得到的新值 $> 1$ 就入队。
3. 若停在 $u > 1$：所有 $u$ 的倍数堆都能被反复偷到空（偷 $u$ 之后堆还是 $u$ 的倍数、$x$ 也还是 $u$）。
4. 「$d$ 的倍数堆的金币总和」怎么算：$u$ 一定是某个 $g$ 的因子，把每个 $\text{sum}[g]$ 加到 $g$ 的所有因子上，就得到 $w[d]$。
5. 答案 $= \max\{w[u] : u \text{ 可达},\ u > 1\}$。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 3e5+1;
int n,x,t;
int a[maxn];
map<int, ll> sum; //所有gcd=g币总和
map<int, ll> w;   //所有d|a[i]币总和？
vector<int> gs;   //所有不同的g？
set<int> reach;   //可达的？当前x值
queue<int> q;

//总时间 2h 15 min 剩余时间 40 min 好难

//首先想 对于现在的x或者说g 我们把所有金币中的关于g的倍数拿走是不影响g而且还最优的
//你们关键在于怎么寻找下一个x或者说g
//喵的 好瞌睡
//我们想到gcd的性质 这题一直在多次gcd 那么他其实是若干个数共同的gcd
//猜想 可以通过预处理来提前对这些数字进行分类？
//如果当前手里的数叫 u 对第 i 堆操作后新的 x 是 gcd(当前的 a[i], u)
//但是当前的 a[i] 和初始的 a[i] 模 u 是同余的 因为之前偷走的都是 u 的倍数
//所以 gcd(当前a[i], u) = gcd(初始a[i], u)
//又因为 u 一定是初始 x 的因子 所以 gcd(初始a[i], u) = gcd(gcd(初始a[i], 初始x), u)
//令 g[i] = gcd(a[i], x) 那么新的 x 就是 gcd(u, g[i])
//这样就不用管当前 a[i] 变成多少了 只看预处理的 g 就行？
//嘶 但是这有什么用？
//如果最终停在 d 那么所有 d 的倍数堆都能被偷完 因为 gcd(a[i], d)=d 偷 d 后 a[i] 还是 d 的倍数 x 还是 d
//这和我们一开始想的一样 能反复偷直到清空
//怎么去想哪些 d是相互可达的？ 他们之间影响什么？
//为什么有可达性？
//好困

//注意到！！从初始 x 出发 每次可以跳到 gcd(当前u, g[i]) 因为 g[i] 是固定的 所以能到达的 u 都是 x 的因子 
//到底怎么知道哪些 u 是可达的？？？
//我们可以从 x 开始 每次拿一个 g 去 gcd 一下 看看能变出什么新数
//变出来的数如果 >1 就说明还能继续偷 就继续拿去 gcd
//这个过程一直重复 直到没有新数出现为止
//BFS？
//如果停在 u 那 u 的倍数堆都能偷完
//那怎么算 u 的倍数堆一共有多少金币
//暴力的想直接对每个 u 扫一遍 a[i] 看能不能整除 但这样太慢了
//然后发现 u 一定是某个 g 的因子 而 g 是 gcd(a[i],x)
//d|a[i] 且 d|x 等价于 d|gcd(a[i],x)=g
//所以只要枚举 g 的因子 d 把 sum[g] 加到 w[d] 上！！！！！！！！！
//这样 w[d] 就是所有 d 的倍数堆的金币总和了
//那答案不就是所有可达的 u>1 里面 w[u] 最大的那个吗
//妈呀 好难好难 TWTWTWT

int gcd(int a,int b){return a%b==0? b:gcd(b,a%b);}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n>>x;
		for(int i=1;i<=n;i++) cin>>a[i];
		sum.clear();
		w.clear();
		gs.clear();
		reach.clear();
		while(!q.empty()) q.pop();
		
		for(int i=1;i<=n;i++) sum[gcd(a[i], x)] += a[i];
		for(auto p : sum) gs.push_back(p.first);
		for(auto p : sum){
			int g = p.first;
			ll s = p.second;
			for(int d=1; d*d<=g; d++){
				if(g % d == 0){
					w[d] += s;
					if(d * d != g) w[g/d] += s;
				}
			}
		}
		
		reach.insert(x);
		q.push(x);
		while(!q.empty()){
			int u = q.front();
			q.pop();
			for(int g : gs){
				int v = gcd(u, g);
				if(v > 1 && !reach.count(v)){
					reach.insert(v);
					q.push(v);
				}
			}
		}
		
		ll ans = 0;
		for(int u : reach) if(u > 1) ans = max(ans, w[u]);
		cout<<ans<<'\n';
	}
	return 0;	
}
```
/*
00:10 AC，剩 39 分钟。全场最花脑筋的一题，推导全在代码注释里：关键一步是「偷走的都是当前 x 的倍数 ⇒ 当前 a[i] 与初始 a[i] 模 u 同余 ⇒ 转移只依赖预处理出的 g[i]」，然后可达性 BFS + 枚举因子求和。
*/

## D. Backrooms Hill
https://codeforces.com/contest/2267/problem/D

> 若存在 $k$（$1 \le k \le m$）使数组 $b$ 的前 $k$ 个元素严格递增、后 $m-k+1$ 个元素严格递减，则称 $b$ 为**山丘（hill）**数组。给定 $1 \sim n$ 的一个排列 $a$，每次操作可以交换 $a_i$ 与 $a_{i+2}$（$1 \le i \le n-2$），次数不限。判断能否把 $a$ 变成山丘数组。

**输入**

第一行包含整数 $t$（$1 \le t \le 10^4$）— 测试用例数。
每个测试用例第一行包含整数 $n$（$1 \le n \le 2 \times 10^5$）。
第二行包含 $n$ 个不同的整数 $a_i$（$1 \le a_i \le n$），所有测试用例的 $n$ 之和不超过 $2 \times 10^5$。

**输出**

对于每个测试用例，输出 `YES` 或 `NO`。

**数学推导**：

- 交换距离是 2，所以**奇数位的元素只能在奇数位之间重排，偶数位同理**（相邻交换 = 冒泡排序的结论，打的第一场 CF 的 T3 里就写过）。
- 把奇数位、偶数位的值分别排序得到 $o$、$e$。峰值必须是全局最大值，所以 $k$ 的奇偶被最大值所在的集合决定。
- 左侧要严格递增：从两个集合最小的值开始交错取（位置 $1$ 固定是奇数位），预处理出最长能取多长；右侧去掉峰值后从最大开始交错取，起始集合有两种，对应 $k$ 的两种奇偶。
- 枚举合法奇偶的 $k$，$O(1)$ 判断 $L = k-1$、$R = n-k$ 是否都不超过预处理出的上限。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;
int a[maxn];
vector<int> o,e;
vector<int> o2,e2;  //去掉峰值的奇偶
int mx;
bool mxinodd;       //峰值是否来自奇

//总时间 2h 15 min 剩余时间 1 min 压哨

//这个D看起来就比C要好写 我们能不能去枚举每一个 k 然后分别对两个子数组
//(因为相邻交换可以视为冒泡排序 这个结论我在打的第一场CF T3就写出来了)进行两个方向的排序 然后合并到一起来判断可不可以？
//但是这个时间复杂度似乎是超的 O(n^2logn)？
//能不能用堆排序去优化这个过程？这样每次插入一个新元素就是logn的 但是问题在于没法快速获取排好序的元素 和 删除一个元素
//除非手写四个堆么?
//还是说通过一次数据结构的预处理（树状数组 线段树存当前的排名？）来优化这个排序的过程？
//好难 呜呜呜呜呜 我想睡觉 已经0:21了 还在医院旁边
//哦还有 当前美剧的k鸡还是偶也会影响答案的判断 这里需要分类讨论一下
//莫非真的要手写四个堆吗 我真想不出来其他解法了
//先把数组拆分 然后在美剧k 然后再分四段排序 然后再合并 是否可行？
//等一下 好像不需要拆成四段 他们不能随便排吗 那不两段直接分开拍一次 然后再美剧k的时候直接正着读取前k哥 然后倒着读取后k个
//等一下 为什么一定要整段整段的操作呢 我们为什么不用两个指针来枚举奇偶两个段的情况？哦 好像是需要满足k的原因
//不对啊 双指针不也可以满足这个吗？
//妈的 好困
//！！其实只要拆成奇偶两段分别排序就够了
//因为交换i和i+2只能同奇偶互换 所以奇数位元素只能在奇数位重排 偶数位同理
//那峰值k的奇偶必须和全局最大值所在集合一致 不然峰值就放不到k上
//左侧要严格递增 那就从最小的开始交错取(奇位取o 偶位取e 或者反)
//右侧要严格递减 那就从最大的开始交错取 但注意去掉峰值
//两种起始奇偶对应k的奇偶 预处理出最长长度 然后枚举k O(1)判断

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n;
		o.clear(); e.clear();
		for(int i=1;i<=n;i++){
			cin>>a[i];
			if(i&1) o.push_back(a[i]);
			else e.push_back(a[i]);
		}
		sort(o.begin(),o.end());
		sort(e.begin(),e.end());
		mx = max(o.back(), e.back());
		mxinodd = (o.back() == mx);
		
		//左侧:从小往大交错取 最长严格递增长度
		int maxleft = 0;
		{
			int i=0, j=0;
			int pre = INT_MIN;
			int pos = 1;
			while(1){
				int cur;
				if(pos&1){
					if(i>=(int)o.size()) break;
					cur = o[i++];
				}else{
					if(j>=(int)e.size()) break;
					cur = e[j++];
				}
				if(cur <= pre) break;
				pre = cur;
				maxleft++;
				pos++;
			}
		}
		
		o2.clear(); e2.clear();
		if(mxinodd){
			o2.assign(o.begin(), o.end()-1);
			e2 = e;
		}else{
			o2 = o;
			e2.assign(e.begin(), e.end()-1);
		}
		
		//右侧第一个是奇 k为偶
		int maxrighta = 0;
		int i=(int)o2.size()-1, j=(int)e2.size()-1;
		int pre = INT_MAX;
		bool turnodd = true;
		while(1){
			int cur;
			if(turnodd){
				if(i<0) break;
				cur = o2[i--];
			}else{
				if(j<0) break;
				cur = e2[j--];
			}
			if(cur >= pre) break;
			pre = cur;
			maxrighta++;
			turnodd = !turnodd;
		}
		
		//右侧第一个是偶 k为奇
		int maxrightb = 0;
		int i2=(int)o2.size()-1, j2=(int)e2.size()-1;
		int pre2 = INT_MAX;
		bool turnodd2 = false;
		while(1){
			int cur;
			if(turnodd2){
				if(i2<0) break;
				cur = o2[i2--];
			}else{
				if(j2<0) break;
				cur = e2[j2--];
			}
			if(cur >= pre2) break;
			pre2 = cur2;
			maxrightb++;
			turnodd2 = !turnodd2;
		}	
		
		bool ok = false;
		int startk = mxinodd ? 1 : 2;// k的奇偶和峰值一致
		for(int k=startk;k<=n;k+=2){//注意这里是k+2 峰值 k的奇偶必须和最大值一致 所以 k 只能取一种奇偶!!!!!!!!!!!
			int L = k-1,R = n-k;
			if(L > maxleft) continue;
			if(k&1){
				if(R <= maxrightb) ok = true;
			}else{
				if(R <= maxrighta) ok = true;
			}
			if(ok) break;
		}
		cout<<(ok?"YES":"NO")<<'\n';
	}
	return 0;	
}
```
/*
00:49 剩 15 秒压哨交了一发，WA on pretest 1。赛后复盘：方向全对，挂在贪心的「断链」上——交错取数时，当前集合的下一个放不进去不该直接 break，而要在集合内**跳过**它继续找（右侧取完 5、3 之后，奇数位集合里的 4 接不上，但 2 可以）。把 break 改成集合内指针前移就能过，样例 3（`5 3 4 6 2 1`，答案 YES）正好卡掉这个写法。
*/

## E. Clean Substrings
https://codeforces.com/contest/2267/problem/E

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,t;

//总时间 2h 15 min 剩余时间 2h 15 min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>t;
	while(t--){
		cin>>n;
		
	}
	return 0;	
}
```

## F1. XOR Transformations (Easy Version)
https://codeforces.com/contest/2267/problem/F1

题面没开，空模板原样躺着。

## F2. XOR Transformations (Hard Version)
https://codeforces.com/contest/2267/problem/F2

题面没开，空模板原样躺着。

## G. New LRT
https://codeforces.com/contest/2267/problem/G

题面没开，空模板原样躺着。
