---
title: "AtCoder Beginner Contest 471"
date: 2026-08-15
draft: false
comments: true
---

![ABC471提交记录](/img/acm/ABC471_submit.png)
![ABC471](/img/acm/ABC471.png)
目前打的最爽的一场，感觉发挥的非常好

## A
https://atcoder.jp/contests/abc471/tasks/abc471_a

> 给定两个正整数 $A$ 和 $B$。如果以下值中至少有一个等于 $9$，请输出 `Nine`；否则，请输出 `Nein`：
> - $A + B$
> - $A - B$
> - $A \times B$
> - $A \div B$

**输入**

输入格式如下：
```
A B
```

**数据范围**

- $1 \le A \le 100$
- $1 \le B \le 100$

**输出**

如果四种运算结果中至少有一个等于 $9$，输出 `Nine`；否则输出 `Nein`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int a,b;

int main(){
    cin>>a>>b;
    if(a-b == 9 || a+b == 9 || a*b == 9 || a/b == 9) cout<<"Nine";
    else cout<<"Nein";
    return 0;
}
```
/*
分别检查四种运算结果是否等于 9。注意除法 $A \div B = 9$ 等价于 $A = 9B$。
*/

## B
https://atcoder.jp/contests/abc471/tasks/abc471_b

> 高桥正在统计一项调查的结果。共有 $N$ 人参与了调查，第 $i$ 个人的回答是一个由英文字母组成的字符串 $S_i$。
> 请找出本次调查中，给出**相同回答的最多人数**。回答中的字母**不区分大小写**。例如，`AtCoder`、`ATCODER` 和 `atcoder` 均被视为相同的回答。

**输入**

输入格式如下：
```
N
S_1
S_2
...
S_N
```

**数据范围**

- $1 \le N \le 100$
- $S_i$ 仅包含大小写英文字母，且长度不超过 $10$

**输出**

输出给出相同回答的最多人数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int n,ans;
string s;
map<string,int> q;

int main(){
    cin>>n;
    q["123"]++;
    while(n--){
        cin>>s;
        int len = s.length();
        for(int i=0;i<len;i++) if(s[i] >= 'A' && s[i] <= 'Z') s[i] = (s[i] - 'A') + 'a';
        q[s]++;
    }
    for(auto it = q.begin();it != q.end();++it) ans = max(ans,it->second);
    cout<<ans;

    return 0;
}
```
/*
将所有字符串统一转为小写（或大写），用 map 统计每种字符串的出现次数，取最大值即可。
*/

## C
https://atcoder.jp/contests/abc471/tasks/abc471_c

> 在数轴上有 $N$ 个位置放有饼干，第 $i$ 块饼干的坐标为 $A_i$。
> 高桥最初位于坐标 $0$ 处，他将重复执行以下动作，直到捡起所有的 $N$ 块饼干：
> - 动作：移动到距离当前位置**最近**的饼干所在的坐标（如果存在多块这样的饼干，则选择坐标**最小**的那一块），并捡起该饼干。
>
> 请计算高桥在捡起所有饼干的过程中所移动的**总距离**。

**输入**

输入格式如下：
```
N
A_1 A_2 ... A_N
```

**数据范围**

- $1 \le N \le 3 \times 10^5$
- $-10^9 \le A_i \le 10^9$
- $A_i \ne 0$ 且 $A_i$ 互不相同

**输出**

输出高桥移动的总距离。

