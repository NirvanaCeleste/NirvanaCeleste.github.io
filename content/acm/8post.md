---
title: "JPRS Programming Contest 2026#2 (AtCoder Beginner Contest 470)"
date: 2026-08-08
draft: false
comments: true
---
![ABC470提交记录](/img/acm/ABC470_submit.png)
![ABC470](/img/acm/ABC470.png)
## A
https://atcoder.jp/contests/abc470/tasks/abc470_a

> 给定一个正整数 $N$。对于 $i = 1, 2, \dots, N$，如果 $i$ 是 $3$ 的倍数，则输出 `Fizz`，否则输出 $i$。

**输入**

输入格式如下：
```
N
```


**输出**

输出 $N$ 行答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int n;

int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        if(i % 3 == 0) cout<<"Fizz"<<endl;
        else cout<<i<<endl;
    }

    return 0;
}
```
/*
直接按题意模拟即可：遍历 1 到 N，用取模判断是否为 3 的倍数。
*/

## B
https://atcoder.jp/contests/abc470/tasks/abc470_b

> 有 $N$ 个球，第 $i$ 个球的颜色为 $C_i$。每次操作可以将任意一个球改成任意颜色。求使所有球颜色相同所需的最少操作次数。

**输入**

输入格式如下：
```
N
C_1 C_2 ... C_N
```


**输出**

输出最少操作次数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int n,c;
int tot[maxn];

int main(){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>c,tot[c]++;
    int ans = INT_MIN;
    for(int i=1;i<=n;i++) ans = max(ans,tot[i]);
    ans = n - ans;
    cout<<ans;

    return 0;
}
```
/*
最优策略是保留出现次数最多的颜色，把其他颜色的球都改成这个颜色。
答案即为 N 减去出现次数最多的颜色的出现次数。
*/

## C
https://atcoder.jp/contests/abc470/tasks/abc470_c

这一道题卡太久了 赛时还没调出来

> 有一个长度为 $N$ 的整数序列 $A=(A_1,A_2,\ldots,A_N)$，初始时所有元素均为 $0$。按顺序处理 $Q$ 个查询，查询有两种类型：
> - `1 x`：将 $A_x$ 的值增加 $1$。
> - `2`：对于所有 $i=1,2,\ldots,N$，如果 $A_i \ge 1$，则将 $A_i$ 的值减少 $1$。
>
> 每次查询处理后，输出 $A_1, A_2, \dots, A_N$ 的按位异或（bitwise XOR）值。

**输入**

输入格式如下：
```
N Q
query_1
query_2
...
query_Q
```
其中每个查询为以下两种格式之一：
```
1 x
2
```


**数据范围**

- $1 \le N \le 5 \times 10^5$
- $1 \le Q \le 5 \times 10^5$
- $1 \le x \le N$


**输出**

输出 $Q$ 行，第 $i$ 行为第 $i$ 个查询处理后的 XOR 值。

