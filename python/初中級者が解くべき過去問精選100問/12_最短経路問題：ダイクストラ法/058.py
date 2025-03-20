# 最短経路問題：ダイクストラ法
# PyPyだとMLEしてしまうが、CpythonだとACできる。
# 実行制限時間が10secと長めなので、Cpythonでも余裕
import heapq
from collections import deque

# 入力のインプット
city_n, road_n, zombie_city_n, S = list(map(int, input().split(' ')))
safe_city_hotel_fee, dangerous_city_hotel_fee = list(map(int, input().split(' ')))
zombie_city_l = [int(input()) for _ in range(zombie_city_n)]
road_l = [[] for _ in range(city_n+1)]
for _ in range(road_n):
    city1, city2 = list(map(int, input().split(' ')))
    road_l[city1].append(city2)
    road_l[city2].append(city1)

# 幅優先探索で「ゾンビに支配されている街:0」「危険な街:1」「安全な街:2」のラベリングを行う
def BFS(zombie_city_l):
    city_label_l = [2 for _ in range(city_n+1)]
    for f_node in zombie_city_l:
        distance_l = [-1 for _ in range(city_n+1)]
        # 探索する最初のノードを追加
        queue = deque([])
        queue.append(f_node)
        city_label_l[f_node] = 0
        distance_l[f_node] = 0
        # 幅優先探索する
        while queue:
            node = queue.popleft()
            next_node_l = road_l[node]
            for n_node in next_node_l:
                if(distance_l[n_node]>0): continue
                distance_l[n_node] = distance_l[node]+1
                if(distance_l[n_node]>S): continue
                queue.append(n_node)
                if(city_label_l[n_node]==2): city_label_l[n_node]=1
                
    return city_label_l

# ダイクストラ法で街１→街Nの単一始点最短経路問題を解く
# V = [(街i, 街iに到着するまでにかかるコスト)]
def dijkstra(start, goal):
    cost_l = [float('inf') for _ in range(city_n+1)]
    # V = [(start, 0)]
    V = [(0, start)]
    while V:
        # node, cost = heapq.heappop(V)
        cost, node = heapq.heappop(V)
        if(cost>cost_l[node]): continue
        for n_node in road_l[node]:
            if(city_label_l[n_node]==0): continue
            hotel_fee = safe_city_hotel_fee if(city_label_l[node]==2) else dangerous_city_hotel_fee
            if(cost+hotel_fee<cost_l[n_node]): 
                cost_l[n_node] = cost+hotel_fee
                # heapq.heappush(V, (n_node, cost_l[n_node]))
                heapq.heappush(V, (cost_l[n_node], n_node))
    # 街1では宿泊しないので、街1の代金は引いておく
    cost_city1 = safe_city_hotel_fee if(city_label_l[1]==2) else dangerous_city_hotel_fee
    return cost_l[goal] - cost_city1

city_label_l = BFS(zombie_city_l=zombie_city_l)
ans = dijkstra(1, city_n)
print(ans)

