---
title: "牛客练习赛 159"
tags: [nowcoder, 题解]
aliases: ["/acm/27post/"]
date: 2026-11-06
draft: false
comments: true
upsolve:
  - problem: "D"
    name: "Crescent Flower"
    url: "https://ac.nowcoder.com/acm/contest/142560/D"
    status: "skip"
    note: "双人换位状态图最短路——全源 BFS 预处理 + (位置, 位置) 状态 Dijkstra，没开题"
  - problem: "E"
    name: "Faith Flower (Easy)"
    url: "https://ac.nowcoder.com/acm/contest/142560/E"
    status: "skip"
    note: "树上路径先后冲突建图 + 拓扑排序（LCA 判点是否在路径上），没开题"
  - problem: "F"
    name: "Eternal Flower"
    url: "https://ac.nowcoder.com/acm/contest/142560/F"
    status: "skip"
    note: "双指针维护区间 + 每种口味第一颗糖的增量计数，没开题"
---

> **30 秒版**：练习赛不计 rating。A/B/C 三题完成——A 预打表 343 种初始状态、B 把「二分 + 判定」反转成「枚举 k + 四前缀和」、C 在 n² 死局里连续四跳收敛到「分层 BFS + set 每点只死一次」。三题终版代码与官方题解参考代码本地对拍全绿（A 343 组、B 400 组、C 400 + 600 组大值域多测，另加划分合法性校验）。D/E/F 没开题。

