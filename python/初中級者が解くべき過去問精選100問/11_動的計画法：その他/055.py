# 11_動的計画法：その他
# 広義単調増加部分列の最大の長さを求める
# 狭義単調増加の時と二分探索のコードが少し異なる（①）

N = int(input())
A = [int(input()) for _ in range(N)]
B = A[::-1]

INF = float('inf')
dp = [INF for _ in range(N+1)]

def binary_search(l, r, c):
    while True:
        if(r-l<=1): break
        mid = (l+r)//2
        if(dp[mid]<=c): l = mid # ①
        else: r = mid
    return r

for b in B:
    i = binary_search(l=0,r=len(dp)-1, c=b)
    dp[i] = b

LIS = 0
for i in range(1,len(dp)):
    if(dp[i]==INF): break
    LIS = i
print(LIS)