```cpp
//#include <bits/stdc++.h>
//using namespace std;
//const int maxn = 300030;
//int n,now;
//long long ans;
//int a[maxn],aleft[maxn],aright[maxn];
//
//int lfind(int x){
//  if(aleft[x] != x) aleft[x] = lfind(aleft[x]);
//  return aleft[x];
//}
//int rfind(int x){
//  if(x == n + 1) return n + 1;
//  if(aright[x] != x) aright[x] = rfind(aright[x]);
//  return aright[x];
//}
//
////int main(){
//  scanf("%d",&n);
//  for(int i=1;i<=n;i++) scanf("%d",&a[i]),aleft[i] = i,aright[i] = i;
//  aright[n+1] = n+1;
//  sort(a+1,a+1+n);
//  if(upper_bound(a+1,a+1+n,0) - a == n+1) ans -= a[1];
//  else if(upper_bound(a+1,a+1+n,0) - a == 1) ans = a[n];
//  else{
//      ans = 0;
//      int l = upper_bound(a+1,a+1+n,0) - a - 1,r = upper_bound(a+1,a+1+n,0) - a;
//      if(0 <= a[r] + a[l]) now = l,ans += -1*a[l];
//      else now = r,ans += a[r];
//      int cnt = 1;
//      while(cnt < n){//注意还要更新边界的左右边界
//          cnt++;
//          int l = lfind(now-1),r = rfind(now+1),tmp = now;
//          if(l == 0) aleft[r] = l,aright[now] = r,now = r;
//          else if(r == n+1) aright[l] = r,aleft[now] = l,now = l;
//          else{
//              if(a[now] - a[l] <= a[r] - a[now]) aright[l] = r,aleft[now] = l,now = l;
//              else aleft[r] = l,aright[now] = r,now = r;
//          }
//          ans += tmp >= now ? a[tmp] - a[now] : a[now] - a[tmp];
//          cout<<cnt<<' '<<ans<<' '<<now<<endl;
//      }
//  }
//  for(int i=1;i<=n;i++) cout<<aleft[i]<<' ';
//  cout<<endl;
//  for(int i=1;i<=n;i++) cout<<aright[i]<<' ';
//  cout<<endl;
//  printf("%lld",ans);
//
//  return 0;
//}
#include <bits/stdc++.h>
using namespace std;
const int maxn = 300030;
int n,now;
long long ans;
int a[maxn],aleft[maxn],aright[maxn];

int lfind(int x){
    if(x == 0) return 0;                     // 添加边界
    if(aleft[x] != x) aleft[x] = lfind(aleft[x]);
    return aleft[x];
}
int rfind(int x){
    if(x == n + 1) return n + 1;
    if(aright[x] != x) aright[x] = rfind(aright[x]);
    return aright[x];
}

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]),aleft[i] = i,aright[i] = i;
    aleft[0] = 0;                            // 添加哨兵
    aright[n+1] = n+1;
    sort(a+1,a+1+n);

    int pos0 = upper_bound(a+1,a+1+n,0) - a; // 第一个 > 0 的位置
    if(pos0 == n+1){                         // 全负
        ans = -1LL * a[1];
        printf("%lld\n",ans);
        return 0;
    }
    else if(pos0 == 1){                      // 全正
        ans = 1LL * a[n];
        printf("%lld\n",ans);
        return 0;
    }
    else{
        ans = 0;
        int l = pos0 - 1;   // 最后一个负数
        int r = pos0;       // 第一个正数
        if(0 <= a[r] + a[l]) now = l, ans += -1*a[l];
        else now = r, ans += a[r];

        int cnt = 1;
        while(cnt < n){
            cnt++;
            int L = lfind(now-1);
            int R = rfind(now+1);
            int tmp = now;
            int nxt; // 下一步要去的位置

            // 决定目标
            if(L == 0) nxt = R;
            else if(R == n+1) nxt = L;
            else{
                if(a[tmp] - a[L] <= a[R] - a[tmp]) nxt = L;
                else nxt = R;
            }

            // 累加距离（用 tmp 和 nxt 比较）
            ans += tmp >= nxt ? a[tmp] - a[nxt] : a[nxt] - a[tmp];

            // 删除旧点 tmp（关键：双向都更新）
            aleft[tmp] = L;
            aright[tmp] = R;
            if(L != 0) aright[L] = R;
            if(R != n+1) aleft[R] = L;

            now = nxt;
            // cout<<cnt<<' '<<ans<<' '<<now<<endl; // 调试可删
        }
    }
    // 调试输出可删
    // for(int i=1;i<=n;i++) cout<<aleft[i]<<' ';
    // cout<<endl;
    // for(int i=1;i<=n;i++) cout<<aright[i]<<' ';
    // cout<<endl;
    printf("%lld",ans);
    return 0;
}
```
/*
将饼干按坐标排序。高桥每次选择距离当前位置最近的饼干，这等价于在已排序的正负两侧各维护一个指针，每次选择距离更近的那一侧。
代码中利用并查集思想维护每个位置左右两侧未捡起的最近的饼干，模拟整个过程。
*/

## D
https://atcoder.jp/contests/abc471/tasks/abc471_d

> 有 $Q$ 个事件，有两种类型：
> - `1 t w`：在时刻 $t$ 放入一个电量上限为 $w$ 的电池（若 $w \ge V$ 则视为满电电池）。
> - `2 t`：在时刻 $t$ 取出一个电池，要求取出当前电量**最大**的电池。
>
> 不考虑电池容量上限 $V$ 时，若一个电池在时刻 $t$ 开始充电，到时刻 $w$ 时的电量为 $w - t$。
> 考虑容量上限 $V$ 时，实际电量为 $\min(w - t, V)$。
> 每次操作 `2` 时，输出取出的电池的电量；若没有电池可取，输出 $-1$。

