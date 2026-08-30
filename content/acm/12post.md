---
title: "牛客练习赛156"
date: 2026-08-28
draft: false
comments: true
---

![niuke156](/img/acm/niuke156.png)
![niuke156提交记录](/img/acm/niuke156_submit.png)

## A
https://ac.nowcoder.com/acm/contest/139209/A

> 有一条无限长的数轴，糖果店在 $0$ 点位置。初始时 RainbowDash 的坐标是一个整数 $X \in [-10, 10]$，他会移动 $2$ 步，用一个字符串 $s = s_1s_2$ 表示，如果 $s_i = \texttt{L}$ 他的第 $i$ 次移动会向左移动一个单位；如果 $s_i = \texttt{R}$ 他的第 $i$ 次移动会向右移动一个单位。他手里有一个坏掉的 GPS，每移动一步，GPS 会显示对应的信息，用一个字符串 $t = t_1t_2$ 表示，若第 $i$ 次移动后位置相对移动前距离糖果店更近，$t_i = \texttt{C}$；否则 $t_i = \texttt{F}$。现在给你 RainbowDash 的移动序列 $s$ 以及 GPS 的指示序列 $t$，请你判断 RainbowDash 的初始位置可能在哪里。如果不存在合法的初始位置，请输出 `T_T`。

**输入**

第一行输入一个长度为 $2$ 且仅由字符 `L`、`R` 组成的字符串 $s$，表示移动序列。第二行输入一个长度为 $2$ 且仅由字符 `C`、`F` 组成的字符串 $t$，表示 GPS 的指示序列。

**输出**

如果可以找到一个初始坐标 $X$ 使得移动和 GPS 指示完全匹配，请输出任意一个可能的初始坐标；如果不存在这样的位置，请输出 `T_T`。

```cpp
#include <bits/stdc++.h>
using namespace std;
string s1,s2;

int main(){
        cin>>s1>>s2;
        if(s1 == "LL"){
                if(s2 == "CC") cout<<2;
                else if(s2 == "CF") cout<<1;
                else if(s2 == "FF") cout<<-2;
                else if(s2 == "FC") cout<<"T_T";
        }
        else if(s1 == "LR"){
                if(s2 == "CC") cout<<"T_T";
                else if(s2 == "CF") cout<<1;
                else if(s2 == "FF") cout<<"T_T";
                else if(s2 == "FC") cout<<-1;
        }
        else if(s1 == "RR"){
                if(s2 == "CC") cout<<-2;
                else if(s2 == "CF") cout<<-1;
                else if(s2 == "FF") cout<<2;
                else if(s2 == "FC") cout<<"T_T";
        }
        else if(s1 == "RL"){
                if(s2 == "CC") cout<<"T_T";
                else if(s2 == "CF") cout<<-1;
                else if(s2 == "FF") cout<<"T_T";
                else if(s2 == "FC") cout<<1;
        }
        return 0;
}
```
/*
移动序列只有 $4$ 种可能（LL、LR、RL、RR），GPS 指示也只有 $4$ 种可能（CC、CF、FC、FF）。直接枚举所有 $16$ 种状态组合，对每种组合判断是否存在整数 $X \in [-10, 10]$ 满足条件，输出任意一个即可。注意输出 `T_T` 的情况。
*/

## B
https://ac.nowcoder.com/acm/contest/139209/B

