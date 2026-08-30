---
title: "Codeforces Round 1117 (Div. 2)"
date: 2026-08-17
draft: false
comments: true
---

![CF1117Div2](/img/acm/CF1117Div2.png)
![CF1117Div2提交记录](/img/acm/CF1117Div2_submit.png)

## A
https://codeforces.com/contest/2257/problem/A

> 海狸有一个初始包含 $n$ 个单词的集合 $S$。然后他进行了 $m$ 次操作：
> - 海狸从集合 $S$ 中选出一个或多个单词组成一个序列（同一个单词可以在序列中出现多次），取序列中每个单词的首字母，构成一个**缩写**。
> - 然后海狸将这个缩写加入集合 $S$，之后可以像普通单词一样使用它。
>
> 给定初始的 $n$ 个单词，以及海狸形成的 $m$ 个缩写。判断是否存在一种合适的操作顺序，使得这些缩写都能依次被生成。

**输入**

每个测试点包含多个测试用例。第一行包含测试用例数 $t$（$1 \le t \le 500$）。

每个测试用例的第一行包含两个整数 $n$ 和 $m$，分别表示普通单词数和缩写数（$1 \le n, m \le 100$）。

接下来 $n$ 行，每行一个字符串 $w_i$，表示一个普通单词（$1 \le |w_i| \le 20$）。

接下来 $m$ 行，每行一个字符串 $a_i$，表示一个缩写（$1 \le |a_i| \le 20$）。

所有普通单词由**小写**英文字母组成，所有缩写由**大写**英文字母组成。每个测试用例中，所有字符串 $w_1, w_2, \dots, w_n, a_1, a_2, \dots, a_m$ 两两不同。所有测试用例的字符串总长度不超过 $50000$。

**输出**

对于每个测试用例，如果存在合适的生成顺序，输出 `YES`，否则输出 `NO`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxx = 100010;
#define ll long long
int t,n,m;
string s;
bool pd[30];
int main(){
        ios::sync_with_stdio(false);
        cin.tie(0);
        cin>>t;
        while(t--){
                memset(pd,0,sizeof(pd));
                cin>>n>>m;
                while(n--){
                        cin>>s;
                        int now = s[0] - 'a';
                        pd[now] = 1;
                }
                bool ans = 1;
                while(m--){
                        cin>>s;
                        for(int i=0;i<s.length();i++) if(!pd[s[i] - 'A']) ans = 0;
                }
                if(ans) cout<<"YES"<<'\n';
                else cout<<"NO"<<'\n';
        }
        return 0;
}
```
/*
一个缩写能被生成，当且仅当它的每个字母都对应某个可用单词的首字母。初始时可用首字母就是 $n$ 个普通单词的首字母。一旦某个缩写被生成，它也可以作为普通单词使用，但其首字母并没有新增任何东西（因为缩写的首字母一定来自已有单词的首字母）。因此，所有能生成的缩写，其每个字母都必须属于初始单词的首字母集合。只需检查每个缩写中的每个大写字母是否都有对应的初始单词首字母即可。
*/

## B
https://codeforces.com/contest/2257/problem/B

> 两个巨人 Bea 和 Ver 在玩游戏，各自有一座山脉。Bea 的山脉高度为 $a_1, a_2, \dots, a_n$（从左到右编号），Ver 的山脉高度为 $b_1, b_2, \dots, b_m$（从右到左编号）。两座山脉的高度均按**非递增**顺序排列（即 $a_i \ge a_{i+1}$，$b_i \ge b_{i+1}$）。初始时两个巨人都站在各自山脉的 1 号山峰上，面对面。每回合，巨人向他对手所在的山峰扔一块巨石，使该山峰高度减少 1。如果巨人发现正前方的山峰高度比当前所在山峰高 1，他就跳到那座山峰上。如果巨人发现自己站在高度为 0 的地面上且前方没有更多山峰，他就认输。Bea 先手。请判断谁会获胜。

**输入**

每个测试点包含多个测试用例。第一行包含测试用例数 $t$（$1 \le t \le 500$）。

每个测试用例第一行包含两个整数 $n, m$（$1 \le n, m \le 100$）。

第二行包含 $n$ 个整数 $a_1, a_2, \dots, a_n$（$1 \le a_i \le 10^9$，保证非递增）。

第三行包含 $m$ 个整数 $b_1, b_2, \dots, b_m$（$1 \le b_i \le 10^9$，保证非递增）。

**输出**

若 Bea 获胜输出 `1`，若 Ver 获胜输出 `2`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
#define ll long long
int t,n,m;
ll a[maxn],b[maxn];
ll asum,bsum;
int main(){
        ios::sync_with_stdio(false);
        cin.tie(0);
        cin>>t;
        while(t--){
                cin>>n>>m;
                asum = 0,bsum = 0;
                for(int i=1;i<=n;i++) cin>>a[i];
                for(int i=1;i<=m;i++) cin>>b[i];
                int ans = 1;
                for(int i=1;i<n;i++) asum += a[i] - a[i+1] + 1;
                asum += a[n];
                for(int i=1;i<m;i++) bsum += b[i] - b[i+1] + 1;
                bsum += b[m];
                if(asum >= bsum) ans = 1;
                else ans = 2;
                cout<<ans<<"\n";
        }
        return 0;
}
```
/*
关键在于计算每个巨人能“存活”的回合数。由于山脉高度非递增，巨人只会向前跳到高度恰好比当前高 1 的山峰。从一个高度 $h$ 的山峰出发，能连续跳过的山峰数量为 $h - h_{next} + 1$。因此 Bea 的总可跳步数为 $a_n + \sum_{i=1}^{n-1} (a_i - a_{i+1} + 1)$，Ver 同理。比较两者大小即可。
*/

