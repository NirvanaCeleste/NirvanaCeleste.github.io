---
title: "AtCoder Beginner Contest 468"
date: 2026-07-25
draft: false
comments: true
---
![ABC468提交记录](/img/acm/ABC468_submit.png)
![ABC468](/img/acm/ABC468.png)
## A
https://atcoder.jp/contests/abc468/tasks/abc468_a

> 给定一个长度为 $N$ 的整数序列 $A=(A_1, A_2, \ldots, A_N)$。求满足 $A_i < A_{i+1} > A_{i+2}$ 的整数 $i$（$1 \le i \le N-2$）的个数。

**输入**

第一行包含一个整数 $N$（$3 \le N \le 100$）。
第二行包含 $N$ 个整数 $A_1, A_2, \ldots, A_N$（$1 \le A_i \le 10^9$）。

**输出**

输出满足条件的 $i$ 的个数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int n,ans;
int a[maxn];

int main(){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n-2;i++) if(a[i] < a[i+1] && a[i+1] > a[i+2]) ans++;
    cout<<ans;

    return 0;
}
```
/*
遍历每个连续三元组，检查是否为“峰”形结构（中间元素严格大于左右两边）。
*/

## B
https://atcoder.jp/contests/abc468/tasks/abc468_b

> 给定整数 $M, D$ 和一个长度为 $M$、由 `G` 和 `.` 组成的字符串 $S$。
> 有 $M$ 个格子排成一排，从左到右编号为 $1$ 到 $M$。如果 $S_i$ 为 `G`，则第 $i$ 个格子上站着守卫；如果 $S_i$ 为 `.`，则没有人。
> 与有守卫的格子的距离不超过 $D$ 的格子会被该守卫监视。也就是说，如果存在某个格子 $i$ 满足 $S_i =$ `G` 且 $|x - i| \le D$，则格子 $x$ 被守卫监视。
> 求 $M$ 个格子中未被监视的格子数量。

**输入**

第一行包含两个整数 $M$ 和 $D$（$1 \le M \le 100$，$0 \le D \le 100$）。
第二行包含一个长度为 $M$ 的字符串 $S$，由 `G` 和 `.` 组成。

**输出**

输出未被监视的格子数量。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
int m,d,ans;
string s;
bool h[maxn];

int main(){
    cin>>m>>d;
    cin>>s;
    for(int i=0;i<m;i++){
        if(s[i] == 'G'){
            for(int j=i-d;j<=i+d;j++){
                if(j<0 || j>=m) continue;
                h[j] = 1;
            }
        }
    }
    for(int i=0;i<m;i++) if(!h[i]) ans++;
    cout<<ans;
    return 0;
}
```
/*
对每个守卫，标记其监视范围内的所有格子，最后统计未被标记的格子数。
*/

## C
https://atcoder.jp/contests/abc468/tasks/abc468_c

> 给定整数 $N$ 和两个排列 $P=(P_1,P_2,\ldots,P_N)$、$Q=(Q_1,Q_2,\ldots,Q_N)$，它们都是 $(1,2,\ldots,N)$ 的排列。
> 求满足以下条件的整数序列的数量：该序列是 $(1,2,\ldots,N)$ 的一个排列，且字典序严格大于 $P$、严格小于 $Q$。

**输入**

第一行包含一个整数 $N$（$1 \le N \le 10$）。
第二行包含 $N$ 个整数 $P_1, P_2, \ldots, P_N$。
第三行包含 $N$ 个整数 $Q_1, Q_2, \ldots, Q_N$。

**输出**

输出满足条件的排列数量。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 12;
int n,ans;
int p[maxn],q[maxn],tmp[maxn];
string a="",b="",c="";

bool check(){
    if(a<c&&c<b) return 1;
    return 0;
}

int main(){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>p[i],a+='0'+p[i];
    for(int i=1;i<=n;i++) cin>>q[i],b+='0'+q[i];
    for(int i=1;i<=n;i++) tmp[i] = i;
    if (a >= b) {
        cout<<0;
        return 0;
    }
    do{
        c = "";
        for (int i = 1; i <= n; i++) c+='0'+tmp[i];
        if (check()) ans++;
    } while (next_permutation(tmp + 1, tmp + n + 1));
    cout<<ans;

    return 0;
}
```
/*
利用 next_permutation 枚举所有排列，将排列转为字符串后直接比较字典序。
*/

## D
https://atcoder.jp/contests/abc468/tasks/abc468_d

> 由小写英文字母组成的字符串被称为好字符串，当且仅当它可以通过修改最多一个字符变成回文串。
> 给定一个字符串 $S$，求其所有子串中好字符串的个数。

**输入**

输入一行包含一个字符串 $S$（$1 \le |S| \le 10^4$），由小写英文字母组成。

**输出**

输出好子串的个数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 10010;
int n;
string s;
long long ans;

void check(){
//  long long dp[maxn];
//  deque<char> q;
//  dp[0] = 1;
//  for(int i=1;i<n;i++){
//      dp[i] += dp[i-1];
//      for(int len=1;len++;len<=i){
//          if(len == 1 || len == 2) dp[i]++;
//          else if(len%2==0)
//          else if(len%2==1)
//      }
//      q.clear();
//      for(int j=i;j>=0;j--){
//          if(q.empty)
//      }
//  }
//  cout<<dp[n-1];
}

int main(){
    cin>>s;
    n = s.length();
    int l=0,r=0;
//  ans += n;
//  ans += 2*n-1;
    int diff = 0;
    for(int i=0;i<n;i++){
        l = i,r = i;
        diff = 0;
        while(l>=0 && r<n && diff<=1){
            if(l<0 || r>=n) break;
            if(s[l] != s[r]) diff++;
            if(diff>1) break;
            l--,r++;
            ans++;
        }
    }
    for(int i=2;i<=2*n-2;i+=2){
        l = (i-2)/2,r = i/2;
        diff = 0;
        while(l>=0 && r<n && diff<=1){
            if(l<0 || r>=n) break;
            if(s[l] != s[r]) diff++;
            if(diff>1) break;
            l--,r++;
            ans++;
        }
    }
    cout<<ans;
    return 0;
}
```
/*
分别枚举奇数长度和偶数长度的子串，从中心向两端扩展，统计字符不同的次数不超过 1 的子串数量。
*/

