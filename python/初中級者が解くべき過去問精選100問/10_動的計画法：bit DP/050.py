# 動的計画法：bit DP
# 49とは違いグラフが無向グラフであることに注意

INF = float('inf')
building_n, road_n = list(map(int, input().split(' ')))
graph_M = [[(INF, INF)]*(building_n) for _ in range(building_n)]
for _ in range(road_n):
    s,t,d,time = list(map(int, input().split(' ')))
    graph_M[s-1][t-1] = (d, time)

dp = [[[INF,0]]*(building_n) for _ in range(2**building_n)]
dp[1][0] = [0,1]

for subset in range(2**building_n):
    for v in range(building_n):
        for k in range(building_n):
            if(graph_M[k][v][0]<=graph_M[v][k][0]): distance, time = graph_M[k][v][0], graph_M[k][v][1]
            else: distance, time = graph_M[v][k][0], graph_M[v][k][1]
            has_visited_k = (subset>>k & 1 == 1)
            has_visited_v = (subset>>v & 1 == 1)
            is_on_time = (dp[subset][k][0]+distance<=time)
            if((has_visited_k) and (not has_visited_v) and (is_on_time)):
                new_subset = subset | 1<<v
                if(dp[new_subset][v][0] == dp[subset][k][0]+distance):
                    dp[new_subset][v][1] += dp[subset][k][1]
                elif(dp[new_subset][v][0] > dp[subset][k][0]+distance):
                    dp[new_subset][v] = [dp[subset][k][0]+distance, dp[subset][k][1]]


# for i,l in enumerate(dp): print(f'{bin(i)}:{l}')

ans = (INF, INF)
for v in range(building_n):
    if(graph_M[0][v][0]<=graph_M[v][0][0]): distance, time = graph_M[0][v][0], graph_M[0][v][1]
    else: distance, time = graph_M[v][0][0], graph_M[v][0][1]
    is_on_time = (dp[(2**building_n)-1][v][0]+distance<=time)
    if(is_on_time):
        if(dp[(2**building_n)-1][v][0]+distance==ans[0]):
            ans = [ans[0], ans[1]+dp[(2**building_n)-1][v][1]]
        elif(dp[(2**building_n)-1][v][0]+distance<ans[0]):
            ans = [dp[(2**building_n)-1][v][0]+distance, dp[(2**building_n)-1][v][1]]


if(ans[0]==INF): print('IMPOSSIBLE')
else: print(f'{ans[0]} {ans[1]}')