## C
这个C真是卡的太久了 T_T 一开始甚至想：？这不是排个序直接输出就行了吗？如果根节点1也是必经节点的话就把第一个节点去掉输出
然后一想：不怼 肯定没有那么简单 然后开始深度思考 没绷住 调了半天还调错了 猪来了
![依旧灵魂画手](/img/acm/CF1117Div2C.png)
https://codeforces.com/contest/2257/problem/C

> 给定一棵以 1 为根的树，有 $n$ 个顶点。海狸从根出发，沿着树边走到某个水坝所在的顶点。水坝位于 $a_1, a_2, \dots, a_m$ 这些顶点中的某一个（但具体是哪一个未知）。你可以在树的**边**上放置摄像头。如果海狸经过一条有摄像头的边，你就会观察到。在所有移动结束后，你会获得海狸经过的所有带摄像头的边的序列。你需要用**最少数量的摄像头**，使得无论海狸去往哪个水坝，你都能根据观察到的边序列**唯一确定**它的目的地。请输出最少摄像头数量 $k$ 以及这些摄像头应放置的边。

**输入**

每个测试点包含多个测试用例。第一行包含测试用例数 $t$（$1 \le t \le 2 \times 10^4$）。

每个测试用例第一行包含整数 $n$（$2 \le n \le 10^5$）。

第二行包含 $n-1$ 个整数 $p_2, p_3, \dots, p_n$，表示顶点 $2$ 到 $n$ 的父节点（$1 \le p_i < i$）。

第三行包含整数 $m$（$1 \le m \le n$）。

第四行包含 $m$ 个整数 $a_1, a_2, \dots, a_m$，表示水坝所在的顶点。

所有测试用例的 $n$ 之和不超过 $10^5$。

**输出**

对于每个测试用例，第一行输出 $k$。如果 $k > 0$，在同一行输出 $k$ 个整数，表示放置摄像头的边的**子节点端**的顶点编号（顺序任意）。如果 $k = 0$，则只输出一行 `0`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 100010;
#define ll long long
int t,n,m,k;
int p[maxn];
bool pd[maxn];
int ans[maxn],cnt[maxn];
vector<int> b[maxn];
int base;

int dfs(int x){
    for(int i=0;i<b[x].size();i++){
        int nxt = b[x][i];
        cnt[nxt] = cnt[x] + 1;
        dfs(nxt);
    }
    return cnt[x];
}