```cpp
#include <bits/stdc++.h>
using namespace std;
int n,q,x,opt;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve2();
    return 0;
}
//unordered_map < int , long long > cnt;
//priority_queue < long long, vector<long long>, greater<long long> > heap;
//void solve2() {
//    cin >> n >> q;
//    long long shift = 0;
//    while (q--) {
//        int op;
//        cin >> op;
//        if (op == 1) {
//            int x;
//            cin >> x;
//            cnt[x]++;
//            heap.push(cnt[x]);
//        } else {
//            shift++;
//            // 清空所有已经失效的数
//            while (!heap.empty() && heap.top() <= shift) {
//                heap.pop();
//            }
//        }
//        // 每次直接遍历哈希表算总异或
//        long long xor_sum = 0;
//        for (auto &p : cnt) {
//            long long val = p.second - shift;
//            if (val > 0) {
//                xor_sum ^= val;
//            }
//        }
//        cout << xor_sum << '\n';
//    }
//}
//const int maxn = 500010;
//int add[maxn];
//int decr[maxn];
//void solve1(){
//  struct node{
//      int cnt,a;
//  };
//  struct cmp {
//      bool operator()(const node &x, const node &y) {
//          // 小根堆
//          return x.a > y.a;
//      }
//  };
//  priority_queue<node, vector<node>, cmp> d;
//  bool check[maxn];
//  vector<node> temp;
//  int j=0;
//  node tmp;
//  tmp.a = 0;
//  tmp.cnt = 0;
//  cin>>n>>q;
//  for(int i=1;i<=q;i++){
//      cin>>opt;
//      if(opt == 1){
//          cin>>x;
//          add[i] = x;
//      }
//      if(opt == 2) decr[i]++;
//      decr[i] += decr[i-1];
//  }
//  for(int i=1;i<=q;i++){
//      if(!add[i]) continue;
//      while(!d.empty()){
//          if(d.top().a > decr[i] - decr[j]) break;
//          check[d.top().a] = 0;
//          d.pop();
//      }
//      //?????
//      while(!d.empty()){
//          temp.push_back(d.top());
//          temp.back().a -= decr[i] - decr[j];
//          d.pop();
//      }
//      while(!temp.empty()){
//          if(temp.back().cnt = add[i]) temp.back().a += 1;
//          d.push(temp.back());
//          temp.pop_back();
//      }
//      //?????
//      j = i;
//      if(!check[add[i]]){
//          tmp.cnt = add[i];
//          tmp.a = 1;
//          d.push(tmp);
//          check[add[i]] = 1;
//      }
//  }
//  int ans = 0;
//  while(!d.empty()){
//      ans ^= d.top().a;
//      d.pop();
//  }
//  cout<<ans;
//}
```
/*
维护一个集合记录所有 A_i >= 1 的下标。操作 1 将 A_x 加 1，若此前为 0 则加入集合；
操作 2 遍历集合中的所有元素减 1，若变为 0 则移出集合。
同时维护当前异或和，单点修改时用 X xor A_x xor (A_x+1) 差分更新。
*/

## D
https://atcoder.jp/contests/abc470/tasks/abc470_d

> 给定一个 $(1, \dots, N)$ 的排列 $P = (P_1, \dots, P_N)$。按顺序处理 $Q$ 个查询，查询有两种类型：
> - `1 x y`：交换 $P_x$ 和 $P_y$ 的值。
> - `2`：构造排列 $P'$，使得对于所有 $i$，都有 $P_{P'_i} = i$（即 $P'$ 是 $P$ 的逆排列），然后将 $P$ 替换为 $P'$。

**输入**

输入格式如下：
```
N Q
P_1 P_2 ... P_N
query_1
query_2
...
query_Q
```


**数据范围**

- $2 \le N \le 5 \times 10^5$
- $2 \le Q \le 5 \times 10^5$


**输出**

