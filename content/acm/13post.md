---
title: "AtCoder Beginner Contest 473"
date: 2026-08-29
draft: false
comments: true
---
![ABC473](/img/acm/ABC473.png)
![ABC473提交记录](/img/acm/ABC473_submit.png)
## A
https://atcoder.jp/contests/abc473/tasks/abc473_a

> 给定一个长度为 $n$ 的正整数序列 $a_1, a_2, \dots, a_n$。求序列**后半部分**的和，即 $\sum_{i=\lfloor n/2 \rfloor + 1}^{n} a_i$。

**输入**

输入格式如下：
```
n
a_1 a_2 ... a_n
```

**数据范围**

- $1 \le n \le 100$（由 `maxn = 101` 推断）
- $1 \le a_i \le 10^9$

**输出**

输出一个整数，表示后半部分的和。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 101;
#define ll long long 
int n,t;
int a[maxn];
int ans;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=n/2+1;i<=n;i++) ans += a[i];
    
    cout<<ans;
    return 0;
}
```
/*
从 $\lfloor n/2 \rfloor + 1$ 开始累加后半部分即可。
*/

## B
https://atcoder.jp/contests/abc473/tasks/abc473_b

> 给定一个长度为 $n$ 的正整数序列，统计其中出现次数为**奇数**的数的和。

**输入**

输入格式如下：
```
n
a_1 a_2 ... a_n
```

**数据范围**

- $1 \le n \le 100$
- $1 \le a_i \le 100$

**输出**

输出一个整数，表示所有出现奇数次的数之和。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 101;
#define ll long long 
int n,a,ans;
int tot[maxn];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a,tot[a]++;
    for(int i=1;i<=100;i++) ans += ((tot[i]%2==1)?i:0);
    cout<<ans;
    return 0;
}
```
/*
用桶统计每个数的出现次数，遍历桶将出现奇数次的数累加。
*/

## C
https://atcoder.jp/contests/abc473/tasks/abc473_c

> 有 $n$ 个班级，每个班级有一个编号 $a_i$（$1 \le a_i \le n$），表示该班级的学生人数。如果一个班级的人数与**出现次数最多**的班级人数相等，或者比出现次数最多的班级人数**少 1**，则称该班级为“合法班级”。求合法班级的个数。

**输入**

输入格式如下：
```
n k
a_1 a_2 ... a_n
```

**数据范围**

- $1 \le n \le 2 \times 10^5$（由 `maxn = 2e5+1` 推断）

**输出**

输出合法班级的个数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5+1;
#define ll long long 
int n,a,k,ans;
int c[maxn];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    for(int i=1;i<=n;i++) cin>>a,c[a]++;
    sort(c+1,c+1+n);
    for(int i=1;i<=n;i++) if(c[i]+1 >= c[n]) ans++;
    
    cout<<ans;
    return 0;
}
```
/*
统计每个班级人数（即每个编号的出现次数），找到出现次数的最大值 mx。遍历所有班级，若其出现次数等于 mx 或 mx-1 则累加答案。
*/

## D
前三题都直接秒掉，捏妈妈的这个D卡的太久了，可劲调这个剪枝
https://atcoder.jp/contests/abc473/tasks/abc473_d

> 给定两个整数 $n$ 和 $k$，求所有满足以下条件的长度为 $n$ 的非负整数序列 $a_1, a_2, \dots, a_n$：
> - $\sum_{i=1}^{n} i \cdot a_i = k$
>
> 按字典序从小到大输出所有方案。

**输入**

输入格式如下：
```
n k
```

**数据范围**

- $1 \le n \le 10$（由 `maxn = 11` 推断）
- $1 \le k \le 3 \times 10^5$

**输出**

按字典序从小到大输出所有满足条件的序列，每个序列占一行，数字之间用空格分隔。

---

**解法思路**：

这是一个经典的整数拆分问题，将 $k$ 拆分成 $n$ 个部分，第 $i$ 部分的权重为 $i$。由于 $n \le 10$，可以暴力搜索所有可能的分配方案。

搜索时从大权重到小权重枚举，可以提前剪枝：若当前剩余和小于当前权重，则不可能再分配。当递归到 $now=2$ 时，枚举 $a_2$ 的取值，剩余部分全部由 $a_1$ 补足，这样可以避免再枚举 $a_1$，减少一层循环。

最后将所有方案按字典序排序输出（字典序即先比较 $a_1$，再比较 $a_2$，以此类推）。

---

**三个版本的代码及说明**：

### 版本 1（D.cpp）：朴素 DFS，无剪枝
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 11;
#define ll long long 
int n,k;
int a[maxn];
inline int check(){
    int tmp = 0;
    for(int i=1;i<=n;i++){
        if(!a[i]) continue;
        tmp += a[i] * i;
    }
    return tmp;
}
void dfs(int now){
    int nowvlu = check();
    if(nowvlu > k) return;
    if(nowvlu == k){
        for(int i=1;i<=n;i++) cout<<a[i]<<' ';
        cout<<'\n';
        return;
    }
    if(now > n) return;
    for(int i=0;i<=k/now;i++){
        a[now] = i;
        dfs(now+1);
    }
    a[now] = 0;
    return;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    dfs(1);
    return 0;
}
```
**说明**：从 $1$ 到 $n$ 依次枚举每个 $a_i$，每次用 `check()` 计算当前和，若超过 $k$ 则回溯。由于没有剪枝且每次递归都重新计算和，效率很低，$k$ 较大时会超时。

