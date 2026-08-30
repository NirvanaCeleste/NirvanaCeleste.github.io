---
title: "AtCoder Beginner Contest 472"
date: 2026-08-22
draft: false
comments: true
---
![ABC472](/img/acm/ABC472.png)
![ABC472提交记录](/img/acm/ABC472_submit.png)
## A
https://atcoder.jp/contests/abc472/tasks/abc472_a

> 给定一个由大写字母组成的字符串 $S$。请输出将其中所有非 `A` 的字符替换为 `.` 后的字符串。

**输入**

输入一行字符串 $S$。

**数据范围**

- $|S| \le 100$（由代码中 `maxn = 102` 推断）

**输出**

输出替换后的字符串。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int len;
string s;

int main(){
    cin>>s;
    len = s.length();
    for(int i=0;i<len;i++){
        if(s[i] == 'A') cout<<'A';
        else cout<<'.';
    }
    return 0;
}
```
/*
遍历字符串，若字符为 'A' 则原样输出，否则输出 '.'。
*/

## B
https://atcoder.jp/contests/abc472/tasks/abc472_b

> 有 $N$ 个木板，第 $i$ 个木板的长度为 $l_i$。将所有这些木板首尾相连拼成一根长木棍，然后从某个位置（在两块木板之间）切断，使得切断后两段长度的差值的绝对值最小。求这个最小差值。

**输入**

输入格式如下：
```
N
l_1 l_2 ... l_N
```

**数据范围**

- $2 \le N \le 100$（由 `maxn = 102` 推断）
- $1 \le l_i \le 10^9$

**输出**

输出最小差值。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;
int n,ans = INT_MAX;
int l[maxn],s[maxn];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++) cin>>l[i],s[i] = s[i-1] + l[i];
    for(int i=2;i<=n;i++) ans = min(ans,abs((s[n] - s[i-1]) - (s[i-1])));
    cout<<ans;
    return 0;
}
```
/*
预处理前缀和。枚举分割点 i（即前 i-1 块为一段，其余为另一段），计算两段长度差的绝对值，取最小值。
*/

## C
https://atcoder.jp/contests/abc472/tasks/abc472_c

> 有 $N$ 个任务，第 $i$ 个任务需要消耗 $a_i$ 点体力。你有一个初始体力 $k$，按照顺序处理任务。对于每个任务，若当前剩余体力足够完成该任务，则完成它并消耗相应体力，输出 `Yes`；否则输出 `No` 且不消耗体力。同时，你有一个长度为 $M$ 的滑动窗口，当处理完第 $i$ 个任务后，如果窗口左端（第 $i-M+1$ 个任务）曾经被完成，则要恢复该任务消耗的体力（相当于将其移出窗口）。请输出每个任务的处理结果。

**输入**

输入格式如下：
```
N M K
a_1 a_2 ... a_N
```

**数据范围**

- $1 \le M \le N \le 2 \times 10^5$（由 `maxn = 200001` 推断）
- $1 \le K \le 10^9$
- $1 \le a_i \le 10^9$

**输出**

共 $N$ 行，每行一个 `Yes` 或 `No`。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200001;
int n,m;
long long k,now;
int a[maxn];
bool pd[maxn];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m>>k;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++){
        if(now + a[i] > k) cout<<"No"<<'\n';
        else{
            now += a[i];
            pd[i] = 1;
            cout<<"Yes"<<'\n';
        }
        if(i >= m && pd[i-m+1]) now -= a[i-m+1];
    }
}
```
/*
维护当前窗口内已选任务的总消耗 `now`。对于每个任务，若能加入（`now + a[i] <= k`）则标记并累加，否则不加入。然后若滑动窗口左端任务被选中，则将其消耗从 `now` 中减去（模拟滑出窗口）。注意先判断再更新窗口。
*/

## D

![灵魂画手](/img/acm/ABC472D.png)

https://atcoder.jp/contests/abc472/tasks/abc472_d

> 有一个 $H$ 行 $W$ 列的网格。某些格子是障碍物（`#`）。另外，如果某一行或某一列存在至少一个障碍物，则称该行或该列为“爆炸行/列”。从所有既不在爆炸行也不在爆炸列的格子出发，每次可以上下左右移动一格，但不能经过障碍物，且步数不能超过 $K$。求所有可达的格子总数（包括起点）。注意：多个起点可能到达同一格子，只需计数一次。

被D题单防了 T_T 
想的太复杂了 一直在想用堆坐标加二分查找来简化曼哈顿距离 最后力竭了写了个bfs还错了 T_T
**输入**

输入格式如下：
```
H W K
S_1
S_2
...
S_H
```
其中 $S_i$ 是长度为 $W$ 的字符串，仅包含 `.` 和 `#`。

**数据范围**

- $1 \le H, W \le 700$（由 `maxn = 5e5+1` 且 `H*W ≤ maxn` 推断，实际未给出明确上限）
- $0 \le K \le 10^9$

**输出**

输出可达格子总数。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 5e5+1;
int h,w,k,ans;
bool vis[maxn],boomx[maxn],boomy[maxn];
int bfsvis[maxn];
int dx[4] = {0,1,0,-1},dy[4] = {1,0,-1,0};
string s;
inline int get(int x,int y){return (y-1)*w+x;}
inline int getx(int under){return under%w==0?w:under%w;}
inline int gety(int under){return under/w==0?under/w:under/w+1;}
void bfs(int x,int y){
    queue<pair<int,int> > q;
    q.push({get(x,y),0});
    while(!q.empty()){
        int nx = getx(q.front().first),ny = gety(q.front().first),step = q.front().second;
        q.pop(),ans++;
        for(int i=0;i<4;i++){
            int nxtx = nx + dx[i],nxty = ny + dy[i];
            if(nxtx < 1 || nxtx > h || nxty < 1 || nxty > w) continue;
            if(vis[get(nxtx,nxty)]) continue;
            if(bfsvis[get(nxtx,nxty)]) continue;
            if(step+1 > k) continue;
            bfsvis[get(nxtx,nxty)] = 1;
            q.push({get(nxtx,nxty),step+1});
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>h>>w>>k;
    for(int i=1;i<=h;i++){
        cin>>s;
        for(int j=0;j<w;j++) if(s[j] == '#') vis[get(i,j+1)] = 1,boomx[i] = 1,boomy[j+1] = 1;
    }
    for(int i=1;i<=h;i++){
        for(int j=1;j<=w;j++){
            if(boomx[i]) continue;
            if(boomy[j]) continue;
            bfsvis[get(i,j)] = 1,bfs(i,j);
        }
    }
    cout<<ans;
    return 0;
}
```
/*
使用一维数组存储网格。标记障碍物，并标记有障碍的行和列。对于每个既不在障碍行也不在障碍列的格子，作为起点进行 BFS，步数限制为 K，累加访问过的格子数（注意：代码中未清空 `bfsvis`，可能导致不同起点的 BFS 互相干扰，且每个起点都 BFS 一次效率较低。此处按原样保留。
*/

## E
https://atcoder.jp/contests/abc472/tasks/abc472_e

> （题目描述未提供，请参考原题）

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;

int main(){
    // 本题代码未提供，请自行实现
    return 0;
}
```

## F
https://atcoder.jp/contests/abc472/tasks/abc472_f

> （题目描述未提供，请参考原题）

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;

int main(){
    // 本题代码未提供，请自行实现
    return 0;
}
```

## G
https://atcoder.jp/contests/abc472/tasks/abc472_g

> （题目描述未提供，请参考原题）

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 102;

int main(){
    // 本题代码未提供，请自行实现
    return 0;
}
```