处理完所有查询后，输出 $P_1, P_2, \dots, P_N$。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 500010;
int n, q;
int P[maxn],Q[maxn];   // Q 始终是 P 的逆 当前排列可能是 P 或 Q
bool rev = false;      // false: 当前排列为 P, true: 当前排列为 Q
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>q;
    for(int i=1;i<=n;i++) cin >> P[i];
    for(int i=1;i<=n;i++) Q[P[i]] = i;
    while(q--){
        int type;
        cin>>type;
        if(type == 1){
            int x,y;
            cin>>x>>y;
            if(!rev){
                int a = P[x], b = P[y];
                swap(P[x], P[y]);
                Q[a] = y;
                Q[b] = x;
            }else{
                int a = Q[x], b = Q[y];
                swap(Q[x], Q[y]);
                P[a] = y;
                P[b] = x;
            }
        }
        else rev = !rev;
    }
    if (!rev) for(int i=1;i<=n;i++) cout<<P[i]<<' ';
    else for (int i=1;i<=n;i++) cout<<Q[i]<<' ';
    return 0;
}
```
/*
同时维护排列 P 和它的逆排列 Q。
操作 1 交换 P_x 和 P_y，同时更新 Q 中对应位置的映射。
操作 2 将 P 替换为其逆排列，等价于交换 P 和 Q，用 rev 标记当前使用的是哪一个。
*/

## E
https://atcoder.jp/contests/abc470/tasks/abc470_e

> 有 $2N$ 张牌，每张牌上写着一个数字。数字 $1$ 到 $N$ 各出现恰好两次。所有牌随机打乱后正面朝下放置。
> 你有 $L$ 条命。每次操作你翻开一张牌。如果你翻开的牌与之前某张已翻开但未配对的牌数字相同，则配对成功，这两张牌移出游戏。否则这张牌保持翻开状态（你知道它的数字和位置）。
> 求在最优策略下，成功配对的期望对数。

**输入**

第一行包含两个整数 $N$ 和 $L$（$1 \le N \le 200$，$1 \le L \le N$）。

**输出**

输出期望配对数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;


int main(){


    return 0;
}
```
/*
概率 DP。状态 f[i][j][k] 表示剩余 i 条命，已经配对了 j 对，已经知道但未配对的牌有 k 张的期望得分。
按最优策略转移：优先翻开已知配对的牌；否则随机翻开一张新牌，若与已知牌匹配则配对，否则再翻一张。
*/

## F
https://atcoder.jp/contests/abc470/tasks/abc470_f

> 给定一个长度为 $N$ 的字符串 $S$，由小写英文字母组成。
> 有 $M$ 种交换操作，第 $i$ 种操作可以交换 $S$ 中位置 $A_i$ 和 $B_i$ 的字符。
> 你可以按任意顺序执行这些操作任意多次（每种操作可使用任意次），但总操作次数必须恰好为 $10^{100}$（一个极大的偶数）。
> 求最终可能得到的不同字符串的数量，答案对 $998244353$ 取模。

**输入**

第一行包含两个整数 $N$ 和 $M$。
第二行包含字符串 $S$。
接下来 $M$ 行，每行两个整数 $A_i$ 和 $B_i$。

**输出**

输出可能得到的不同字符串数量对 $998244353$ 取模的结果。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 500010;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    return 0;
}
```
/*
将 N 个位置看作图的 N 个节点，M 种交换操作看作无向边。
同一个连通块内的位置可以任意交换排列。
由于操作次数必须是偶数 $10^{100}$，若某个连通块大小 > 1，偶数次操作可以实现任意排列。
对每个连通块统计各字母出现次数，用组合数计算方案数。
*/

## G
https://atcoder.jp/contests/abc470/tasks/abc470_g

> 给定一个长度为 $N$ 的非负整数序列 $A = (A_1, A_2, \dots, A_N)$。
> 求所有子数组的 mex 之和：
> $$\sum_{l=1}^{N} \sum_{r=l}^{N} \text{mex}(A_l, \dots, A_r)$$
> 其中 $\text{mex}$ 表示未在子数组中出现的最小非负整数。

**输入**

第一行包含一个整数 $N$（$1 \le N \le 3 \times 10^5$）。
第二行包含 $N$ 个整数 $A_1, A_2, \dots, A_N$（$0 \le A_i \le N$）。

**输出**

输出所有子数组的 mex 之和。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;


int main(){


    return 0;
}
```
/*
换角度思考：对于每个 k，统计有多少个子数组包含 0~k 的所有元素。
固定右端点 r，维护 lst[x] 表示数字 x 在 [1,r] 中最后一次出现的位置。
包含 0~k 的子数组数量为 $\sum_{r=1}^{N} \min_{0 \le x \le k} lst_r[x]$。
用线段树维护区间最小值，从 k=0 到 N 递推计算。
```