# 最短経路問題：ダイクストラ法
from collections import deque
import heapq

city_n, road_n = list(map(int, input().split(' ')))
taxi_company_l = [[0, 0]]+[list(map(int, input().split(' '))) for _ in range(city_n)]
road_l = [[] for _ in range(city_n+1)]
for _ in range(road_n):
    city1, city2 = list(map(int, input().split(' ')))
    road_l[city1].append(city2)
    road_l[city2].append(city1)

# 街kからタクシーに乗って、移動できる街を探索
def BFS(city_k):
    _, max_length = taxi_company_l[city_k]
    available_city = []
    distance_from_city = [-1 for _ in range(city_n+1)]
    queue = deque([])
    queue.append(city_k)
    distance_from_city[city_k] = 0
    while queue:
        node = queue.popleft()
        for n_node in road_l[node]:
            if(distance_from_city[n_node]>=0): continue
            distance_from_city[n_node] = 1+distance_from_city[node]
            if(distance_from_city[n_node]>max_length): continue
            queue.append(n_node)
            available_city.append(n_node)
    return available_city

avaliable_city_l = [[0]]
for city in range(1, city_n+1):
    avaliable_city_l.append(BFS(city))

# ダイクストラ：街1からそれぞれの街への最短経路を探索
# V = [(city_k, city_k到達までにかかるコスト)]
def dijkstra(start, goal):
    cost_l = [float('inf') for _ in range(city_n+1)]
    V = [(0, start)]
    # V = [(start, 0)]
    while V:
        cost, city = heapq.heappop(V)
        # city, cost = heapq.heappop(V)
        if(cost>cost_l[city]): continue
        next_city_l = avaliable_city_l[city]
        for n_city in next_city_l:
            taxi_fee = taxi_company_l[city][0]
            if(cost+taxi_fee<cost_l[n_city]):
                cost_l[n_city] = cost+taxi_fee
                heapq.heappush(V, (cost_l[n_city], n_city))
                # heapq.heappush(V, (n_city, cost_l[n_city]))
    return cost_l[goal]

print(dijkstra(1, city_n))