void dfs2(int x){
    if(pd[x] && x != base) ans[++k] = x;
    for(int i=0;i<b[x].size();i++) dfs2(b[x][i]);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    while(t--){
        k = 0;
        cin>>n;
        for(int i=2;i<=n;i++){
            cin>>p[i];
            b[p[i]].push_back(i);
        }
        cin>>m;
        for(int i=1;i<=m;i++){
            int a;
            cin>>a;
            pd[a] = 1;
        }
        if(m == 1) cout<<"0\n";
        else{
            cnt[1] = 0;
            dfs(1);
            base = -1;
            for(int i=1;i<=n;i++) if(pd[i] && (base == -1 || cnt[i] < cnt[base])) base = i;
            dfs2(1);
            cout<<k;
            for(int i=1;i<=k;i++) cout<<' '<<ans[i];
            cout<<'\n';
        }
        for(int i=1;i<=n;i++){
            b[i].clear();
            pd[i]=false;
            cnt[i]=0;
        }
    }
    return 0;
}
```
/*
要唯一确定海狸去了哪个水坝，只需要区分所有可能的水坝顶点。最优策略是：找到深度最小的水坝顶点作为“基准”，然后在所有其他水坝顶点到根的路径上放置摄像头。具体地，先 DFS 求出每个点的深度，找到深度最小的标记点作为 base；再遍历整棵树，输出所有其它标记点（即在这些点的父边上放摄像头）。这样每个非基准水坝都会被唯一的一条带摄像头的边区分开。
*/

## D
https://codeforces.com/contest/2257/problem/D

一眼数学题

> 海狸正在探索“百慕大矩形”。百慕大矩形的面积为 $S$，边长为整数，左下角位于 $(0,0)$。有 $q$ 个询问，每个询问给出一个矩形，边长为 $x$ 和 $y$，左下角位于 $(0,0)$。海狸想知道，在这个询问矩形中，有多少个格子**可能**位于某个合法的百慕大矩形内部。一个格子被认为是“可能位于”的，如果存在一个满足面积 $S$ 且边长为整数的矩形包含该格子。

**输入**

每个测试点包含多个测试用例。第一行包含测试用例数 $t$（$1 \le t \le 10000$）。

每个测试用例第一行包含两个整数 $S$ 和 $q$（$1 \le S \le 10^{14}$，$1 \le q \le 3 \cdot 10^5$）。

接下来 $q$ 行，每行两个整数 $x, y$（$1 \le x, y \le S$）。

所有测试用例的 $q$ 之和不超过 $3 \cdot 10^5$，$\sum \sqrt{S}$ 不超过 $10^7$。

**输出**

对于每个询问，输出一个整数表示答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 200005;
ll S,x,y,ans;
ll a[maxn], len[maxn], val[maxn], prefLen[maxn], prefVal[maxn];
int q,k;

int main(){
        ios::sync_with_stdio(false);
        cin.tie(0);
        int tc;
        cin>>tc;
        while(tc--){
                cin>>S>>q;
                k=0;
                for(ll i=1;i*i<=S;i++){
                        if(S%i==0){
                                a[++k]=i;
                                if(i*i!=S) a[++k]=S/i;
                        }
                }
                sort(a+1,a+1+k);
                ll last=0;
                for(int i=1;i<=k;i++){
                        len[i]=a[i]-last;
                        val[i]=S/a[i];
                        last=a[i];
                }
                for(int i=1;i<=k;i++){
                        prefLen[i]=prefLen[i-1]+len[i];
                        prefVal[i]=prefVal[i-1]+len[i]*val[i];
                    }
                while(q--){
                        cin>>x>>y;
                        x=min(x,S);
                        int r=upper_bound(a+1,a+1+k,x)-a-1;
                        int t=upper_bound(a+1,a+1+k,S/y)-a-1;
                        ans=0;
                        if(r>=1){
                                int mid=min(r,t);
                                if(mid>=1) ans += (prefLen[mid]-prefLen[0])*y;
                                if(r>t) ans += (prefVal[r]-prefVal[t]);
                        }
                        if(r+1<=k && x>a[r]){
                                int idx=r+1;
                                ll part=x-a[r];
                                if(idx<=t) ans += part*y;
                                else ans += part*val[idx];
                        }
                        cout<<ans<<"\n";
                }
        }
        return 0;
}
```
/*
百慕大矩形的所有可能形状为 $(d, S/d)$，其中 $d$ 是 $S$ 的因子。对于询问 $(x,y)$，答案等于 $\sum_{i=1}^{x} \min(\lfloor S/i \rfloor, y)$。$\lfloor S/i \rfloor$ 的取值在 $i$ 的不同区间内保持不变，且这些区间端点都是 $S$ 的因子。枚举 $S$ 的所有因子并排序，将数轴按因子分成若干段。每段内 $f(i)=\lfloor S/i \rfloor$ 的值相同，预处理长度前缀和、长度乘 $f(i)$ 的前缀和。对每个询问 $(x,y)$，用二分找到 $x$ 和 $S/y$ 所在的位置，然后利用前缀和 $O(\log k)$ 回答。
*/

## E
https://codeforces.com/contest/2257/problem/E

> 海狸成立了一家建筑公司。公司初始资金为 $x$ 胡萝卜，有 $n$ 个建筑项目可供选择。每个项目 $i$ 有 $m_i$ 层楼可建。建造第 $i$ 个建筑的第 $j$ 层需要花费 $a_{i,j}$，建完后立即获得收益 $b_{i,j}$，资金会实时更新。你可以在不同项目之间任意切换，也可以不完成某个项目。目标是**建造尽可能高的楼**（即总层数最大）。如果有多个项目都能达到这个最大层数，输出**编号最小**的项目。