## E
https://atcoder.jp/contests/abc468/tasks/abc468_e

> 给定一个正整数 $N$ 和一个长度为 $N$ 的整数序列 $A=(A_1,A_2,\ldots,A_N)$。
> 定义 $f(l,r)$ 为序列 $A$ 中下标 $[l,r]$ 的算术平均值，即 $f(l,r)=\frac{\sum_{i=l}^{r} A_i}{r-l+1}$。
> 求 $\sum_{1 \le l \le r \le N} f(l,r)$ 对 $998244353$ 取模后的值。

**输入**

第一行包含一个整数 $N$（$1 \le N \le 5 \times 10^5$）。
第二行包含 $N$ 个整数 $A_1, A_2, \ldots, A_N$（$1 \le A_i \le 10^9$）。

**输出**

输出所求值对 $998244353$ 取模后的结果。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 500500;
int n;
int p[maxn];
//int dp[maxn];
//int len[maxn];
int x,y,ans;
//struct node{
//  int p,cnt;
//}a[maxn];
//bool cmp(const node &a,const node &b){
//  return a.p < b.p;
//}
void solve(){
    //  dp[1] = 1;
//  for(int i=2;i<=n;i++){
//      if(dp[i] > dp[i-1]) dp[i] = dp[i-1] + 1;
//      else dp[i] = 1
//  }
//  ans++;
//  x = p[1];
}
void solve2(){
//  for(int i=1;i<=n;i++) cin>>a[i].p,a[i].cnt = i;
//  sort(a+1,a+1+n,cmp);
//  for(int i=1;i<=n;i++){
//
//
//  }
//  ans += len[1];
//  int tmp = 0;
//  for(int i=2;i<=n;i++) tmp = max(tmp,len[i]);
//  ans += tmp;

}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++) cin>>p[i];
    for(int i=1;i<=n;i++){
        if (x > y) swap(x, y);
        if(p[i] > y) {          // 比两个都大，只能得分，且放到较大的容器上
            y = p[i];
            ++ans;
        }
        else if(p[i] > x) {   // 介于两者之间，只能放到较小容器上，得分
            x = p[i];
            ++ans;
        }
        // 否则 p <= x，放到哪个容器都不得分，且最大值不变
    }
    cout<<ans+1;

    return 0;
}
```
/*
（算法思路略，代码由用户提供）
*/

## F
https://atcoder.jp/contests/abc468/tasks/abc468_f

> 给定一个正整数 $N$ 和一个排列 $P=(P_1,P_2,\ldots,P_N)$，它是 $(1,2,\ldots,N)$ 的一个排列。
> 求通过以下操作能获得的最大得分：
> - 维护两个变量 $x$ 和 $y$，初始为 $0$。
> - 按顺序遍历 $P$ 中的每个元素，每次可以选择放入 $x$ 或 $y$。
> - 如果放入后该变量变大，则得 $1$ 分。
> 求最大得分。

**输入**

第一行包含一个整数 $N$（$1 \le N \le 5 \times 10^5$）。
第二行包含 $N$ 个整数 $P_1, P_2, \ldots, P_N$，是 $(1,2,\ldots,N)$ 的一个排列。

**输出**

输出最大得分。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200020;


int main(){


    return 0;
}
```
/*
（算法思路略，代码由用户提供）
*/

## G
https://atcoder.jp/contests/abc468/tasks/abc468_g

> 给定一个长度为 $n$ 的字符串 $s$，由 `o` 和 `x` 组成。
> 求满足以下条件的排列 $1,2,\ldots,n$ 的数量：
> - 对于每个 $i$（$1 \le i \le n$），前缀 $1,2,\ldots,i$ 在排列中形成的连续段数量满足：
>   - 如果 $s_i =$ `o`，则连续段数量必须为 $1$；
>   - 如果 $s_i =$ `x`，则连续段数量不能为 $1$。

**输入**

第一行包含一个整数 $n$（$1 \le n \le 2000$）。
第二行包含一个长度为 $n$ 的字符串 $s$，由 `o` 和 `x` 组成。

**输出**

输出满足条件的排列数量对 $998244353$ 取模后的结果。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200020;


int main(){


    return 0;
}
```
