---
title: "程序设计新生周赛（一）"
tags: [新生赛, 题解]
aliases: ["/acm/26post/"]
date: 2026-11-01
draft: false
comments: true
upsolve:
  - problem: "B"
    name: "方程换元"
    url: "https://oj.zznu.edu.cn/p/259"
    status: "wrong"
    note: "赛时 4 发 45→45→95→95；终场后 11 秒才落盘的 fabsl + long double 修复版本地过全部样例与官方边界，OJ 补交待做"
---

比赛时间：2026-11-01 14:00 ~ 17:00（[ZZNU OJ 新生周赛（一）](https://oj.zznu.edu.cn/contest/6ae0c655655f2199b8baf481)，XCPC 赛制，16:24 封榜）｜446 人参与

**成绩**：7 / 8，**rank 16**，罚时 4:50（= 7 题 AC 时刻之和 250:31 + A 两发 WA 的 40:00 罚时）。15 人 AK，7 题选手里排第一；B「方程换元」4 发未出——那也是全场通过率最低的一题（84 / 713）。

**做题情况**（提交时刻，来自赛后拉取的 13 条评测记录）

- 0:07 C 过（一发）
- 0:15 G 过（一发）
- 0:18 E 过（一发）
- 0:30 D 过（一发；「唐了 先看其他题目了 中间还绕了一下」）
- 0:45 F 过（一发）
- 0:49 / 0:54 A 两发 WA（都 80 分）→ 0:56 A 过（第三发）
- 1:16 H 过（一发）
- 2:12 / 2:40 / 2:49 / 2:58 B 四发 WA（45 → 45 → 95 → 95 分）——赛时没写对
- 17:00:11 终场后 11 秒，B 的修复版才落盘

## A - 埃拉托色尼筛法？（P1262）
https://oj.zznu.edu.cn/p/262

> **题意**：$n$ 个正整数（$n \le 10^4$，$a_i \le 10^4$），能否选出**任意多个**元素使乘积恰好为 67。能输出 YES，否则 NO。

题名带问号是因为它和筛法毫无关系。67 是质数：乘积恰为 67 ⟺ **数组里出现过 67**（选一堆 1 不改变乘积，其它数只会把乘积顶爆）。提交量 1063 发全场第一、通过 249——大概不少人真去筛了。

**第一版**（0:49 提交，80 分）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e4+1;
ll n,a;
ll res = 1;

//48min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
//	vector<int> b;
//	for(int i=1;i<=n;i++){
//		cin>>a;
//		if(a > 67) continue;
//		b.push_back(a);	
//	}
//	sort(b.begin(),b.end());
//	//突然想到 因为 67是个质数 所以 只要 前缀乘积 整除 67 即可 这波唐了
//	for(auto)
	for(int i=1;i<=n;i++) cin>>a,res *= a;
	
	if(res % 67 == 0) cout<<"YES";//6767676767
	else cout<<"NO";
	return 0;
}
```

两处错：① $n$ 个 $\le 10^4$ 的数全乘起来，`long long` 几步就溢出了；② 「`res % 67 == 0`」判的是「乘积是 67 的**倍数**」——输入 `134` 会误判 YES，可你选不出恰好 67。第二发（0:54，80 分）改了个「`a >= 67 && a % 67 == 0`」的变体，还是没跳出倍数思维。

**第三版**（0:56 过，A1.cpp）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e4+1;
ll n,a;
ll res = 1;

//唐完了 连内存都不会算了吗 56min

void check(){
	for(int i=1;i<=67;i++){
		if(67 % i == 0) cout<<i<<' ';
		
	}
}

int main(){
//	check();
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	bool ans = 0;
	for(int i=1;i<=n;i++){
		cin>>a;
//		if(a>=67 && a%67==0) ans = 1;我是猪 题目说的是 乘积是67 而不是 被惩处 白痴两发法师
		if(a == 67) ans = 1;
	}
	if(ans) cout<<"YES";
	else cout<<"NO";
	return 0;
}
```

