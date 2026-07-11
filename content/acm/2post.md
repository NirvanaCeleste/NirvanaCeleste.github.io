---
title: "AtCoder Beginner Contest 463 E题"
date: 2026-07-12T00:00:00+08:00
draft: false
comments: true
---


## E

https://atcoder.jp/contests/abc463/tasks/abc463_e 

类图论，加强的最短路

#### 问题陈述

AtCoder 国家有 $N$ 座城市和 $M$ 条道路。 $i$ 条道路 $(1\le i\le M)$ 双向连接 $u _ i$ 和 $v _ i$ 两个城市，从一个城市到另一个城市只需 $T _ i$ 分钟。

此外，每个城市都安装了曲速门，使用曲速门可以在 $X _ i+X _ j+Y$ 分钟内从城市 $i\ (1\le i\le N)$ 到达城市 $j\ (1\le j\le N)$ 。

国内没有其他城市之间的交通方式。

请为每个 $k=2,3,\ldots,N$ 解出下面的问题：

- 求从城市 $1$ 到城市 $k$ 所需的最短时间。

在同一城市，从一条道路或翘曲门到另一条道路或翘曲门所需的时间可以忽略不计。

- $2\le N\le2\times10 ^ 5$
- $0\le M\le2\times10 ^ 5$
- $1\le u _ i\lt v _ i\le N\ (1\le i\le M)$
- $1\le T _ i\le10 ^ 9\ (1\le i\le M)$
- $1\le X _ i\le10 ^ 9\ (1\le i\le N)$
- $1\le Y\le 10 ^ 9$
- 所有输入值均为整数。

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const unsigned int maxx = 200001 + 2;
const ll INF = 0x3f3f3f3f3f3f3f3f;
/*
一开始想复杂了 感觉证明不了缩点 
我在想 如果边那么多 直接建边肯定是不行的 需要缩点
但是缩点真的可行吗 比如把 传送门 拆成 前半段加常值Y加后半段 然后去泡普通的最短路 
还以为会1 -> 3 的最短路径 可能会被认为是1 -> 2 的前半段加上 1 -> 3 的后半段 
今天补题的时候发现 人家题目其实已经说了 所有前半段都是X【i】
所有后半段也都是X【j】 所以不存在刚刚说的那种情况 
甚至前后半段都是X一个常数列 读题大失误啊 
*/ 
ll n,m,tot,y,dotin,dotout;
ll head[maxx],vlu[maxx*4],nxt[maxx*4],to[maxx*4],dis[maxx],x[maxx];

inline void insert(ll u,ll v,ll w){
	to[++tot] = v;
	vlu[tot] = w;
	nxt[tot] = head[u];
	head[u] = tot;
}
void pre(){
	scanf("%lld%lld%lld",&n,&m,&y);
	ll u,v,w;
	for(int i=1;i<=m;i++) scanf("%lld%lld%lld",&u,&v,&w),insert(u,v,w),insert(v,u,w);
    // 虚拟点一并初始化为无穷
	for(int i=1;i<=n+2;i++) dis[i] = INF;
	for(int i=1;i<=n;i++) scanf("%lld",&x[i]);
	dotin = n+1;
	dotout = n+2;
	insert(dotin,dotout,y);
	for(int i=1;i<=n;i++) insert(i,dotin,x[i]),insert(dotout,i,x[i]);
	return;
}
void dij(ll root){
	priority_queue<pair<ll,ll> > q;//大根堆模拟小根堆 
	dis[root] = 0;
	q.push(make_pair(0,root));
	while(!q.empty()){
		ll curd = -q.top().first;
		ll u = q.top().second;
		q.pop();
		if(curd > dis[u]) continue;
		for(ll i=head[u];i;i=nxt[i]){
			ll v = to[i],w = vlu[i];
			//注意迪杰斯特拉需要先更新最短路再插入新节点 
			if(dis[v] > dis[u] + w){
				dis[v] = dis[u] + w;
				q.push(make_pair(-dis[v],v));//注意此处插入的是 dis[v] 
			}
		}
	}
}
int main(){
	pre();
	dij(1);
	for(int i=2;i<=n;i++) printf("%lld ",dis[i]);
	return 0;
}
```