**输入**

第一行包含两个整数 $Q$ 和 $V$。
接下来 $Q$ 行，每行一个事件。

**数据范围**

未在公开题解中明确给出，参考同类题目估计：
- $1 \le Q \le 2 \times 10^5$
- $1 \le V \le 10^9$

**输出**

对于每个类型 `2` 的事件，输出取出的电池电量；若没有电池可取，输出 $-1$。

```cpp
//#include <bits/stdc++.h>
//using namespace std;
//const int maxn = 300030;
//long long q, v, tmp;
//priority_queue<long long> pq;
//
//int main() {
//    scanf("%lld %lld",&q,&v);
//    long long cur_time = 0;   // 当前时间
//    bool full = 0;       // 满电
//    while(q--){
//        scanf("%lld",&tmp);
//        if(tmp == 1){
//            long long t,w;
//            scanf("%lld %lld",&t,&w);
//            cur_time = t;
//            if(w >= v) full = 1;
//            else pq.push(w - t);   /// 插入未满电池，key = w - t
//        }else{  // tmp == 2
//            long long t;
//            scanf("%lld",&t);
//            cur_time = t;
//            // 弹出所有已经充满的电池（移到 full 计数）
//            while(!pq.empty()){
//                long long top = pq.top();
//                if (cur_time + top >= v) {
//                    pq.pop();
//                    full = 1;
//                }
//                else break;
//            }
//            if(full){
//                printf("%lld\n",v);
//                full = 0;
//            }else if(!pq.empty()) {
//                long long top = pq.top();
//                pq.pop();
//                printf("%lld\n", cur_time + top);
//            }else{
//                printf("%d\n",-1);
//            }
//        }
//    }
//    return 0;
//}
#include <bits/stdc++.h>
using namespace std;
const int maxn = 300030;
long long q, v, tmp;
priority_queue<long long> pq;

int main() {
    scanf("%lld %lld",&q,&v);
    long long cur_time = 0;
    long long full = 0;       // 改为 long long，记录满电电池个数
    while(q--){
        scanf("%lld",&tmp);
        if(tmp == 1){
            long long t,w;
            scanf("%lld %lld",&t,&w);
            cur_time = t;
            if(w >= v) full++;        // 直接入满电计数
            else pq.push(w - t);
        }else{  // tmp == 2
            long long t;
            scanf("%lld",&t);
            cur_time = t;
            // 将堆中已充满的移到 full 计数
            while(!pq.empty()){
                long long top = pq.top();
                if (cur_time + top >= v) {
                    pq.pop();
                    full++;
                }
                else break;
            }
            if(full > 0) {
                printf("%lld\n", v);
                full--;
            } else if(!pq.empty()) {
                long long top = pq.top();
                pq.pop();
                printf("%lld\n", cur_time + top);
            } else {
                printf("-1\n");
            }
        }
    }
    return 0;
}
```
/*
维护一个大根堆存储未满电池的 `w - t` 值（即充满所需时长）。
每次操作 `2` 时，先将堆中已充满的电池弹出并计入满电计数，然后优先输出满电电池（电量为 V），否则输出堆顶电池的当前电量 `cur_time + top`。
*/

## E
https://atcoder.jp/contests/abc471/tasks/abc471_e

> 有一个由 $N$ 项组成的数列 $\langle A_1, A_2, \dots, A_N \rangle$。
> 从 $A$ 中选出**不同的** $K$ 项 $A_{I_1}, A_{I_2}, \dots, A_{I_K}$（$1 \le I_1 < I_2 < \dots < I_K \le N$），求所有选法中 $\left( \sum_{j=1}^{K} A_{I_j} \right)^2$ 的**总和**，对 $998244353$ 取模。

**输入**

输入格式如下：
```
N K
A_1 A_2 ... A_N
```

**数据范围**

- $1 \le K \le N \le 2 \times 10^5$
- $1 \le A_i \le 10^9$

**输出**

输出所有选法的和的平方的总和，对 $998244353$ 取模。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 998244353;

