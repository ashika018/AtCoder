# 13_最短経路問題：ワーシャルフロイド法

row, col = list(map(int, input().split(' ')))
cost_M = [list(map(int, input().split(' '))) for _ in range(10)]
wall_M = [list(map(int, input().split(' '))) for _ in range(row)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            cost_M[i][j] = min(cost_M[i][j], cost_M[i][k]+cost_M[k][j])

ans = 0
for r in range(row):
    for c in range(col):
        value = wall_M[r][c]
        if(value!=-1): ans += cost_M[value][1]

print(ans)