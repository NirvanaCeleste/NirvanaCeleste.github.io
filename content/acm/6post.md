---
title: "Codeforces Round 1114 (Div. 3)"
date: 2026-08-04
draft: false
comments: true
---
![CF1114Div3](/img/acm/CF1114Div3.png)
![CF1114Div3_submit](/img/acm/CF1114Div3_submit.png)

（CF前20分钟交不上东西 吃罚时了 QWQ）
## A
https://codeforces.com/contest/2254/problem/A

爱丽丝、鲍勃和查理正在玩一个关于代币的游戏。他们分别以 $a$、$b$ 和 $c$ 个代币开始。游戏按轮进行。在每轮开始前，他们会检查每个人拥有的代币数量：
- 如果任意两个玩家拥有完全相同数量的代币，游戏立即结束。
- 否则，本轮开始，三个玩家拥有的代币数量严格不同。拥有严格最多代币的玩家给拥有严格最少代币的玩家恰好 1 个代币。

给定起始代币数量 $a$、$b$ 和 $c$，确定游戏在结束前会持续多少轮。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^3$）——测试用例的数量。
每个测试用例由一行包含三个整数 $a$、$b$ 和 $c$（$1 \le a, b, c \le 10$）。

**输出**

对于每个测试用例，输出一个整数——游戏在结束前持续的轮数。

```cpp
#include <bits/stdc++.h>
using namespace std;
int t;
int a,b,c,ans,maxx,minn;
 
int main(){
	cin>>t;
	while(t){
		t--;
		cin>>a>>b>>c;
		ans = 0;
		while(a != b && b != c && a != c){
			maxx = max(a,max(b,c));
			minn = min(a,min(b,c));
			if(maxx == a) a--;
			if(maxx == b) b--;
			if(maxx == c) c--;
			if(minn == a) a++;
			if(minn == b) b++;
			if(minn == c) c++;
			ans++;
		} 
		cout<<ans<<endl;	
	}
	return 0;	
}
```
/*
每次将最大值减 1、最小值加 1 模拟一轮，直到出现相等。
*/

## B
https://codeforces.com/contest/2254/problem/B

设 $f(s)$ 为字符串 $s$ 的压缩版本，通过将每个由相同字符组成的最大连续块替换为该字符的单个副本来形成。例如，$f(\text{"aabbcc"}) = \text{"abc"}$。

设 $|s|$ 表示字符串 $s$ 的长度。相应地，$|f(s)|$ 表示压缩后字符串的长度。

尤瑟夫给了你一个由 $n$ 个小写拉丁字母组成的字符串 $s$。你必须恰好删除一个字符 $s_i$（$2 \le i \le n-1$）来形成新字符串 $s'$，然后找出 $|f(s')|$ 的最小可能值。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个整数 $n$（$3 \le n \le 2 \cdot 10^5$）——字符串的长度。
每个测试用例的第二行包含一个字符串 $s$（$|s| = n$），由小写拉丁字母组成。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出一个整数——删除一个字符后得到的压缩字符串的最小可能长度。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxx = 200020;
int t,n,ans;
string s;
char tmp = ' ';
int pd = 0;

int main(){
	cin>>t;
	while(t){
		t--;
		cin>>n;
		cin>>s;
		ans = 0;
		tmp = ' ';
		pd = 0;
		for(int i=0;i<n;i++){
			if(tmp == s[i]) continue;
			tmp = s[i];
			ans++;
		}
		for(int i=1;i<n-1;i++){
			if(s[i-1] != s[i] && s[i] != s[i+1]){
				pd = 1;
				if(s[i-1] == s[i+1]){
					pd = 2;
					break;	
				}
			}
		}
		if(pd == 1) cout<<ans-1<<endl;
		else if(pd == 2) cout<<ans-2<<endl;
		else cout<<ans<<endl;
	}
	return 0;	
}
```
/*
先求原串压缩长度 ans，删除中间字符可能使压缩长度减少 1 或 2（形成 "aba" 型时减 2）。
*/

## C1
https://codeforces.com/contest/2254/problem/C1

这是该问题的简单版本。在此版本中，你只需判断字符串 $a$ 是否可以转换为字符串 $b$。

尤瑟夫给了你两个长度相同的二进制字符串 $a$ 和 $b$。你可以对 $a$ 执行以下任意操作：
- 选择 $a$ 中等于 `001` 的子串并将其替换为 `100`，反之亦然（即 `001→100` 或 `100→001`）。
- 选择 $a$ 中等于 `110` 的子串并将其替换为 `011`，反之亦然（即 `011→110` 或 `110→011`）。

你的任务是确定是否可以通过有限次操作将字符串 $a$ 转换为字符串 $b$。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个整数 $n$（$1 \le n \le 2 \cdot 10^5$）——每个字符串的长度。
每个测试用例的第二行包含一个二进制字符串 $a$（$|a| = n$），仅由字符 `0` 和/或 `1` 组成。
每个测试用例的第三行包含一个二进制字符串 $b$（$|b| = n$），仅由字符 `0` 和/或 `1` 组成。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，如果可以通过有限次操作将字符串 $a$ 转换为字符串 $b$，则输出 "YES"，否则输出 "NO"。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200010;
string a,b;
int n,n1,n2,t; 
bool ans;
int a1[maxn],a2[maxn],b1[maxn],b2[maxn];

int main(){
	cin>>t;
	while(t){
		t--;
		cin>>n;
		cin>>a>>b;
		ans = 1;
		n1 = 0,n2 = 0; 
		if(n == 1 || n == 2){
			if(a == b) ans = 1;
			else ans = 0;
		}
		if(n >= 3){
			for(int i=0;i<n;i++){
				if(i%2 == 0) a1[++n1] = a[i] - '0',b1[n1] = b[i] - '0';
				else a2[++n2] = a[i] - '0',b2[n2] = b[i] - '0';
			}
			int sum1 = 0,sum2 = 0;
			for(int i=1;i<=n1;i++) sum1 += a1[i],sum2 += b1[i];
			if(sum1 != sum2) ans = 0;
			if(ans){
				sum1 = 0,sum2 = 0;
				for(int i=1;i<=n2;i++) sum1 += a2[i],sum2 += b2[i];
				if(sum1 != sum2) ans = 0;	 
			}
		}	
		if(ans) cout<<"Yes"<<endl;
		else cout<<"No"<<endl;
	}
	return 0;	
}
```
/*
操作不改变奇数位和偶数位上 1 的总数，只需检查奇偶位上的 1 的个数是否一致。
*/