### 解读

判断「能否凑出质数 p」只有一条路：p 出现过。注释里那句「因为 67 是个质数」在第一版里就想到了，可惜想到的是「前缀乘积整除 67」而不是「出现过」。教训：**判断类题落笔前先造两个反例**——全 1 数组、以及 67 的倍数（134）。

## B - 方程换元（P1259，未解出）
https://oj.zznu.edu.cn/p/259

> **题意**：求方程 $2^{x+2} + \dfrac{\log_2 b}{2^x} = \log_2 a$ 的最大实数解。无解输出 `No Answer`；按四舍五入保留两位小数，四舍五入为零时统一输出 `0.00`、不输出 `-0.00`。$1 \le a, b < 10^4$。

**数学部分其实是顺利的**。设 $t = 2^x > 0$，记 $A = \log_2 a$、$B = \log_2 b$，两边乘 $t$ 得

$$4t^2 - At + B = 0,\qquad \Delta = A^2 - 16B.$$

$\Delta < 0$ 无解；否则解出 $t$，再 $x = \log_2 t$。卡住的全是工程细节：



### 做法与教训

四发的部分分轨迹是 45 → 45 → 95 → 95：

1. **第一发（2:12，45 分）**：`const int maxn = 1e5+1, eps = 1e-8;` —— `eps` 是 `int`，`1e-8` 截断成 **0**。更致命的是四舍五入守卫写成了 `ans1 <= 1e-3 || ans1 >= -1e-3`——两个条件的**并集覆盖全体实数**，任何答案都会被清成 `0.00`。开题阶段的注释原话：「对于 2^x 和 log2（x）的函数是怎么写的？？」「不会是牛顿迭代法二分吧大哥？？？」——后来试出 `pow` / `exp2` 能直接用（「我去！竟然可以 看来我对C++的探索度不到1%」）。
2. **第二发（2:40，45 分）**：`eps` 修成 `long double 1e-8`，但守卫改成 `ans1 <= 0.0049… || ans1 >= -0.0049…`——**还是并集**，还是全零。分数没动，正好说明卡的是同一处。
3. **第三、四发（2:49 / 2:58，95 分）**：守卫修好（这两版没有留档），爬到 95 分——只剩一个测试点，到终场也没定位出来。
4. **终场版（17:00:11 落盘）**：`fabsl(ans1) <= 0.005L` 才是防 `-0.00` 的正确写法；换成 `exp2l / log2l / sqrtl`；`Δ` 先按 `< -eps` 判无解、再把 `|Δ| ≤ eps` 的浮点噪声夹成 0。本地验证：三个样例 + 官方题解的边界用例（`1 1 → No Answer`、`2 1 → -2.00`）全过。差的那一口气没赶上交。

**第一发（2:12 提交，45 分）——B.cpp 原文：**

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1,eps = 1e-8;
ll a,b;
long double m,n,t1,t2,det,ans1,ans2;

//换元 得到 t = 2^x m = log2b n = log2a 
//得到 4t^2 - nt + m = 0
//有实数解的前提是 n^2 - 16m >= 0 其两个解为 t1 t2
//同时存在至少一个解 t1 或 t2 满足 t1 > 0 || t2 > 0
//接下来处理比较难的就是 二分 2^x == t1 || 2^x == t2
//这个数学上 小数次幂 是啥来着？？？
//以及c++中 对于2^x 和 log2（x）的函数是怎么写的？
//不会是牛顿迭代法二分吧大哥？？？？
//这是真不会啊
//1h 36min
//我勒哥啊一个两个全都 ak了 
//2h 12min 终于能交上第一发了

long double check(long double x){//至今不知道要怎么表示小数幂
	long double l = -1e18,r = 1e18,mid = 0.0,ans = 0.0;//竟然能开这么大？
	long double erfen = -1e4;//好久没写小书二分了 现在都生疏了
//	while(l <= r + erfen){
	for(int i=1;i<=100000;i++){
		mid = l + (r - l) / 2.00;
		if(exp2(mid) >= x + eps) r = mid;
		else l = mid;
	}
	return l;
}

