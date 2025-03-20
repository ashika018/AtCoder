# 13_最短経路問題：ワーシャルフロイド法

city_n = int(input())
dp= [list(map(int, input().split(' '))) for _ in range(city_n)]

# MLEする原因はlっぽい。
# lをリストのまま扱ってたらめちゃくちゃTLEしたから、lの長さがとんでもないのでしょう、、。
l = []
for k in range(city_n):
    for i in range(city_n):
        for j in range(city_n):
            if(dp[i][j] > dp[i][k]+dp[k][j]):
                print(-1)
                exit()
            if(dp[i][j] == dp[i][k]+dp[k][j]):
                if(dp[i][k]!=0 and dp[k][j]!=0):
                    l.append((i,j))

l = set(l)
ans = 0
for i in range(city_n):
    for j in range(city_n):
        if((i,j) not in l):
            ans += dp[i][j]
print(ans//2)