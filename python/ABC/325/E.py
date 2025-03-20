def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


# 社用車→電車の乗り換えのみ可能
# 社用車で都市1→都市i(i=1,2,..,N)に移動し、電車で都市i→都市Nに移動することを考える
# 都市1から都市iまでの最短経路は、ダイクストラ法でO(N^2 + Nlog(N^2)) = O(N^2)で求められる
# 都市iから都市Nまでの最短経路は、都市Nから都市iへの最短経路と考えることで上と同様に考えることができる

import heapq

N, A, B, C = ILI()
graph_M = [ILI() for _ in range(N)]
INF = float('inf')

# ダイクストラ法
# V = [(スタートするノード番号, ノードまでの距離)]
# タプルのリストをheappopすると、タプルの二つ目の要素の中で最小のものを持つやつがpopされる。
def dijkstra(graph_M, start_node, mode):
    INF = float('inf')
    distance_d = dict([(i, INF) for i in range(1, N+1)])
    V = [(start_node, 0)]

    # Vが空になるまで。
    while V:
        # 距離が最小の頂点を取り出す
        node, distance = heapq.heappop(V)

        # すでにより短いパスが見つかっている場合は何もしない
        if(distance>distance_d[node]): continue

        # 隣接するノードの最短経路を更新
        for i, D in enumerate(graph_M[node-1]):
            to_node = i+1
            if(mode=='car'):
                between_dis = A*D
            else:
                between_dis = B*D+C if(D!=0) else 0
            # NG : distance_d[to_node] = min(distance+between_dis, distance_d[to_node])
            if(distance+between_dis<distance_d[to_node]):
                distance_d[to_node] = distance+between_dis
                heapq.heappush(V, (to_node, distance_d[to_node]))

    return distance_d

# 都市1から各都市までの社用車での移動について
car_d = dijkstra(graph_M=graph_M, start_node=1, mode='car')
# 都市Nから各都市までの電車での移動について
train_d = dijkstra(graph_M=graph_M, start_node=N, mode='train')

ans = INF
for city_i in range(1, N+1):
    ans = min(ans, car_d[city_i]+train_d[city_i])

print(ans)
