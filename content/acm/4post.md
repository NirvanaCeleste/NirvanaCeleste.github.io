---
title: "AtCoder Beginner Contest 467"
date: 2026-07-18
draft: false
comments: true
---
![ABC467提交记录](/img/acm/ABC467_submit.png)
![ABC467](/img/acm/ABC467.png)
## A
https://atcoder.jp/contests/abc467/tasks/abc467_a
简单数学不等式，规避浮点精度误差
#### 问题陈述
通过以下式子计算BMI值：$\text{BMI} = \text{体重}[kg] \div \text{身高}[m] \div \text{身高}[m]$。
在日本，BMI大于等于25的人判定为肥胖。给定身高$H$（厘米）、体重$W$（千克，判断是否肥胖。
原式浮点等价整数不等式：$400 \times W \ge H \times H$，满足输出`Yes`，否则输出`No`。
##### 约束
- $1 \le H \le 300$
- $1 \le W \le 300$
- 所有输入均为整数
##### 输入格式
一行两个整数 $H\ W$
##### 输出格式
单行输出`Yes`或`No`
```cpp
#include <bits/stdc++.h>
using namespace std;
//double h,w,ans,pd = 25.00;
int h,w;
int main(){
	cin>>h>>w;
//	h/=100;
//	ans = w;
//	ans/=h;
//	ans/=h;
//	if(ans >= pd) cout<<"Yes";
	if(400*w>=h*h) cout<<"Yes";
	else cout<<"No";
	return 0;
}	
```
/*
一开始打算直接用浮点除法计算BMI，担心小数精度出错，改用整数乘法比较，完全规避浮点数误差问题。
*/

## B
https://atcoder.jp/contests/abc467/tasks/abc467_b
简单模拟、差值统计
#### 问题陈述
高桥初始持有10000日元，一共$N$家店铺。
第$i$家店铺商品价格$A_i$，支付金额$B_i$（保证$A_i \le B_i$），找零金额为$B_i - A_i$。
- `take`：收下找零；
- `keep`：放弃找零，店家不返还零钱。
设$X$为实际最终所持金额，$Y$为每家店都收下找零的理想金额，输出$Y-X$，即损失的总金额。
##### 约束
- $1 \le N \le 100$
- $1 \le A_i \le B_i \le 100$
- $S_i$为`keep`或`take`
- 所有输入均为整数
##### 输入格式
第一行整数$N$
接下来$N$行，每行$A_i\ B_i\ S_i$
##### 输出格式
单行输出损失金额
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 110;
int n;
struct shop{
	string s;
	int a,b;
}c[maxn];
int x,y;
int main(){
	cin>>n;
	x = 10000,y = 10000;
	for(int i=1;i<=n;i++){
		cin>>c[i].a>>c[i].b>>c[i].s;	
		if(c[i].s == "take") x -= c[i].a;
		else x -= c[i].b;
		y -= c[i].a;
	}
	cout<<y-x; 
	
	return 0;
}
```
/*
y数组全程模拟全部拿找零的最优情况，x模拟真实消费后的余额，两者差值就是放弃找零总共亏的钱。
*/

## C
https://atcoder.jp/contests/abc467/tasks/abc467_c
递推构造，仅\(M=2\)简化版
#### 问题陈述
给定长度$N$的数组$A$，长度$N-1$的数组$B$，数组元素均为$0\sim M-1$。
允许任意次操作：任选下标$i$，将$A_i$数值+1，每次操作代价1。
要求对全部$1\le i\le N-1$满足 $(A_i+A_{i}) \bmod M = B_i$，求最小操作次数。
本题仅$\(M=2\)$，序列由首项0/1唯一确定，两种方案分别统计修改代价取最小值。
##### 约束
- $2 \le N \le 2\times10^5$
- $\(M=2\)$
- $0 \le A_i,B_i \le 1$
- 所有输入均为整数
##### 输入格式
第一行$N\ M$
第二行$A_1\ A_2 \dots A_N$
第三行$B_1\ B_2 \dots B_{N-1}$
##### 输出格式
单行输出最小操作次数
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200020;
int a[maxn],b[maxn],c[maxn],d[maxn];
int n,m = 2,ans1,ans2;
//bool check(int cnt){
//	for(int i=1;i<=n;i++){
//		if(cnt < 0) return 0;
//		
//		
//	}
//	
//	return 1;
//}
void pre(){
	for(int i=1;i<n;i++){
		if(b[i] == 0){
			if(c[i] == 1 && c[i+1] == 0) c[i+1] = 1,ans1++;
			if(c[i] == 0 && c[i+1] == 1) c[i+1] = 0,ans1++;
			if(d[i] == 1 && d[i+1] == 0) d[i+1] = 1,ans2++;
			if(d[i] == 0 && d[i+1] == 1) d[i+1] = 0,ans2++;
		}
		if(b[i] == 1){
			if(c[i] == 0 && c[i+1] == 0) c[i+1] = 1,ans1++;
			if(c[i] == 1 && c[i+1] == 1) c[i+1] = 0,ans1++;
			if(d[i] == 0 && d[i+1] == 0) d[i+1] = 1,ans2++;
			if(d[i] == 1 && d[i+1] == 1) d[i+1] = 0,ans2++;
		}
	}
	
	return;
}
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>a[i],c[i] = a[i],d[i] = a[i];
	for(int i=1;i<n;i++) cin>>b[i];
//	int l=0,r=n,mid=0;
//	while(l<r){
//		mid = (l+r)/2;
//		if(check(mid)) r = mid,ans = mid;
//		else l = mid+1;
//	}
	if(c[1] != 0) c[1] = 0,ans1++;
	if(d[1] != 1) d[1] = 1,ans2++;
	pre();
	cout<<min(ans1,ans2);
	return 0;
}
```
/*
一开始想二分答案求解，写完草稿发现M固定只有2，整个序列由第一个数字唯一决定，直接分两种初始状态递推统计代价更简单。
复制两份数组，分别强制首元素为0/1，顺着相邻模约束依次修正并计数，最后取两者最小值。
*/