## C2
https://codeforces.com/contest/2254/problem/C2

这是该问题的困难版本。在此版本中，你需要确定将 $a$ 转换为 $b$ 所需的最少操作次数。

尤瑟夫给了你两个长度相同的二进制字符串 $a$ 和 $b$。你可以对 $a$ 执行以下任意操作：
- 选择 $a$ 中等于 `001` 的子串并将其替换为 `100`，反之亦然（即 `001→100` 或 `100→001`）。
- 选择 $a$ 中等于 `110` 的子串并将其替换为 `011`，反之亦然（即 `011→110` 或 `110→011`）。

你的任务是确定将字符串 $a$ 转换为字符串 $b$ 所需的最少操作次数。如果无法通过给定操作将 $a$ 转换为 $b$，则输出 $-1$。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个整数 $n$（$1 \le n \le 2 \cdot 10^5$）——每个字符串的长度。
每个测试用例的第二行包含一个二进制字符串 $a$（$|a| = n$），仅由字符 `0` 和/或 `1` 组成。
每个测试用例的第三行包含一个二进制字符串 $b$（$|b| = n$），仅由字符 `0` 和/或 `1` 组成。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出将 $a$ 转换为 $b$ 所需的最少操作次数。如果不可能，则输出 $-1$。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200010;
string a,b;
int n,n1,n2,t; 
int ans;
int a1[maxn],a2[maxn],b1[maxn],b2[maxn];
int sum1,sum2,sum3,sum4;
int posA1[maxn], posB1[maxn], posA2[maxn], posB2[maxn];
int cntA1, cntB1, cntA2, cntB2;

int main(){
    cin>>t;
    while(t--){
        cin>>n;
        cin>>a>>b;
        ans = 0;
        n1 = n2 = 0;
        sum1 = sum2 = sum3 = sum4 = 0;
        cntA1 = cntB1 = cntA2 = cntB2 = 0;

        for(int i=0;i<n;i++){
            if(i%2==0){
                a1[++n1] = a[i]-'0';
                b1[n1] = b[i]-'0';
                sum1 += a1[n1];
                sum2 += b1[n1];
            }else{
                a2[++n2] = a[i]-'0';
                b2[n2] = b[i]-'0';
                sum3 += a2[n2];
                sum4 += b2[n2];
            }
        }

        if(sum1 != sum2 || sum3 != sum4){
            cout << -1 << '\n';
            continue;
        }

        for(int i=1;i<=n1;i++){
            if(a1[i]==1) posA1[++cntA1] = i;
            if(b1[i]==1) posB1[++cntB1] = i;
        }
        for(int i=1;i<=cntA1;i++){
            ans += abs(posA1[i] - posB1[i]);
        }

        for(int i=1;i<=n2;i++){
            if(a2[i]==1) posA2[++cntA2] = i;
            if(b2[i]==1) posB2[++cntB2] = i;
        }
        for(int i=1;i<=cntA2;i++){
            ans += abs(posA2[i] - posB2[i]);
        }

        cout << ans << '\n';
    }
    return 0;
}
```
/*
同样分离奇偶位，每位的 1 必须移动到对应位置，最小移动距离之和即为答案。
*/

## D
https://codeforces.com/contest/2254/problem/D

尤瑟夫有一个长度为 $n$ 的秘密数组 $a$，由严格正整数组成。对于每个元素 $a_i$，其阴影 $b_i$ 是 $a$ 中所有严格小于 $a_i$ 的元素之和。

形式化地：$b_i = \sum_{1 \le j \le n, \ a_j < a_i} a_j$

给定数组 $b$（即阴影），重构出任意一个能产生这些阴影的数组 $a$。如果存在多个，输出字典序最小的那个。如果不存在这样的数组，则输出 $-1$。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个整数 $n$（$1 \le n \le 2 \cdot 10^5$）——数组的长度。
每个测试用例的第二行包含 $n$ 个整数 $b_1, b_2, \dots, b_n$（$0 \le b_i \le 10^{18}$）——阴影数组的元素。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，如果存在有效的数组 $a$，输出 $n$ 个严格正整数 $a_1, a_2, \dots, a_n$（$a_i \ge 1$）——字典序最小的原数组。如果不存在，则输出 $-1$。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200200;
long long b[maxn],a[maxn];
int t,n;
int main(){
	cin>>t;
	while(t){
		t--;
		
	}
	return 0;	
}
```