### 版本 2（D2.cpp）：尝试用字符串存储并排序，但有 bug
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 11,maxm = 3e5+1;
#define ll long long 
int n,k,tot;
int a[maxn];
struct node{
    string s = "";
}ans[maxm];
bool cmp(const node& a,const node &b){
    return a.s < b.s;
}
void dfs(int now,int last){
    if(last < 0) return;
    if(last == 0){
        ++tot;
        string tmp = "";
        for(int i=1;i<=n;i++) tmp += (a[i] + '0');
        ans[tot].s = tmp;
        return;
    }
    if(last < now) return;
    if(now < 1) return;
    for(int i=0;i<=k/now;i++){
        a[now] = i;
        dfs(now-1,last-i*now);
    }
    a[now] = 0;
    return;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    dfs(n,k);
    sort(ans+1,ans+1+tot,cmp);
    for(int i=1;i<=tot;i--){   // 错误：i-- 导致死循环且输出方向错
        for(int j=0;j<n;j++){
            cout<<ans[i].s[j]<<' ';
        }
        cout<<'\n';
    }
    return 0;
}
```
**说明**：从 $n$ 到 $1$ 递归（先决定大权重），并用 `last` 传递剩余和，剪枝条件 `last < now` 提前返回。将方案存为字符串，最后排序。但输出部分的 `for(int i=1;i<=tot;i--)` 是死循环，且排序后输出顺序错误（i-- 会从1开始递减），导致 bug。

### 版本 3（D3.cpp）：最终正确版本
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, k;
int a[11];                  // 临时存放当前方案 (a[1]~a[n])
vector<vector<int>> ans;   // 存储所有方案

// 递归处理面额 now, now 从 n 递减到 2
void dfs(int now, int rem) {
    if (now == 2) {
        // 只剩面额 2 和 1，枚举 a2
        for (int cnt = 0; cnt <= rem / 2; ++cnt) {
            a[2] = cnt;
            int a1 = rem - 2 * cnt;   // 剩余全部由面额 1 补足
            if (a1 < 0) break;        // cnt 递增，a1 递减，一旦为负后续更小
            a[1] = a1;
            // 将当前方案存入答案
            vector<int> sol;
            for (int i = 1; i <= n; ++i) sol.push_back(a[i]);
            ans.push_back(sol);
        }
        return;
    }

    // 枚举当前面额 now 的使用数量
    int upper = rem / now;
    for (int cnt = 0; cnt <= upper; ++cnt) {
        a[now] = cnt;
        dfs(now - 1, rem - cnt * now);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> k;

    // n=1 时只有一种方案
    if (n == 1) {
        cout << k << '\n';
        return 0;
    }

    dfs(n, k);

    // 按字典序排序 (a1 优先，其次 a2...)
    sort(ans.begin(), ans.end(), [](const vector<int>& x, const vector<int>& y) {
        for (int i = 0; i < (int)x.size(); ++i) {
            if (x[i] != y[i]) return x[i] < y[i];
        }
        return false;
    });

    // 输出所有方案
    for (const auto& sol : ans) {
        for (int i = 0; i < n; ++i) cout << sol[i] << ' ';
        cout << '\n';
    }

    return 0;
}
```
**说明**：从 $n$ 递减到 $2$ 递归，将 $a_1$ 的处理留到 `now == 2` 时枚举 $a_2$ 并直接计算 $a_1$，避免再递归一层。使用 `vector<vector<int>>` 存储方案，最后用 lambda 按字典序排序并输出。该版本正确且高效。

## E
https://atcoder.jp/contests/abc473/tasks/abc473_e

> 给定一个长度为 $n$ 的整数序列 $a_1, a_2, \dots, a_n$ 和一个整数 $k$。将这个序列分成若干段，得分为**和能被 $k$ 整除的段的数量**，求最大得分。

**输入**