> Rainbow 和 Flower 在进行一场卡牌游戏。桌面上有一个包含 $n$ 张卡牌的牌堆，每张卡牌都有数字和花色两种属性，数字有 `0` 和 `1` 两种，花色有 `B` 和 `R` 两种。每张牌上的数字用字符串 $s = s_1s_2\dots s_n$ 表示，花色用字符串 $t = t_1t_2\dots t_n$ 表示，第 $i$ 张牌上的数字为 $s_i$，花色为 $t_i$。数字为 `0` 的卡牌或花色为 `B` 的卡牌对 Rainbow「有效」，数字为 `1` 的卡牌或花色为 `R` 的卡牌对 Flower「有效」。游戏开始时，两人手里都没有卡牌。Rainbow 先手，两人轮流从牌堆中任意选择一张牌放到自己手中，当牌堆上的 $n$ 张卡牌被全部挑完后，游戏结束。两人分别统计自己手中对自己「有效」的卡牌的数量，数量多的一方获胜；若数量相等，则为平局。Rainbow 和 Flower 都绝顶聪明，都使用最优策略进行游戏，请你判断游戏的结果。

**输入**

每个测试文件均包含多组测试数据。第一行输入一个整数 $T$（$1 \le T \le 10^4$）代表数据组数。每组测试数据第一行输入一个整数 $n$（$1 \le n \le 10^5$），表示牌堆的卡牌数量。第二行输入一个长度为 $n$ 且仅由字符 `0`、`1` 组成的字符串 $s$。第三行输入一个长度为 $n$ 且仅由字符 `B`、`R` 组成的字符串 $t$。保证单个测试文件的 $n$ 之和不超过 $10^5$。

**输出**

对于每一组测试数据，新起一行。若 Rainbow 获胜，输出 `Rainbow`；若 Flower 获胜，输出 `Flower`；若平局，输出 `Draw`。

```cpp
#include <bits/stdc++.h>
using namespace std;
int t,n,tmp1,tmp2,tmp3,a,b;
string s1,s2;

int main(){
        ios::sync_with_stdio(false);
        cin.tie(0);
        cin>>t;
        while(t--){
                tmp1 = 0,tmp2 = 0,tmp3 = 0;
                a = 0,b = 0;
                cin>>n;
                cin>>s1>>s2;
                for(int i=0;i<n;i++){
                        if(s1[i] == '0' && s2[i] == 'B') tmp1++;
                        if(s1[i] == '0' && s2[i] == 'R' || s1[i] == '1' && s2[i] == 'B') tmp2++;
                        if(s1[i] == '1' && s2[i] == 'R') tmp3++;
                }
                if(tmp2 % 2 == 1){
                        a += tmp2/2+1,b += tmp2/2;
                        if(tmp3 == tmp1 + 1 || tmp3 == tmp1) b += tmp3,a += tmp1;
                        else if(tmp3 < tmp1) b += tmp3,a += tmp3 + (tmp1 - tmp3)/2;
                        else if(tmp3 > tmp1 + 1) b += tmp1 + ( ((tmp3 - tmp1) % 2 == 1) ? (tmp3 - tmp1)/2 + 1 : (tmp3 - tmp1)/2 ), a += tmp1;
                }
                else{
                        a += tmp2/2,b += tmp2/2;
                        if(tmp1 == tmp3 + 1 || tmp1 == tmp3) a += tmp1,b += tmp3;
                        else if(tmp1 < tmp3) a += tmp1,b += tmp1 + (tmp3 - tmp1)/2;
                        else if(tmp1 > tmp3 + 1) a += tmp3 + ( ((tmp1 - tmp3) % 2 == 1) ? (tmp1 - tmp3)/2 + 1 : (tmp1 - tmp3)/2 ), b += tmp3;
                }
                if(a > b) cout<<"Rainbow"<<'\n';
                else if(a == b) cout<<"Draw"<<'\n';
                else if(a < b) cout<<"Flower"<<'\n';
        }
        return 0;
}
```
/*
将卡牌分成三类：
- 第 1 类：数字为 `0` 且花色为 `B`（对 Rainbow 有效，对 Flower 无效）
- 第 2 类：数字与花色不一致（`0R` 或 `1B`，对双方都有效）
- 第 3 类：数字为 `1` 且花色为 `R`（对 Flower 有效，对 Rainbow 无效）

双方都会优先抢夺第 2 类卡牌（对双方都有用）。第 2 类数量为奇数时先手多拿一张。剩余的双方再根据第 1 类和第 3 类的数量差进行分配。分类讨论累加双方分数后比较即可。
*/