## E
https://codeforces.com/contest/2254/problem/E

尤瑟夫有一个长度为 $n$ 的隐藏数组 $a$，完全由严格正整数组成。恰好执行了一次操作来创建数组 $b$：
- 设 $b_1 = a_1$。
- 对于每个 $i$ 从 $2$ 到 $n$，设 $b_i = a_i - a_{i-1}$。
- 之后，$b$ 的元素被完全打乱。

给定打乱后的数组 $b$。重构出字典序最小的原数组 $a$。如果 $b$ 的任何排列都无法产生一个由严格正整数组成的数组 $a$，则输出 $-1$。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个整数 $n$（$1 \le n \le 2 \cdot 10^5$）——数组的大小。
每个测试用例的第二行包含 $n$ 个整数 $b_1, b_2, \dots, b_n$（$-10^9 \le b_i \le 10^9$）——打乱后的数组 $b$ 的元素。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，输出 $n$ 个严格正整数 $a_1, a_2, \dots, a_n$（$a_i \ge 1$）——字典序最小的原数组 $a$。如果无法创建有效的数组 $a$，则输出 $-1$。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 200010;
long long b[maxn], a[maxn];
long long sum;
int n, t;
long long minPos;
int ans;
int flag;

int main() {
    cin >> t;
    while (t--) {
        t--;
        cin >> n;
        sum = 0;
        minPos = 1e18;
        flag = 1;
        
        for (int i = 1; i <= n; i++) {
            cin >> b[i];
            sum += b[i];
            if (b[i] > 0) minPos = min(minPos, b[i]);
        }
        
        if (sum <= 0 || minPos == 1e18) {
            cout << -1 << endl;
            continue;
        }
        
        multiset<long long> ms;
        for (int i = 1; i <= n; i++) ms.insert(b[i]);
        
        auto it = ms.find(minPos);
        ms.erase(it);
        
        a[1] = minPos;
        long long cur = minPos;
        
        for (int i = 2; i <= n; i++) {
            long long need = -cur + 1;
            auto it2 = ms.lower_bound(need);
            
            if (it2 == ms.end()) {
                flag = 0;
                break;
            }
            
            long long d = *it2;
            ms.erase(it2);
            cur += d;
            a[i] = cur;
            
            if (a[i] <= 0) {
                flag = 0;
                break;
            }
        }
        
        if (!flag) {
            cout << -1 << endl;
            continue;
        }
        
        for (int i = 1; i <= n; i++) {
            if (i > 1) cout << " ";
            cout << a[i];
        }
        cout << endl;
    }
    return 0;
}
```
/*
a_n = sum(b)，需为正。a_1 取最小正 b_i 保证字典序最小，之后贪心选择使 a_i 为正的最小差值。
*/

## F
https://codeforces.com/contest/2254/problem/F

尤瑟夫给了你一个偶数 $n$ 和两个数组 $a$ 和 $b$，两者都由 $n$ 个非负整数组成。

你可以对数组 $a$ 执行以下任意次操作（可能为零次）：
- 选择一个下标 $i$（$1 \le i \le n$）。
- 对于所有满足 $1 \le j \le n$ 且 $j \neq i$ 的 $j$，将 $a_j$ 替换为 $a_j \oplus a_i$（这里 $\oplus$ 表示按位异或操作）。
- 元素 $a_i$ 保持不变。

确定是否可以通过有限次操作将数组 $a$ 转换为数组 $b$。

**输入**

第一行包含一个整数 $t$（$1 \le t \le 10^4$）——测试用例的数量。
每个测试用例的第一行包含一个偶数 $n$（$2 \le n \le 2 \cdot 10^5$）——数组的长度。
每个测试用例的第二行包含 $n$ 个整数 $a_1, a_2, \dots, a_n$（$0 \le a_i < 2^{30}$）——数组 $a$ 的元素。
每个测试用例的第三行包含 $n$ 个整数 $b_1, b_2, \dots, b_n$（$0 \le b_i < 2^{30}$）——数组 $b$ 的元素。
保证所有测试用例中 $n$ 的总和不超过 $2 \cdot 10^5$。

**输出**

对于每个测试用例，如果可以通过有限次操作将数组 $a$ 转换为数组 $b$，则输出 "YES"，否则输出 "NO"。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxx = 100010;

int main(){
	cin>>t;
	while(t){
		t--;
		
	}
	return 0;	
}
```