ll mod_pow(ll a, ll b) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    cin >> N >> K;
    vector<ll> A(N);
    ll S = 0, Q = 0;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        S = (S + A[i]) % MOD;
        Q = (Q + A[i] * A[i]) % MOD;
    }

    // 预处理阶乘和逆元
    vector<ll> fact(N + 1), inv_fact(N + 1);
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i-1] * i % MOD;
    inv_fact[N] = mod_pow(fact[N], MOD - 2);
    for (int i = N; i >= 1; i--) inv_fact[i-1] = inv_fact[i] * i % MOD;

    auto C = [&](int n, int k) -> ll {
        if (k < 0 || k > n) return 0;
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD;
    };

    ll ans = 0;
    ans = (ans + C(N - 1, K - 1) * Q) % MOD;
    ll diff = (S * S % MOD - Q + MOD) % MOD;
    ans = (ans + C(N - 2, K - 2) * diff) % MOD;

    cout << ans << '\n';
    return 0;
}
```
/*
利用公式 $(\sum a_i)^2 = \sum a_i^2 + 2\sum_{i<j} a_i a_j$。
若选定了一个数 $a_i$，则有 $C_{N-1}^{K-1}$ 种选法包含它。
若选定了一对数 $a_i, a_j$（$i<j$），则有 $C_{N-2}^{K-2}$ 种选法同时包含它们。
答案 = $C_{N-1}^{K-1} \cdot \sum a_i^2 + C_{N-2}^{K-2} \cdot \left( (\sum a_i)^2 - \sum a_i^2 \right)$。
注意第二项对应 $2\sum_{i<j} a_i a_j$，正好等于 $(\sum a_i)^2 - \sum a_i^2$。
*/

## F
https://atcoder.jp/contests/abc471/tasks/abc471_f

> 给定 $N$ 个数字字符串 $S_1, S_2, \dots, S_N$。从中**恰好选择 $K$ 个**，以**任意顺序拼接**，得到一个十进制整数（去除前导零后）。
> 求这个整数的**最大值**。

**输入**

输入格式如下：
```
N K
S_1
S_2
...
S_N
```

**数据范围**

- $1 \le K \le N \le 10^5$
- $S_i$ 的长度在 $1$ 到 $10$ 之间，由数字组成

**输出**

输出最大整数（去除前导零后）。

```cpp
//这个赛时没过 而且这个代码的逻辑其实是有很大错误的 没有分类讨论长度等
#include <bits/stdc++.h>
using namespace std;

bool cmp(const string& a, const string& b) {return a + b > b + a;} // 降序

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, K;
    cin >> N >> K;
    vector<string> S(N);
    for (int i = 0; i < N; i++) cin >> S[i];
    sort(S.begin(), S.end(), cmp);
    string ans;
    for (int i = 0; i < K; i++) ans += S[i];
    size_t pos = ans.find_first_not_of('0');// 去除前导零
    if (pos == string::npos) cout << "0\n";
    else cout << ans.substr(pos) << '\n';

    return 0;
}
```
/*
对于数字字符串的拼接最大化问题，排序规则为 $a+b > b+a$。
但由于字符串长度不超过 10，可能存在前导零的特殊情况，需要特殊处理。
*/



## G
https://atcoder.jp/contests/abc471/tasks/abc471_g

> 有 $K$ 种符号，编号 $0 \sim K-1$，每种符号是元音（$V_j=1$）或辅音（$V_j=0$）。定义符号串的音节数为该串中由元音组成的最大连续子串的个数。给定一个长度为 $N$ 的序列 $A$（实际通过伪随机生成器恢复），对于每个 $k=0,\dots,K-1$，将每个元素 $A_i$ 加 $k$ 后对 $K$ 取模得到新串，求新串的音节数。$N$ 最大 $7 \times 10^6$，$K \le 2300$。

**输入格式（特殊）**：给定 `N K seed M`，以及前 $M$ 个 $b_i$，其余元素通过伪随机生成。最后一行给出 $V_0 \dots V_{K-1}$。

**输出**：$K$ 行，每行一个整数表示对应 $k$ 的答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;

int main(){
    // 本题代码未提供，请自行实现
    return 0;
}
```

**思路提示**：
由于 $K$ 较小而 $N$ 很大，可以考虑对每个 $k$ 分别计算音节数。音节数等于“元音组”的数量，即统计相邻元素中从辅音变为元音（或开头第一个是元音）的次数。可以预处理原序列每个位置 $i$ 的符号是否为元音（随 $k$ 变化），然后用差分或前缀和快速统计每段的切换次数。具体做法：对每个 $k$，遍历 $i=1 \dots N$，判断 $A_i + k \mod K$ 是否为元音，并统计 `(前一个不是元音 && 当前是元音)` 的个数。由于 $K$ 最多 $2300$，$N$ 为 $7\times10^6$，直接对每个 $k$ 遍历 $N$ 会超时，需要优化，例如利用循环节或分块统计。
```