int main(){
//	ios::sync_with_stdio(false);
//	cin.tie(0);
//	cout<<pow(2.0,0.5)<<'\n';//我去！竟然可以 看来我对C++的探索度不到1 %
//	cout<<exp2(0.5)<<'\n';
	cin>>a>>b;
	m = log2(b);//我去竟然可以
	n = log2(a);
//	cout<<m<<'\n'<<n<<'\n';		
	det = n*n - (16.0)*m;
	if(det < eps){
		cout<<"No Answer";
		return 0;
	}
	t1 = (n + sqrt(det)) / 8.0,t2 = (n - sqrt(det)) / 8.0;//嘶 这精度有点感人啊
	if(t1 <= eps && t2 <= eps){
		cout<<"No Answer";
		return 0;
	}
	//最阴的一步来了 怎么表示2的小数次幂？
//	cout<<t1<<'\n'<<t2<<'\n';
	if(det == eps){
		if(t1 > eps) ans1 = check(t1),cout<<fixed<<setprecision(2)<<ans1<<'\n';//唐完了输出都忘了
		return 0;
	}
	bool pd1 = 0,pd2 = 0;
	if(t1 > eps) ans1 = check(t1),pd1 = 1;
	if(t2 > eps) ans2 = check(t2),pd2 = 1;
//	if(pd1 && (ans1 == eps || ans1 == -1.0 * eps)) ans1 = 0.00;
//	if(pd2 && (ans2 == eps || ans2 == -1.0 * eps)) ans2 = 0.00;
	if(pd1 && (ans1 <= 1e-3 || ans1 >= -1.0 * -1e-3)) ans1 = 0.00;
	if(pd2 && (ans2 <= 1e-3 || ans2 >= -1.0 * -1e-3)) ans2 = 0.00;
	if(pd1 && pd2){//唐了 题目说的是输出较大的解
//		if(ans1 == ans2 + eps || ans1 == ans2 - eps) cout<<fixed<<setprecision(2)<<ans1;
//		else cout<<fixed<<setprecision(2)<<ans1<<'\n'<<fixed<<setprecision(2)<<ans2;
		if(ans1 == ans2 + eps || ans1 == ans2 - eps) cout<<fixed<<setprecision(2)<<ans1;
		else if(ans1 > ans2 + eps) cout<<fixed<<setprecision(2)<<ans1;//我勒哥哥啊我求你别输出-0,00了 2h 10min 现在这个二分写的真是一点不熟练了
		else cout<<fixed<<setprecision(2)<<ans2;
	}
	else if(pd1) cout<<fixed<<setprecision(2)<<ans1;
	else if(pd2) cout<<fixed<<setprecision(2)<<ans2;
	return 0;
}
```

**第二发（2:40 提交，45 分）——B1.cpp 原文：**

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
const long double eps = 1e-8;//烫完了哥
ll a,b;
long double m,n,t1,t2,det,ans1,ans2;

//2h 39min

long double check(long double x){
	long double l = -1e18,r = 1e18,mid = 0.0;
	for(int i=1;i<=1000;i++){//	
		mid = l + (r - l) / 2.00;
//		if(fabsl(exp2(mid) - x) >= eps) r = mid;//唐
		if(exp2(mid) >= x) r = mid;
		else l = mid;
	}
	return mid;
}

/*
32 2

*/

int main(){
	cin>>a>>b;
	m = log2(b);
	n = log2(a);	
	det = n*n - (16.0)*m;
	if(det < 0){//唐
		cout<<"No Answer";
		return 0;
	}
	t1 = (n + sqrt(det)) / 8.0,t2 = (n - sqrt(det)) / 8.0;
	if(t1 <= 0 && t2 <= 0){
		cout<<"No Answer";
		return 0;
	}
	if(det == 0){
		if(t1 > 0) ans1 = check(t1),cout<<fixed<<setprecision(2)<<ans1<<'\n';
		return 0;
	}
	bool pd1 = 0,pd2 = 0;
	if(t1 > 0) ans1 = check(t1),pd1 = 1;
	if(t2 > 0) ans2 = check(t2),pd2 = 1;
	if(pd1 && (ans1 <= 0.004999999999999999 || ans1 >= -0.004999999999999999)) ans1 = 0.00;//唐
	if(pd2 && (ans2 <= 0.004999999999999999 || ans2 >= -0.004999999999999999)) ans2 = 0.00;
	if(pd1 && pd2){
		if(fabsl(ans1 - ans2) <= eps) cout<<fixed<<setprecision(2)<<ans1;//唐
		else if(ans1 > ans2) cout<<fixed<<setprecision(2)<<ans1;
		else cout<<fixed<<setprecision(2)<<ans2;
	}
	else if(pd1) cout<<fixed<<setprecision(2)<<ans1;
	else if(pd2) cout<<fixed<<setprecision(2)<<ans2;
	return 0;
}
```