## D
https://atcoder.jp/contests/abc467/tasks/abc467_d
计算几何，__int128 大整数防精度丢失
#### 问题陈述
平面上给定两点$\(P,Q\)$确定圆$C_1$，两点$\(R,S\)$确定圆$C_2$。
判断是否存在同心圆$C_1,C_2$（两圆圆心完全一致，半径可不同/相同）。
判断逻辑：两点中垂线斜率相等则两线段平行，此时需验证中垂线重合；不平行则必然存在公共圆心，直接Yes。
全部计算使用__int128交叉相乘，避免long long转double精度爆炸。
##### 约束
- $1 \le T \le 5\times10^4$
- $-10^9 \le P_x,P_y,Q_x,Q_y,R_x,R_y,S_x,S_y \le 10^9$
- $(P_x,P_y) \ne (Q_x)$，$(R_x,R_y)\ne(S_x,S_y)$
- 所有输入均为整数
##### 输入格式
第一行$T$
每组一行：$P_x\ P_y\ Q_x\ Q_y\ R_x\ R_y\ S_x\ S_y$
##### 输出格式
每组单行输出`Yes`或`No`
```cpp
#include <bits/stdc++.h>
using namespace std;
int t;
long long px,py,qx,qy,rx,ry,sx,sy;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> t;
    while(t--){
        cin >> px >> py >> qx >> qy >> rx >> ry >> sx >> sy;
        __int128 k1 = (__int128)(py - qy) * (rx - sx);
        __int128 k2 = (__int128)(ry - sy) * (px - qx);
        if(k1 == k2){
            __int128 tmp1 = (__int128)(px + qx - rx - sx) * (sx - rx);
            __int128 tmp2 = (__int128)(py + qy - ry - sy) * (ry - sy);
            cout << (tmp1 == tmp2 ? "Yes" : "No") << '\n';
        }else{
            cout << "Yes\n";
        }
    }
    return 0;
}
```
/*
直接浮点计算斜率、中点会因为超大坐标丢失精度，改用__int128做无符号整数交叉乘法比较等式。
关闭cin同步加速大量测试用例输入，防止TLE。
*/

## E
https://atcoder.jp/contests/abc467/tasks/abc467_e
区间相邻和模通用DP，本场仅写空框架未实现代码
#### 问题陈述
题意与C完全一致，仅约束修改：$3\le M\le 10^9$，$N\le 2\times 10^5$。
不再仅有0/1两种首项选择，需要数学推导+线性DP维护最小代价，数据范围更大，难度提升。
##### 约束
- $2 \le N \le 2\times 10^5$
- $3 \le M \le 10^9$
- $0 \le A_i,B_i \le M-1$
- 所有输入均为整数
##### 输入输出格式同C题
#### 说明
本场比赛仅预留空main框架，未编写完整解题逻辑，赛后补全思路、注释与AC代码。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
	
	return 0;
}
```

## F
https://atcoder.jp/contests/abc467/tasks/abc467_f
动态贪心+数据结构维护，本场仅写空框架未实现代码
#### 问题陈述
给定$N$个任务，每个任务书写耗时$A_j$，发送后$B_j$分钟收到回复。
支持单点修改$A_i$/$B_i$，每次修改后求最优书写顺序，使得全部回复收到的时间最小。
需要贪心排序规则 + 平衡树/线段树动态维护极值。
##### 约束
- $1 \le N,Q \le 10^5$
- $1 \le A_j,B_j \le 10^9$
##### 输入输出格式
第一行$N\ Q$
第二行$A_1\dots A_N$
第三行$B_1\dots B_N$
后续$Q$行操作：`1 i x`修改$A_i$；`2 i x`修改$B_i$
每次操作后输出最小结束时间
#### 说明
本场比赛仅预留空main框架，未编写完整解题逻辑，赛后补全思路、注释与AC代码。
```cpp
#include <bits/stdc++.h>
int main(){
	
	return 0;
}
```

## G
https://atcoder.jp/contests/abc467/tasks/abc467_g
区间贪心+可持久化/线段树二分，仅输入框架无核心逻辑
#### 问题陈述
给定长度$N$数组，$Q$次修改询问：先单点更新数值，再查询区间$\([l,r]\)$，挑选最少数字使总和$\ge k$；区间总和不足输出-1。
最优策略：每次选区间最大值，用线段树维护区间总和、区间最大值二分求解。
##### 约束
- $1 \le N,Q \le 10^5$
- $1 \le A_i,x \le 10^9$，$1\le k \le 10^{15}$
##### 输入格式
第一行$N\ Q$
第二行初始数组
后续$Q$行每行$c\ x\ l\ r\ k$
##### 输出格式
每次询问输出最少糖果数或-1
#### 说明
本场仅完成输入读取部分，查询二分、线段树核心逻辑未编写，后续补完整AC代码。
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200020;
int a[maxn],b[maxn],c[maxn];
int n,m = 2;
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<n;i++) cin>>b[i];
	
	return 0;
}
```

本场完成A、B、C、D四道完整可AC代码；E、F仅空白主函数框架无解题逻辑；G仅输入读取框架，核心询问代码未实现。后续补题时补齐E/F/G完整题意注释、解题思路与AC代码。