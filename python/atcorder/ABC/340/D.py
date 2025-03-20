def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 適当にダイクストラをするとTLEした
# heapqに(stage, cost)を格納していたのが不味く、(cost, stage)にしたところ計算時間が1/3に、、！

import heapq

N = II()

# road_l[i]: （ステージiから行くことのできるステージ, 所要時間）
road_l = [[] for _ in range(N+1)]
for stage in range(1, N):
    A, B, X = ILI()
    road_l[stage].append((stage+1, A))
    road_l[stage].append((X, B))

def dijkstra(road_l, start_stage=1, goal_stage=N):
    INF = float('inf')
    cost_d = dict([(i,INF) for i in range(1, N+1)])
    # V = [(start_stage, 0)]
    V = [(0, start_stage)]

    while V:
        # stage, cost = heapq.heappop(V)
        cost, stage = heapq.heappop(V)

        if(cost>cost_d[stage]): continue

        for n_stage, between_cost in road_l[stage]:
            if(cost+between_cost<cost_d[n_stage]):
                cost_d[n_stage] = cost+between_cost
                # heapq.heappush(V, (n_stage, cost_d[n_stage]))
                heapq.heappush(V, (cost_d[n_stage], n_stage))
    
    return cost_d[goal_stage]

print(dijkstra(road_l=road_l))