**终场版（B2.cpp，17:00:11 落盘——终场后 11 秒，未及提交）**：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
const long double eps = 1e-8;
ll a,b;
long double m,n,t1,t2,det,ans1,ans2;

//2h 58min

long double check(long double x){
	long double l = -1e18,r = 1e18,mid = 0.0;
	for(int i=1;i<=1000;i++){
		mid = (l + r) / 2.00;
		if(exp2l(mid) >= x) r = mid;
		else l = mid;
	}
	return mid;
}

int main(){
	cin>>a>>b;
	m = log2l(b);//?
	n = log2l(a);	
	det = n*n - (16.0)*m;
	if(det < -eps){//
		cout<<"No Answer";
		return 0;
	}
	if(det < 0) det = 0;//
	t1 = (n + sqrtl(det)) / 8.0,t2 = (n - sqrtl(det)) / 8.0;//
	if(t1 <= eps && t2 <= eps){//
		cout<<"No Answer";
		return 0;
	}
	if(fabsl(det) <= eps){//
		if(t1 > 0) ans1 = check(t1),cout<<fixed<<setprecision(2)<<ans1<<'\n';
		return 0;
	}
	bool pd1 = 0,pd2 = 0;
	if(t1 > 0) ans1 = check(t1),pd1 = 1;
	if(t2 > 0) ans2 = check(t2),pd2 = 1;
	if(pd1 && fabsl(ans1) <= 0.005L) ans1 = 0.00;//糖上加糖
	if(pd2 && fabsl(ans2) <= 0.005L) ans2 = 0.00;//唐完了数都抄错了
	if(pd1 && pd2){
		if(fabsl(ans1 - ans2) <= eps) cout<<fixed<<setprecision(2)<<ans1;
		else if(ans1 > ans2) cout<<fixed<<setprecision(2)<<ans1;
		else cout<<fixed<<setprecision(2)<<ans2;
	}
	else if(pd1) cout<<fixed<<setprecision(2)<<ans1;
	else if(pd2) cout<<fixed<<setprecision(2)<<ans2;
	return 0;
}
```

**官方做法对比**：官方只取**较大根** $t = \frac{A + \sqrt{\Delta}}{8}$——$\log_2$ 单调，大根不行小根更不行，一整段「两根都判再取 max」的代码可以删掉。另外 `a = b = 1` 时 $A = B = 0$，解出 $t = 0$ 不合法，要输出 `No Answer`——这个边界官方单独点过名，终场版是覆盖了的。

**回头看，二分从头到尾都不需要**：解出 $t$ 之后，$x = \log_2 t$ 就是答案，而这份代码前后已经在调 `log2(a)`、`log2(b)`（终版是 `log2l`）——同一个函数随手就能算出终点。`check()` 里那 1000 轮「对 $2^x$ 二分」，是赛时不知道 `log2` 已经在手里，硬把答案函数亲手重造了一遍。

教训两条：**① 输出格式类的小修正（防 `-0.00` 这种）必须拿边界值单测**（±0.004、±1、0），`||` 和 `&&` 一字之差就是把「绝对值小于阈值」写成「恒真」；**② `exp2` / `log2` / `sqrtl` 这类库函数要赛前混个脸熟**——赛时第一次见它们，光探测函数存在性就烧掉了不少分钟，连 $x = \log_2 t$ 这最后一步都绕成了二分。

## C - 倒三角形（P1207）
https://oj.zznu.edu.cn/p/207

> **题意**：输出 $n$ 层倒三角形：第 $i$ 行有 $2(n-i)+1$ 个星号、前导 $n-i$ 个空格。$n \le 20$。

**代码**（0:07 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n;

//6min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
//	for(int i=n;i>=1;i--){
//		int nowi = (i-1)*2+1;
//		for(int j=1;j<=nowi;j++){
//			int nowj = n - i;
//			if(j <= nowj || (nowi - j))
//		}
//	}
	int len = (n-1)*2+1;
	for(int i=n;i>=1;i--){
		int nowi = (i-1)*2+1;
		for(int j=1;j<=(len-nowi)/2;j++) cout<<' ';
		for(int j=1;j<=nowi;j++) cout<<'*';
		for(int j=1;j<=(len-nowi)/2;j++) cout<<' ';
		cout<<'\n';
	}
	return 0;
}
```

