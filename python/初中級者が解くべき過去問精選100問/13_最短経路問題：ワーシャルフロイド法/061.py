# 13_最短経路問題：ワーシャルフロイド法

busstop_n, route_n = list(map(int, input().split(' ')))
INF = float('inf')
dp = [[INF]*(busstop_n+1) for _ in range(busstop_n+1)]
for _ in range(route_n):
    busstop1, busstop2, time = list(map(int, input().split(' ')))
    dp[busstop1][busstop2] = time
    dp[busstop2][busstop1] = time
for i in range(busstop_n+1): dp[i][i] = 0


for k in range(1, busstop_n+1):
    for i in range(1, busstop_n+1):
        for j in range(1, busstop_n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])


# ansを出すためにややめんどくさい処理をする
ans = INF
for row in range(1, busstop_n+1):
    tmp = 0
    for col in range(1, busstop_n+1):
        if(dp[row][col]<INF): tmp = max(tmp, dp[row][col])
    if(tmp>0): ans = min(ans, tmp)
# for l in dp: print(l)
print(ans)