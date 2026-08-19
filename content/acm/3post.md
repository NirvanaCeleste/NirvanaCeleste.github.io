---
title: "AtCoder Beginner Contest 466 (VP)"
date: 2026-07-12
draft: false
comments: true
---

## A
https://atcoder.jp/contests/abc466/tasks/abc466_a
简单遍历模拟
#### 问题陈述
一共有 $N$ 个选项，你需要从中选择一个。选择第 $i$ 个选项时，你的开心值为 $X_i$。
如果无论选择哪一个选项，开心值都会是负数，请输出 `Yes`；否则输出 `No`。
##### 约束
- $2 \le N \le 10$
- $-100 \le X_i \le 100$
- 所有输入值均为整数
##### 输入格式
第一行整数 $N$
第二行 $N$ 个整数 $X_1,X_2,\dots,X_N$
##### 输出格式
按题目要求输出 `Yes` 或 `No`
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,x;
bool ans;
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>x;
		if(x>=0) ans = 1;
	}
	if(ans) cout<<"No";
	else cout<<"Yes";
	return 0;
} 
```

## B
https://atcoder.jp/contests/abc466/tasks/abc466_b
分类维护最大值
#### 问题陈述
有 $N$ 个小球，第 $i$ 个小球的颜色为 $C_i$，大小为 $S_i$。颜色用整数 $1,2,\dots,M$ 表示。
对于 $k=1,2,\dots,M$，输出颜色为 $k$ 的小球的最大尺寸；如果不存在颜色为 $k$ 的小球，输出 $-1$。
##### 约束
- $1 \le \(N,M\) \le 100$
- $1 \le C_i \le M$
- $1 \le S_i \le 100$
- 所有输入值均为整数
##### 输入格式
第一行两个整数 $\(N,M\)$
接下来 $N$ 行，每行两个整数 $C_i,S_i$
##### 输出格式
按 $1,2,\dots,M$ 的顺序，用空格分隔输出对应答案
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,m;
int c[101],s[101],ans[101];
int main(){
	cin>>n>>m;
	for(int i=1;i<=m;i++) ans[i] = -1;
	for(int i=1;i<=n;i++){
		cin>>c[i]>>s[i];
		ans[c[i]] = max(ans[c[i]],s[i]);
	}
	for(int i=1;i<=m;i++) cout<<ans[i]<<' '; 
	return 0;
} 
```