### 解读

居中倒三角直接按公式打。一个小侥幸：题面说「行末不要输出多余空格」，这份代码每行末尾其实还挂着 $n-i$ 个空格——判题机过滤了行末空白，照样 AC。官方题解特意提醒「不要补齐每行右侧的空白」，下次别赌。

## D - 解绝对值方程（P1257）
https://oj.zznu.edu.cn/p/257

> **题意**：$|x - a| = b$ 的所有实数解。$b < 0$ 无解；$b = 0$ 唯一解 $x = a$；$b > 0$ 两解 $a \pm b$。$-10^6 \le a, b \le 10^6$，解均为整数。

**代码**（0:30 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int a,b,xi,xj;

//唐了 先看其他题目了 中间还绕了一下 29min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>a>>b;
//	xi = a+b,xj = a-b;
//	if(xi < a && xj > a) cout<<"No Answer";
//	else if(xi >= a) cout<<xi<<' ';
//	else if(xj <= a) cout<<xj<<' ';
	if(b < 0) cout<<"No Answer";
	else if(b == 0) cout<<a+b;
	else cout<<min(a+b,a-b)<<' '<<max(a+b,a-b);
	
	return 0;
}
```

### 解读

被划掉的初版在拿 $x \pm a$ 和 $a$ 比大小绕弯，反应过来 $b$ 的符号才是唯一分类依据后三行写完。`b == 0` 分支输出的 `a + b` 就是 $a$ 本身。官方题解的同款提醒：$b = 0$ 只输出一次、两解从小到大。

## E - 阶乘和（P1208）
https://oj.zznu.edu.cn/p/208

> **题意**：求 $1! + 2! + \dots + n!$ 的最后六位（不足六位按实际位数输出）。$n \le 10^6$。

**代码**（0:18 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e6+1,mod = 1e6;
ll ans,n;

//18min

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	ll res = 1;
	for(ll i=1;i<=n;i++) res = (res % mod * i % mod) % mod,ans = (ans % mod + res % mod) % mod;
	cout<<ans;
	return 0;
}
```

### 解读

标准「先乘后加」递推：$res$ 维护 $i! \bmod 10^6$，每轮乘 $i$ 后加进 $ans$——$res$ 从 1 起步，天然不会把 0! 加进答案（官方题解专门点过这个易错点）。取模乘法两边都先 `% mod` 防中间值溢出。一个冷知识：$n \ge 25$ 之后每一项末尾都有至少六个零（$25!$ 的 $v_5 = 6$），所以答案在 $n = 24$ 处就饱和了——本地拿 $n = 10^6$ 实测 51ms 输出 940313。

