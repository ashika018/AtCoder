# 11_動的計画法：その他
# LISであることに気づけるかどうかがポイント

N = int(input())
C = [int(input()) for _ in range(N)]

INF = float('inf')
dp = [INF for _ in range(N+1)]

def binary_search(l, r, c):
    while True:
        if(r-l<=1): break
        mid = (l+r)//2
        if(dp[mid]<c): l = mid
        else: r = mid
    return r

for c in C:
    i = binary_search(l=0,r=len(dp)-1, c=c)
    dp[i] = c

LIS = 0
for i in range(1,len(dp)):
    if(dp[i]==INF): break
    LIS = i
print(N-LIS)