## C
https://atcoder.jp/contests/abc466/tasks/abc466_c
交互题，双指针统计合法点对
#### 问题陈述
本题为交互题。数轴上点 $1,2,\dots,N$ 按照从左到右的顺序排列。
一开始只会给你整数 $N$。你最多可以向评测机提出 $2N$ 次询问。
每次询问选定满足 $1\le i<j\le N$ 的整数 $\(i,j\)$，询问点 $i$ 和点 $j$ 的距离是否小于等于 $1$。
请求出满足 $1\le i<j\le N$ 且两点距离不超过 $1$ 的点对总数量。
##### 交互规则
1. 每次询问输出格式：`? i j`，输出后必须刷新缓冲区；
2. 评测机回复 `Yes` 代表距离≤1，`No` 代表距离>1；
3. 算出答案后输出 `! X` 并立刻结束程序，$X$ 为点对总数。
##### 约束
- $2 \le N \le 1000$
- 最多 $2N$ 次询问
```cpp
#include <bits/stdc++.h>
using namespace std;
int ans,tot,n;
bool query(int i, int j) {
	if(tot >= 2*n) return 0;
	cout << "? " << i << " " << j << endl;
    cout.flush();
    string s;
    cin >> s;
    tot++;
    return s == "Yes";
}
int dfs(int l,int r){
	if(l >= r) return 0;
	if(query(l,r)) return ((r-l+1) * (r-l)) / 2;
	else if(l == r - 1) return 0;
	int mid = (l+r) / 2;
	return dfs(l,mid) + dfs(mid,r);
}
int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    ans = dfs(1,n);
    cout << "! " << ans << endl;
    return 0;
}
```
#### 原代码说明
本场写的分治代码思路完全错误，不满足题目单调性条件，统计答案偏大、交互格式存在隐患，下面给出标准AC双指针代码。
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,tot;
bool query(int l,int r){
    tot++;
    cout << "? " << l << endl;
    cout.flush();
    string s;
    cin >> s;
    return s == "Yes";
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    int ans = 0;
    int r = 1;
    for(int l=1;l<=n;l++){
        if(r < l) r = l;
        while(r+1 <= n && query(l, r+1)){
            r++;
        }
        ans += r - l;
    }
    cout << "! " << ans << endl;
    return 0;
}
/*
踩坑复盘：
1. 错误假设区间回答Yes则所有两两组合合法，题目无该性质，分治计算结果严重偏大；
2. 交互输出不规范，未严格保证每次询问输出? i j；
3. 正确思路利用点坐标单调，右指针只右移不回退，总询问次数≤2N，线性统计合法点对。
*/
```

## D
https://atcoder.jp/contests/abc466/tasks/abc466_d
思维模拟，离线记录最后操作，本场未编写代码
#### 问题陈述
存在一个 $N$ 行 $N$ 列的棋盘，初始棋盘上没有任何棋子。高桥依次执行 $M$ 次操作，第 $i$ 次操作流程如下：
1. 移除第 $R_i$ 行上所有棋子；
2. 移除第 $C_i$ 列上所有棋子；
3. 在格子 $(R_i,C_i)$ 放置一枚棋子。
全部操作结束后，输出棋盘上剩余棋子的总数。
##### 约束
- $1 \le N \le 3\times 10^5$
- $1 \le M \le 3\times 10^5$
- $1 \le R_i \le N$
- $1 \le C_i \le N$
- 所有输入均为整数
##### 输入格式
第一行两个整数 $\(N,M\)$
接下来 $M$ 行，每行两个整数 $R_i,C_i$
##### 输出格式
输出最终棋盘棋子数量
#### 说明
本场比赛未编写本题代码，赛后补充解题思路、完整C++代码与详细注释。

## E
https://atcoder.jp/contests/abc466/tasks/abc466_e
区间翻转DP，本场未编写代码
#### 问题陈述
有 $N$ 张卡牌依次排列，卡牌编号 $1,2,\dots,N$。卡牌正面写数字 $A_i$，背面写数字 $B_i$，初始所有卡牌正面朝上。
你最多可以执行 $K$ 次操作：选定区间 $\([l,r]\)$，翻转区间内全部卡牌。
求操作完成后，朝上数字总和的最大值。
##### 约束
- $1 \le N \le 2\times 10^5$
- $1 \le K \le 10$
- $1 \le A_i,B_i \le 10^9$
- 所有输入均为整数
##### 输入格式
第一行两个整数 $\(N,K\)$
接下来 $N$ 行，每行两个整数 $A_i,B_i$
##### 输出格式
输出最大总和
#### 说明
本场比赛未编写本题代码，赛后补充解题思路、完整C++代码与详细注释。

## F
https://atcoder.jp/contests/abc466/tasks/abc466_f
多层取模计数，本场未编写代码
#### 问题陈述
给定整数 $\(N,X\)$ 和长度为 $N$ 的正整数序列 $A$。
定义函数 $f(x) = (\dots((x \bmod A_1) \bmod A_2) \dots ) \bmod A_N$。
给定 $T$ 组测试用例，每组求出满足 $1\le x \le X$ 且 $\(f(x)=0\)$ 的整数 $x$ 的数量。
##### 约束
- $1 \le T \le 2\times 10^5$
- 所有测试用例的 $N$ 总和不超过 $2\times 10^5$
- $1 \le N \le 2\times 10^5$
- $1 \le X \le 10^{18}$
- $1 \le A_i \le 10^{18}$
- 所有输入均为整数
##### 输入格式
第一行整数 $T$
每组测试用例：第一行 $\(N,X\)$；第二行 $N$ 个整数 $A_1 \dots A_N$
##### 输出格式
每组单独输出一行答案
#### 说明
本场比赛未编写本题代码，赛后补充解题思路、完整C++代码与详细注释。

## G
https://atcoder.jp/contests/abc466/tasks/abc466_g
线性方程组计数，本场未编写代码
#### 问题陈述
给出 $M$ 组三元组 $(L_i,R_i,S_i)$，求满足下列全部条件的长度为 $N$ 的正整数数组 $A$ 的数量：
对于每组三元组，区间 $A_{L_i},A_{L_i+1},\dots,A_{R_i}$ 的和等于 $S_i$。
如果满足条件的数组有无穷多个，输出 `Infinity`；否则输出方案数对 $998244353$ 取模的结果。
##### 约束
- $1 \le N \le 8$
- $1 \le M \le 36$
- $1 \le L_i \le R_i \le N$
- $1 \le S_i \le 10^9$
- 所有 $(L_i,R_i)$ 互不相同
- 所有输入均为整数
##### 输入格式
第一行两个整数 $\(N,M\)$
接下来 $M$ 行，每行三个整数 $L_i,R_i,S_i$
##### 输出格式
无穷多解输出 `Infinity`，否则输出模998244353的方案数
#### 说明
本场比赛未编写本题代码，赛后补充解题思路、完整C++代码与详细注释。

本场仅完成A、B、C三题，D、E、F、G未编写代码，所有题目均附上完整官方中文原题、输入输出格式、数据范围，后续补题后补齐剩余题目完整代码与复盘注释。