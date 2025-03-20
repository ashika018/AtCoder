# 13_最短経路問題：ワーシャルフロイド法

node_n, edge_n = list(map(int, input().split(' ')))
# dpテーブルの生成と初期値を格納
INF = float('inf')
dp = [[INF]*node_n for _ in range(node_n)]
for i in range(node_n): dp[i][i] = 0
for _ in range(edge_n):
    node1, node2, d = list(map(int, input().split(' ')))
    dp[node1][node2] = d

# ワーシャルフロイド部分
for k in range(node_n):
    for i in range(node_n):
        for j in range(node_n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(node_n): 
    if(dp[i][i]<0): 
        print('NEGATIVE CYCLE')
        exit()

for i in range(len(dp)): print(' '.join([str(n) for n in dp[i]]))