## F - 66ccff（P1258）
https://oj.zznu.edu.cn/p/258

> **题意**：$n$ 盏灯每盏六位编码 `66ccff` 或 `ee0000`（字母不分大小写），拼成长 $6n$ 的串。统计两种色的灯数和**最长连续同色段**长度。$n \le 10^4$。

**代码**（0:45 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int n,a,b,na,nb,c;
string s;

//45min

inline bool check1(int x){
	string tmp = "";
	for(int i=x;i<x+6;i++) tmp += s[i];
//	cout<<"now check1 is "<<tmp<<'\n';
	if(tmp[0] != '6' || tmp[1] != '6') return 0;
	if(!(tmp[2] == 'c' || tmp[2] == 'C') || !(tmp[3] == 'c' || tmp[3] == 'C')) return 0;
	if(!(tmp[4] == 'f' || tmp[4] == 'F') || !(tmp[5] == 'f' || tmp[5] == 'F')) return 0;
	return 1;
}

inline bool check2(int x){
	string tmp = "";
	for(int i=x;i<x+6;i++) tmp += s[i];
//	cout<<"now check2 is "<<tmp<<'\n';
	if(!(tmp[0] == 'e' || tmp[0] == 'E') || !(tmp[1] == 'e' || tmp[1] == 'E')) return 0;
	for(int i=2;i<6;i++) if(tmp[i] != '0') return 0;
	return 1;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n;
	cin>>s;
	for(int i=0;i<n;i++){
//		cout<<i<<' '<<a<<' '<<b<<' '<<c<<'\n';
//		int now = i*n;//唐完了
		int now = i*6;//唐完了
		if(check1(now)) a++,nb = 0,na++;
		else if(check2(now)) b++,na = 0,nb++;
		else na = 0,nb = 0;
		c = max(c,max(na,nb));
	}
	cout<<a<<' '<<b<<' '<<c;
	return 0;
}
```

### 解读

逐组扫，`na / nb` 维护当前连续段、换色即清零，`c = max(c, max(na, nb))`——首尾不相连，不用环形合并。注释里 `i * n` 那发「唐完了」是起点写错。官方的取巧更干净：两种编码首字符必然不同（`6` vs `e/E`），只看 `s[j*6]` 就能分色，连大小写都不用管。

## G - 完全平方回文数（P1204）
https://oj.zznu.edu.cn/p/204

> **题意**：无输入。输出所有「五位 + 回文 + 完全平方」的数，空格分隔、从小到大。

**代码**（0:15 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
int t,n;

//15min

inline bool check1(int x){
	int tmp = x,cnt = 0,res = 10000;
	while(tmp){
		cnt += (tmp % 10) * res;
		res /= 10;
		tmp /= 10;
	}
	return cnt == x;
}

inline bool check2(int x){
//	for(ll i=1;i*i<=1LL*x;i++){//O(89999 * √1e5) 1e6 能过吧
//		if(i*i == )
//	}
	int p = int(sqrt(x));//会不会有精度问题？
	if(p*p == x) return 1;
	for(int i=max(1,p-10);i<=min(x,p+10);i++){
		if(i*i == x) return 1;
	}
	return 0;
}

int main(){
//	cout<<check1(10101);
	ios::sync_with_stdio(false);
	cin.tie(0);
	for(int i=10000;i<=99999;i++){
		if(check1(i) && check2(i)) cout<<i<<' ';
	}
	return 0;
}
```

### 解读

七个数：**10201 12321 14641 40804 44944 69696 94249**。最容易漏的是 **94249 = 307²**——它确实是回文（94249 倒着读还是 94249）。`check2` 里 `int(sqrt(x))` 后再扫 ±10 邻域，是防浮点误差的标准兜底。官方的写法更省：直接枚举平方根 100…316（$317^2$ 已是六位），平方天然有序，连排序都省了，候选只有 217 个。