比赛时间：2026-11-06 19:00 ~ 21:30（共 2h30，945 人报名）｜[官方题解](https://www.nowcoder.com/discuss/945753592042954752)

OJ 侧的判定记录没有抓到（这次接口没公开），三题的正确性以**本地对拍**为证：终版代码与官方题解附带的参考代码随机数据互测，A 全 343 组输入域、B 400 组、C 400 组再加 600 组大值域多测（并逐组校验 C 划分合法性），全部一致。下文时间线来自代码注释里的赛时标记。

<details class="tl-fold">
<summary>做题情况 —— 点开展开</summary>

- 0:17 A 第一发（注释「第一次提交 2h13min」= 剩 2h13，与 A.cpp 落盘 19:17:00 精确吻合）
- 0:30~0:58 B 第一版（单调栈/二分方向）——写到一半放弃，从未提交
- 1:13:15 B 第一发（B2.cpp 注释「第一次提交 01时 13分 15秒」；终版落盘 1:33:36）
- 2:17 C 第一发（剩余 13min，C.cpp 21:15 落盘）

</details>

## A - Amber Flower
https://ac.nowcoder.com/acm/contest/142560/A

> **题意**（按官方题解概括）：三盏灯各有初始颜色，每按一次按钮，三盏灯分别前进 $1、2、3$ 种颜色（按 $7$ 循环）。求最少的按键次数使三盏灯同色；若按多少次都不行，输出 $-1$。

**代码**：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5+1,mod = 7;
int t;
int ans[7][7][7];

//解同余方程 但是不需要这么麻烦应该 直接分套应该就行了 
//或者可能存在结论 可以直接美剧而且没巨量很小 这一点可以达标验证\
//首先要有一个简单的判断什么时候无解 可以自然的想到如果是一个环的话就不行（回到最初形态）
//或者尝试思考正解 要找到 最小的 m 使得 (a + m) == (b + 2m) == (c + 3m) mod 7
//a + m == x*7+xa 同理 y*7+yb z*7 + zc
//算了不想了 美剧好像能过
//共 2 h 30 min 第一次提交 2 h 13 min

int solve1(int a,int b,int c){
	int na = a,nb = b,nc = c;
	int cnt = 0,p = 0;
	while(na != nb || nb != nc || na != nc){//唐了一开始写的&&
		cnt++;
		na = (na + 1) % mod;
		nb = (nb + 2) % mod;
		nc = (nc + 3) % mod;
		if(na == a && nb == b && nc == c){
			p = 1;
			break;
		}
	}
	if(p == 1) return -1;
	else return cnt;
}

void pre(){
	for(int a=0;a<=6;a++){
		for(int b=0;b<=6;b++){
			for(int c=0;c<=6;c++){
				ans[a][b][c] = solve1(a,b,c);
			}
		}
	}
}

int main(){
//	cout<<solve1(1,1,2);
	ios::sync_with_stdio(false);
	cin.tie(0);
	pre();//卧槽直接美剧能过啊 我想想 甚至预先处理更好一些
	cin>>t;
	while(t--){
		int a,b,c;
		cin>>a>>b>>c;
//		cout<<solve1(a,b,c)<<'\n';
		cout<<ans[a][b][c]<<'\n';
	}
	return 0;
}
```

### 解读

同余方程 $a + m \equiv b + 2m \equiv c + 3m \pmod 7$ 的最小非负解。模拟整个状态环回到原点判无解，343 种初始状态全部预打表，查询 $O(1)$——注释里「卧槽直接美剧能过啊 我想想 甚至预先处理更好一些」。两处细节：终止条件该用 `||` 判「尚未全部相等」（`&&` 是开局踩的坑）；回到初始形态即环，直接判 -1。官方写法更轻：对每组输入直接枚举 $i \in [0, 6]$。对拍 343 组（全输入域）与官方完全一致。

## B - Blessing Flower
https://ac.nowcoder.com/acm/contest/142560/B

> **题意**（按官方题解概括）：$n$ 名游客站成一排，每人有朝向（`L` / `R`）和身高 $h_i$。一名游客能被拍到，当且仅当他**面向**那一侧、且比该侧的所有人都高（严格）。可以让队列**最前面的 $k$ 人**依次转身。求能被拍到的最大人数 $M$，以及取得最大值的最小转身人数 $k$。

**弃稿**（B.cpp，写到一半放弃——`#define ll long long` 和数组名 `ll` 撞宏，`cout<<ans<'\n'` 还少一个 `<`，**编译都过不去**，从未提交）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
int h[maxn],ll[maxn],lr[maxn],rl[maxn],rr[maxn];
string s;

//共 2 h 30 min 第一次提交 
//肯定有预处理 我的大脑已经往单调栈 二分答案靠拢了
//感觉单调栈不好写出来 先尝试写一个n^2logn的暴力
//肯定要预处理 最右两边的最大身高 以及可能还要对 L R 等进行操作
//不行思路太混乱了 重新写一遍  01时 31分 48秒


void pre(){
	ll[0] = 0,lr[n+1] = 0,rl[0] = 0,rr[n+1] = 0;
	for(int i=1;i<=n;i++){
		ll[i] = ll[i-1],rl[i] = rl[i-1];
		if(s[i-1] == 'L') ll[i] = max(ll[i],h[i]);
		if(s[i-1] == 'R') rl[i] = max(rl[i],h[i]);
	}
	for(int i=n;i>=1;i--){
		lr[i] = lr[i+1],rr[i] = rr[i+1];
		if(s[i-1] == 'L') lr[i] = max(lr[i],h[i]);
		if(s[i-1] == 'R') rr[i] = max(rr[i],h[i]);
	}
	return;
}

bool check(int x){
	int cnt = 0;
	for(int k=0;k<=n;k++){
		for(int i=1;i<=n;i++){
			
			if(cnt >= x) return 1;
		}
		if(cnt >= x) return 1;
		cnt = 0;
	}
	return 0;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>h[i];
		cin>>s;
		pre();
		int ans = 0,l = 0,r = n + 1,mid = 0;
		while(l <= r){
			mid = (l + r) >> 1;
			if(check(mid)) ans = mid,l = mid + 1;
			else r = mid - 1;
		}
		cout<<ans<'\n';
	}
	return 0;
}
```

**终版**（B2.cpp，1:13:15 第一次提交）：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 2e5+1;
int t,n;
int h[maxn];
int lm[maxn],rm[maxn];
int a1[maxn],a2[maxn],b1[maxn],b2[maxn];
int p1[maxn],p2[maxn],p3[maxn],p4[maxn];
string s;

//共 2 h 30 min 第一次提交 01时 13分 15秒
//先停下来思考 首先 预处理最优最大身高肯定没问题
//其次 问题现在主要是 怎么O(1)的判断 0 - k 中对应的 f(k) >= x 
//等等 如果我能求出来 f(k)的话为什么还要二分 直接 枚举所有 k 然后取 f(k) 最大值不就行了吗
//shit 到底要怎么写 上我想一想 我能通过预处理 O(1) 求出来 f(k)吗？
//f(k) 就是前 k 个翻一下 后面不动 数两边各拍到几个
//每个人能不能被拍 只看他朝哪 和 左/右最大身高
//k 一变只影响 i<=k 的朝向 别的不动
//所以每人 4 种情况是定死的 预处理一遍就完事
//然后 4 个前缀和 for k 一把 取最大 记 k
//草 那上面 pre 那 4 个数组其实不是我要的 白写了
//我是猪吗？？
//哦 可以用四颗前缀和来优化然后 p1 p2 p3 p4 四个前缀和
//左 = p2[k] + (p1[n]-p1[k])b 右 = p3[k] + (p4[n]-p4[k]) 总 = 左+右  一人只朝一边
//a1 L h>lm 不翻 左能拍  i>k
//a2 R h>lm 翻了变L 左能拍 i<=k
//b1 L h>rm 翻了变R 右能拍 i<=k
//b2 R h>rm 不翻 右能拍  i>k

void pre(){
    lm[1] = 0;
    for(int i=2;i<=n;i++) lm[i] = max(lm[i-1],h[i-1]);
    rm[n] = 0;
    for(int i=n-1;i>=1;i--) rm[i] = max(rm[i+1],h[i+1]);

    for(int i=1;i<=n;i++){
        a1[i]=a2[i]=b1[i]=b2[i]=0;
        if(s[i-1]=='L'){
            if(h[i]>lm[i]) a1[i]=1;
            if(h[i]>rm[i]) b1[i]=1;
        }else{
            if(h[i]>lm[i]) a2[i]=1;
            if(h[i]>rm[i]) b2[i]=1;
        }
    }
    for(int i=1;i<=n;i++){
        p1[i]=p1[i-1]+a1[i];
        p2[i]=p2[i-1]+a2[i];
        p3[i]=p3[i-1]+b1[i];
        p4[i]=p4[i-1]+b2[i];
    }
}


int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>t;
    while(t--){
		cin>>n;
		for(int i=1;i<=n;i++) cin>>h[i];
		cin>>s;
		pre();
		int mx=-1,mk=0;
		for(int k=0;k<=n;k++){
			int L = p2[k] + (p1[n]-p1[k]);
			int R = p3[k] + (p4[n]-p4[k]);
			int tot = L + R;
			if(tot > mx) mx = tot,mk = k;
		}
		cout<<mx<<" "<<mk<<"\n";
    }
    return 0;
}
```