输入格式如下：
```
n k
a_1 a_2 ... a_n
```

**数据范围**

- $1 \le n \le 2 \times 10^5$
- $1 \le k \le 10^9$

**输出**

输出一个整数，表示最大得分。

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    unordered_map<int, int> best_mod;
    best_mod[0] = 0;          
    int best_all = 0;         
    int pref = 0;             
    int dp = 0;               
    for (int i = 0; i < N; ++i) {
        pref = (pref + A[i]) % K;
        dp = best_all;
        auto it = best_mod.find(pref);
        if (it != best_mod.end()) dp = max(dp, it->second + 1);
        if (dp > best_mod[pref]) best_mod[pref] = dp;
        if (dp > best_all) best_all = dp;
    }
    cout << dp << '\n';
    return 0;
}
```
/*
令前缀和 $pref_i = (\sum_{j=1}^{i} a_j) \bmod k$。一个区间 $[l, r]$ 的和能被 $k$ 整除，当且仅当 $pref_r = pref_{l-1}$。设 $dp_i$ 为前 $i$ 个数能获得的最大得分，转移为 $dp_i = \max(dp_{i-1}, dp_j + 1)$，其中 $pref_i = pref_j$。用哈希表维护每个前缀和值对应的最大 $dp$ 值，即可 $O(n)$ 完成转移。
*/

## F
https://atcoder.jp/contests/abc473/tasks/abc473_f

> 给定一个由 `A` 和 `B` 组成的字符串，支持两种操作：
> - 单点修改：将某个位置的字符改为 `A` 或 `B`
> - 区间查询：查询某个子串是否能由空串通过若干次**插入 `A`** 或**插入 `AB`** 操作得到
>
> 每次查询输出 `Yes` 或 `No`。

**输入**

第一行输入一个整数 $n$ 和字符串 $s$（长度为 $n$）。
第二行输入一个整数 $q$。
接下来 $q$ 行，每行一个操作：
- `1 x c`：将第 $x$ 个字符修改为 $c$（$c$ 为 `A` 或 `B`）
- `2 l r`：查询子串 $s[l..r]$ 是否合法

**数据范围**

- $1 \le n \le 10^5$
- $1 \le q \le 10^5$

**输出**

对于每个查询操作，输出一行 `Yes` 或 `No`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5;
#define ll long long 
int n,t;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    return 0;
}
```
/*
将 `A` 视为 $+1$，`B` 视为 $-1$。一个字符串能由空串通过插入 `A` 或 `AB` 得到，当且仅当该字符串的**任意前缀**中 `A` 的数量不少于 `B` 的数量。
用线段树维护区间加和区间最小值。查询时计算子串 $[l, r]$ 的前缀和最小值减去 $l-1$ 处的前缀和，若结果非负则合法。
*/

## G

这集我看过，卷积多项式（呜呜但是从来没写出来过）

https://atcoder.jp/contests/abc473/tasks/abc473_g

> 有 $n$ 张牌，数字分别为 $1, 2, \dots, n$，初始时全部正面朝下，数字未知。每次可以选择翻开一张牌。如果当前翻开的牌**小于所有已翻开的牌中的最小值**（即比当前所有已翻开的牌都小），则可以立即拿走这张牌。特别地，第一张翻开的牌可以直接拿走。求在**最优策略**下，恰好使用 $k$ 步翻完所有牌的概率。

**输入**

输入格式如下：
```
n k
```

**数据范围**

- $1 \le n \le 2 \times 10^5$

**输出**

输出一个整数表示概率（通常对 $998244353$ 取模）。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;

int main(){
    
    return 0;
}
```
/*
最优策略：如果当前翻开的牌符合条件（比所有已翻开的牌都小），则立即拿走；否则记住这个位置，等以后符合条件时再拿。每张牌最多贡献两次操作次数（一次翻开，一次拿走）。

操作数一定在 $[n, 2n-1]$ 之间。设当前还有 $s$ 张牌未知，下一次操作时，有 $1/s$ 的概率操作数不变（翻到了当前最小的牌，可以直接拿走），有 $(s-1)/s$ 的概率操作数 $+1$（翻到的不是最小牌，需要记住）。

问题转化为：从 $i=n$ 到 $2$，每次以 $1/i$ 的概率选择“不变”，以 $(i-1)/i$ 的概率选择“$+1$”，求恰好有 $k-n$ 次“$+1$”的概率。答案为：
$$\sum_{\text{count}(g)=k-n} \prod_{i=2}^{n} h(i, g_i)$$
其中 $h(i,0)=1/i$，$h(i,1)=(i-1)/i$。

可以通过生成函数或 NTT 优化计算。
*/