**输入**

每个测试点包含多个测试用例。第一行包含测试用例数 $t$（$1 \le t \le 3 \times 10^4$）。

每个测试用例第一行包含两个整数 $n$ 和 $x$（$1 \le n \le 2 \times 10^5$，$0 \le x \le 10^{18}$）。

接下来 $n$ 个项目描述，每个项目包含：

- 第一行：$m_i$（$1 \le m_i \le 2 \times 10^5$）
- 第二行：$m_i$ 个整数 $a_{i,1}, a_{i,2}, \dots, a_{i,m_i}$（$0 \le a_{i,j} \le 10^9$）
- 第三行：$m_i$ 个整数 $b_{i,1}, b_{i,2}, \dots, b_{i,m_i}$（$0 \le b_{i,j} \le 10^9$）

所有测试用例的 $\sum m_i$ 不超过 $2 \times 10^5$。

**输出**

对于每个测试用例，输出两个整数：最大层数，以及能达到该层数的**最小项目编号**。

```cpp
// 本题代码未提供，请自行实现
```
/*
对于每个项目独立计算最多能建多少层。由于资金可以跨项目使用，但建造每一层都需要先有足够的钱支付 $a_{i,j}$，建完后钱增加 $b_{i,j}$。如果 $b_{i,j} \ge a_{i,j}$，则该层是“赚钱”的，建了不会亏；如果 $b_{i,j} < a_{i,j}$，则是“亏钱”的，需要先用其他项目赚到足够的钱再来建。最优策略是：先尽可能多地建所有“赚钱”的层（按所需资金从小到大排序），积累资金；然后再尝试建“亏钱”的层。对每个项目分别模拟即可，取能建层数最多的项目，若相同则取编号小的。
*/

## F1
https://codeforces.com/contest/2257/problem/F1

> 这是简单版本，约束为 $x \le 5$。海狸在训练跳跃。赛道由 $n$ 个平台组成，第 $i$ 个平台有 $d_i$ 个单元格。如果海狸站在平台 $i$ 上起跳并**落回同一个平台**，则会产生 $s_i$ 惩罚；否则（跳到其他平台）没有惩罚。海狸每次可以向前跳**不超过 $x$** 个单元格的任意整数距离（可以跳过多个平台）。有 $q$ 个操作，包含单点修改（修改某个平台的 $d_i$ 或 $s_i$）和区间查询（查询从平台 $l$ 到 $r$ 的最小惩罚）。

**输入**

第一行包含三个整数 $n, q, x$（$1 \le n \le 10^6$，$1 \le q \le 10^4$，$1 \le x \le 5$）。

第二行包含 $n$ 个整数 $d_i$（$1 \le d_i \le 10^7$）。

第三行包含 $n$ 个整数 $s_i$（$1 \le s_i \le 10^5$）。

接下来 $q$ 行，每行一个操作：

- `1 i v`：将第 $i$ 个平台的长度改为 $v$（$1 \le v \le 10^7$）
- `2 i y`：将第 $i$ 个平台的惩罚改为 $y$（$1 \le y \le 10^5$）
- `? l r`：查询从平台 $l$ 到 $r$ 的最小惩罚

**输出**

对于每个 `?` 操作，输出一个整数表示最小惩罚。

```cpp
// 本题代码未提供，请自行实现
```
/*
$x$ 很小（$\le 5$），这意味着从一个平台出发，能跳到的“下一个平台”是有限的。可以用线段树维护区间信息：每个节点维护一个 $x \times x$ 的 DP 矩阵，表示从区间左端进入时的“偏移量”到从右端出去时的“偏移量”的最小惩罚。合并时做矩阵乘法（min-plus 卷积）。单点修改时更新叶子节点并向上合并。查询时合并对应区间的矩阵，最后取最小值。
*/

## F2
https://codeforces.com/contest/2257/problem/F2

> 这是困难版本，约束为 $x \le 10$。题意与 F1 相同。

**输入**

同 F1，但 $x \le 10$。

**输出**

同 F1。

```cpp
// 本题代码未提供，请自行实现
```
/*
与 F1 思路相同，使用线段树维护 $x \times x$ 的 DP 矩阵进行区间合并。由于 $x$ 最大为 10，矩阵大小为 $10 \times 10$，合并复杂度为 $O(x^3)$，可以接受。注意 $n$ 较大（$10^6$），需要使用高效的输入输出。
*/