## H - 最大的偶数和（P1260）
https://oj.zznu.edu.cn/p/260

> **题意**：选一个整除 $b$ 的 $k$（允许 $k=1$），同时把 $a$ 变 $a \times k$、$b$ 变 $b / k$。求操作后 $a \times k + b / k$ 的最大**偶数**值；做不到输出 -1。$1 \le a, b \le 10^9$，答案可能超 32 位。

**代码**（1:16 一发过）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1;
ll a,b;

//1h 15min

void solve1(){
	vector<ll> c;
	ll tmp = b;
	for(ll i=1;i*i<=tmp;i++){
		if(tmp % i) continue;
		c.push_back(i),c.push_back(tmp/i),tmp /= i;
	}
	if(tmp) c.push_back(tmp);
	for(auto it : c) cout<<it<<' ';
	cout<<'\n';
	return;
}
//1000000000 1000000000
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>a>>b;
	
	vector<ll> d;
//	ll cnt = 0;
	for(ll i=1;i*i<=b;i++){//竟然这么快？
//		cnt++;
		if(b % i) continue;
		d.push_back(i);
	}
	ll ans = -1;
	for(auto it : d){
//		ll now = a*it + b/it;//注意还有另外一种选择 阳历三3 5 18
		ll now = a*it + b/it,now2 = a*(b/it) + it;
		if((now & 1) == 0) ans = max(ans,now);//唐 位运算优先级都记不清了
		if((now2 & 1) == 0) ans = max(ans,now2);
	}
	cout<<ans;
	return 0;
}
```

### 解读

因数成对出现：枚举 $j \le \sqrt b$，把 $k = j$ 和 $k = b/j$ **都**查一遍——漏掉后半边就会在样例 `3 5 → 16` 上翻车（$k=5$ 那次操作给出 $3 \times 5 + 1 = 16$）。$O(\sqrt b)$ 只有三万次循环，「竟然这么快？」——这就是值域枚举的日常。$(now \And 1) == 0$ 那个括号也留了案底：位运算优先级低于 `==`，不加大括号必翻车。通过率 87 / 556，全场第二低——新生赛里 $\sqrt b$ 配对枚举确实是道坎。

---

## 赛后总结

**成绩**：7 / 8，rank 16 / 446，罚时 4:50:31。C→G→E→D→F 五连一发开了个好头，H 的 $\sqrt b$ 配对枚举一发收敛；全部损耗集中在 A（两发 80 分）和 B（四发未出）。

**做得好的**：

- **开局的节奏**：前 45 分钟五题连发全过，C 开场 7 分钟就收了。
- **H 现场写对**：87 人通过的题一发收敛，$\sqrt b$ 配对枚举和 `(x & 1) == 0` 的括号坑都绕开了。
- **A 陷进去时先放下**：两发 WA 之后没有硬怼，转手把 H 收掉再回来收尾——虽然 A 最终也就拖到 0:56。

**不足**：

1. **A 的「想当然判定」**：第一版「全乘起来取模」同时踩了溢出和倍数误判两个坑（80 分 × 2）。`134` 这种反例开题时想一遍就能避开——判断类题的固定动作：全 1 数组、目标质数的倍数、单元素，各造一个。
2. **B 的工程细节三连**：数学推导一路正确，死在实现层——`eps` 声明成 `int` 截断成 0、四舍五入守卫 `||` 写成恒真并集（两发 45 分同因）、`exp2/log2` 赛时第一次用。45→45→95→95 的轨迹说明大方向一直对，**输出格式类修正必须拿边界值单测**（±0.004、0、负零），`fabsl` 版本终场后 11 秒才落盘，本地已验证样例与官方边界全过。
3. **库函数熟练度**：`exp2`、`log2`、`sqrtl` 这类基本数学函数在赛时是「探索度不到 1%」的状态。B 的 1 小时 24 分钟里，相当一部分花在了确认「这个函数存不存在」上。

补题清单：B 的终场版本地已通过全部样例与官方边界用例，OJ 补交待做。