### 解读

关键转折在注释里写得明明白白：「等等 如果我能求出来 f(k) 的话为什么还要二分 直接 枚举所有 k 然后取 f(k) 最大值不就行了吗」。弃稿把脑子锁死在「单调栈 + 二分答案」里，`check()` 空转的循环就是停工现场；终版的反转是——被拍与否只取决于**朝向**和**两侧的前缀最大身高**，转不转身只影响 $i \le k$ 的人，所以每人恰好四种定死的情形（`a1` 朝 L 不翻被左拍、`a2` 朝 R 翻成 L 被左拍、`b1` 朝 L 翻成 R 被右拍、`b2` 朝 R 不翻被右拍），四个 0/1 数组做前缀和之后：

$$L(k) = p_2[k] + (p_1[n] - p_1[k]),\quad R(k) = p_3[k] + (p_4[n] - p_4[k]),\quad f(k) = L(k) + R(k)$$

对所有 $k \in [0, n]$ 取最大即是答案，$O(n)$，二分整个消失。官方做法同质：基线 + 每人转身的增量 $\pm(R[k] - L[k])$ 前缀累加。注释里那句「草 那上面 pre 那 4 个数组其实不是我要的 白写了 我是猪吗？？」——弃稿的 `ll / lr / rl / rr` 在终版里确实一个都用不上。对拍 400 组随机数据（$n \le 40$，含平身高、全 L、全 R）与官方完全一致。

## C - Dawn Flower
https://ac.nowcoder.com/acm/contest/142560/C

> **题意**（按官方题解概括）：给定 $n$ 和**正**整数序列 $a$。把 $[1, n]$ 划分成若干段连续区间，段 $[l, r]$ 合法当且仅当 $l + a_l = r - a_r$。求最少段数并输出每段的右端点；无法划分输出 $-1$。