## C
https://ac.nowcoder.com/acm/contest/139209/C

这个数学转化和证明其等价性和最优性花了太久

> RainbowDash 正在设计烟花。这款烟花一共有 $n$ 个发光节点，需要用 $n-1$ 个连接杆将这些发光节点连在一起，每个连接杆都能连接两个发光节点。出于结构稳定的考虑，整个烟花骨架需要满足以下条件：
> - 任意两个发光节点之间都能通过不超过 $d$ 个连接杆互相到达；
> - 每个发光节点直接连接的连接杆数量不超过 $k$。
>
> 请你帮助 RainbowDash 设计一种符合要求的烟花。

**输入**

每个测试文件均包含多组测试数据。第一行输入一个整数 $T$（$1 \le T \le 10^4$）代表数据组数。每组测试数据第一行输入三个整数 $n, d, k$（$2 \le n \le 10^5$，$1 \le d, k \le n$）。保证单个测试文件的 $n$ 之和不超过 $10^5$。

**输出**

对于每组测试数据，新起一行。如果无法设计出符合条件的烟花，请输出 `-1`；否则输出 $n-1$ 行，每行包含两个整数 $u_i, v_i$（$1 \le u_i, v_i \le n$），表示第 $i$ 个连接杆连接两个发光节点。如果存在多个解决方案，您可以输出任意一个。

```cpp
#include <bits/stdc++.h>
using namespace std;
int n,d,k;
int used = 0;
vector<pair<int, int> >edges;
// maxDepth还能往下延伸的最大深度degLeft当前节点还能添加的子节点数
void dfs(int u,int maxDepth,int degLeft) {
    if (maxDepth == 0 || degLeft == 0 || used == n) return;
    for (int i=0;i<degLeft && used<n;i++) {
        int v = ++used;
        edges.push_back({u, v});
        //新节点 v 可以继续延伸的深度减 1 它剩余的可分配度数为 k-1 因为它已经连了一个父节点
        dfs(v,maxDepth - 1,k - 1);
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
        cin>>n>>d>>k;
        edges.clear();
        used = 0;
        int len = min(d, n - 1); // 实际链长（边数）
        if((len > 1 && k < 2)){//无解
            cout<<-1<<'\n';
            continue;
        }
        for(int i=1;i<=len;i++) edges.push_back({i,i + 1});
        used = len + 1;
        for(int i=1;i<=len+1;i++){
            int maxDepth = min(d - (i - 1), d - (len + 1 - i));
            int degLeft = (i == 1 || i == len + 1) ? k - 1 : k - 2;
            dfs(i,maxDepth,degLeft);
        }
        if(used < n) cout<<-1<<'\n';
        else for(auto &e : edges) cout<<e.first<<' '<<e.second<<'\n';
    }
    return 0;
}
```
/*
先构造一条长度不超过 $d$ 的链作为直径骨架，链上的节点编号为 $1, 2, \dots, len+1$（$len = \min(d, n-1)$）。然后在这条链的每个节点上，按照剩余深度和剩余度数限制继续挂载子节点。具体地，对于链上第 $i$ 个节点，其还能向下延伸的最大深度为 $\min(d - (i-1), d - (len+1-i))$（即到链两端距离的最小值，保证直径不超过 $d$），剩余可连接子节点数为 $k - (i$ 在链上的度数$)$。DFS 不断挂载新节点，直到用完 $n$ 个节点或无法继续。如果最终节点数不足 $n$，说明无解，输出 $-1$。
*/
## DEF都太过于难了
同时D很像之前打OI的时候做过的一道题，看起来是按位（因为有异或）去分配权值
https://ac.nowcoder.com/acm/contest/139209/D
https://ac.nowcoder.com/acm/contest/139209/E
https://ac.nowcoder.com/acm/contest/139209/F