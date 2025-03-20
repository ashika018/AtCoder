# 11_動的計画法：その他
# アルゴリズムの理解に少し手間取った。
# アリ本、自分のノートを見ればわかるはず。

n = int(input())
A = [int(input()) for i in range(n)]

INF = float('inf')
dp = [INF for _ in range(n+1)]

def binary_search(l, r, a):
    while True:
        if(r-l<=1): break
        mid = (l+r)//2
        if(dp[mid]<a): l = mid
        else: r = mid
    return r

for a in A:
    i = binary_search(l=0,r=len(dp)-1, a=a)
    dp[i] = a

for i in range(1, len(dp)):
    if(dp[i]==INF): break
    ans = i
print(ans)