**代码**（2:17 提交，剩余 13 分钟）：

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5+1;
int t,n;
int a[maxn],b[maxn],c[maxn];
set<int> st[maxn];
int fa[maxn],ans[maxn],cnt;
queue<int> q;

//共 2 h 30 min 第一次提交 剩余时间 13min 
//相当于 l + al + ar == r
//已深度思考20min 只能想到n^2做法
//n^2筛出来所有合法的 l,r 然后 去进行贪心的区间合并
//我的发 我真急哭了 我真不会
//等  一  下  我们注意到！！ 可以对 l+a[l] 和 r+a[r]好i下那个可以预处理然后进行查找
//设 b[i] = a[i] + i,c[i] = i - a[i];那就是找 b[i] == p == c[j](i <= p <= j) 但是现在还是n^2的 肯定还能再发现什么性质
//噢噢噢噢 注意到 1 <= a[i] 所以 l < b[l] c[r] < r 天然成立 
//所以 l < p < r 也天然成立
//嘶 但是这个似乎对 优化时间复杂度没什么帮助
//卧   槽 不会是个土伦吧 好像之前见过类似的处理 想办法把 n^2 弄成边就好办 因为可以用一些神奇方法优化凸轮
//想一下 我们现在想要 从1开始 b[l] == c[r] 卧槽卧槽这不就是建一条边吗 然后跑最短路（或者bfs 感觉这俩时间复杂度等价吧 都至少跑一遍所有的边）
//嘶 但是问题在于现在建立边数是n^2的时间复杂度 而最多有 n*(n-1) 条边
//fuck 还要考虑建模问题 
//现在我们开始思考：嗯 假设现在有若干队边(l,r) 我们从 1 开始 每一个点我们都进行了访问 对于 已经访问过的 r 他只能出 而且类似于dp一样的
//不管他从哪一个 l 来(如果我们用bfs的话 他自带最短路性质) 都不会影响r后面的路 所以每一个r只用走一次（？）就行了
//嗯 让我们再想一想 所以我们现在存所有r 对应的 l 访问到哪个 r 了 就舍弃 他之前的 l 这样比直接建图跑dji小多了
//现在想一想 这么快速的求出所有(l,r)
//wdf!! 可以动态的按 c[r] 分组 每组扔个 set 存 r
//bfs 到一个 l 就去看 b[l] 那组 把里面 > l 的 r 全捞出来
//捞一个就把 r+1 塞队列 然后把 r 从 set 删掉 每个 r 只死一次
//保证每一个元素只进出一次 (nlogn) 
//fack 挑了半天 注意 c可能负 b也可能超
//我的发初始化得写好要不然会超 还有加跳表快速查

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    while(t--){
        cin>>n;
        for(int i=1;i<=n;i++) cin>>a[i];
        for(int i=1;i<=n;i++) b[i] = i + a[i],c[i] = i - a[i];
        for(int i=0;i<=n+1;i++) st[i].clear();
        for(int i=1;i<=n;i++) if(c[i] >= 2 && c[i] <= n-1) st[c[i]].insert(i);//唐
        for(int i=0;i<=n+1;i++) fa[i] = -1;
        
		while(!q.empty()) q.pop();
        q.push(1),fa[1] = 0;
        while(!q.empty()){
            int l = q.front();
			q.pop();
            if(l == n+1) break;
            int p = b[l];
            if(p < 2 || p > n-1) continue;
            auto it = st[p].lower_bound(l+1);
            while(it != st[p].end()){
                int r = *it;
                it = st[p].erase(it);
                int nx = r + 1;
                if(fa[nx] == -1) fa[nx] = l,q.push(nx);
            }
        }
        if(fa[n+1] == -1){
			cout<<-1<<"\n";
			continue;
		}
        cnt = 0;
        int cur = n + 1;
        while(cur != 1) ans[++cnt] = cur - 1,cur = fa[cur];
        reverse(ans+1,ans+cnt+1);//唐
        cout<<cnt<<'\n';
        for(int i=1;i<=cnt;i++) cout<<ans[i]<<' ';
        cout<<'\n';
    }
    return 0;
}
```

### 解读

这段注释是全场最值钱的一段思考记录——从 $n^2$ 死局到正解只用了四跳：

1. **变形**：$l + a_l = r - a_r$ 等价于设 $b[l] = l + a_l$、$c[r] = r - a_r$ 后找 $b[l] = c[r]$；
2. **建模**：「从 1 开始，$b[l] = c[r]$ 的 $(l, r)$ 就是建一条边」——土伦（图论）嗅觉上线；
3. **减边**：每个 $r$ 第一次被访问后，它出发的后路不受来源影响——**每个 $r$ 只走一次，用完即弃**；
4. **数据结构**：按 $c[r]$ 分组扔 `set`，BFS 到一个 $l$ 就把组内大于 $l$ 的 $r$ 全部捞出，每个元素只进出一次，$O(n \log n)$。

尾段注释的两个现场坑也都对应代码：`c[r]` 可能为负、`b[l]` 可能超界（$a_i$ 大的时候），所以插入限定 $2 \le c[r] \le n-1$、转移前判 $2 \le b[l] \le n-1$——在「$a_i$ 为正」的前提下 $l < b[l] \le n-1$、$2 \le c[r] < r$ 天然成立，卡界不丢解。方案重建用 `fa` 回溯到 $n+1$ 再 `reverse`。

官方做法殊途同归：从右往左 dp，`map` 按 $i - a_i$ 分组存「最小剩余段数 + 右端点」——一个从起点分层推进、一个从终点回填最小段数，分组思想同源。对拍 400 组随机 + 600 组大值域多测（单发与 $t=5$ 多测两种喂法），段数与官方零分歧、划分合法性逐组校验全过。

## D / E / F（未开题）

三题只读了官方题解，赛时没碰，一句话挂号：

- **D Crescent Flower**：无向图上两人从 $s, t$ 出发，每步移动一人、移动后两人不得同点且两人间最短路 $\le k$，求恰好互换位置的最少步数。官方做法：每个点作起点的 BFS 全源最短路预处理，再把「两人各自的位置」看作状态跑 Dijkstra。
- **E Faith Flower (Easy)**：树上 $m$ 个球各有一条路径，路径有先后冲突（一球的起点/终点落在另一球路径上就得让路），求合法移动顺序或判无解。官方做法：LCA 判「点是否在路径上」，$O(m^2)$ 建图跑拓扑排序（本场放的是 Easy，$m$ 小）。
- **F Eternal Flower**：双指针维护区间 + 预处理每颗糖同口味的前驱/后继（判断它是不是当前区间里该口味的第一颗），增量维护盒中不协调二元组数。

---

## 赛后总结

**成绩**：A/B/C 三题完成（提交时刻见时间线；OJ 判定记录没抓到，终版代码与官方参考代码对拍全绿——A 全输入域 343 组、B 400 组、C 400 + 600 组多测并逐组校验划分合法性）。练习赛不计 rating。

**做得好的**：

- **A 的打表直觉**：「卧槽直接美剧能过啊 我想想 甚至预先处理更好一些」——343 张表换 $O(1)$ 查询，稳妥且零边界风险。
- **B 的自我反转**：从「单调栈 + 二分答案」的死胡同里跳出（「等等 如果我能求出来 f(k) 的话为什么还要二分」），终版四前缀和 $O(n)$ 干净收场。
- **C 的四跳收敛**：20 分钟只想到 $n^2$ 的局面下，变形 → 建图 → 「每个 r 只死一次」 → set 分组，四步全对，2:17 压哨提交（剩余 13 分钟）。

**不足**：

1. **B 的弃稿成本**：单调栈方向从落笔到放弃大约耗掉半小时（0:30–0:58 成文，之后推倒重写），而弃稿连编译都没过——`#define ll long long` 撞上数组名 `ll` 是五秒钟就能发现的事。写「探索性草稿」时至少让它保持可编译。
2. **C 的压哨提交**：第一发落在剩余 13 分钟，`reverse` 标着「唐」——再早 20 分钟，D 至少能读一遍题面。
3. **后三题零接触**：D/E/F 三道全部挂着「没开题」。D 的双人状态图和 E 的树上拓扑都是可读出套路的题（官方题解正文里都有完整代码），下次前缀题目收完，剩余 20 分钟应该用来**读题**而不是盯提交。
