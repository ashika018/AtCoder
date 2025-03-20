# 最短経路問題：ダイクストラ法
import heapq

# V = [(スタートするノード番号, ノードまでの距離)]
# タプルのリストをheappopすると、タプルの二つ目の要素の中で最小のものを持つやつがpopされる。
def dijkstra(graph_d, start_node, goal_node):
    INF = float('inf')
    distance_d = dict([(i, INF) for i in range(1, iland_n+1)])
    # V = [(start_node, 0)]
    V = [(0, start_node)]

    # Vが空になるまで。
    while V:
        # 距離が最小の頂点を取り出す
        # node, distance = heapq.heappop(V)
        distance, node = heapq.heappop(V)

        # すでにより短いパスが見つかっている場合は何もしない
        if(distance>distance_d[node]): continue

        # 移れるノードがない場合は何もしない
        if(node not in graph_d.keys()): continue 

        # 隣接するノードの最短経路を更新
        for node_tuple in graph_d[node]:
            to_node, between_dis = node_tuple
            # NG : distance_d[to_node] = min(distance+between_dis, distance_d[to_node])
            if(distance+between_dis<distance_d[to_node]):
                distance_d[to_node] = distance+between_dis
                # heapq.heappush(V, (to_node, distance_d[to_node]))
                heapq.heappush(V, (distance_d[to_node], to_node))

    return distance_d[goal_node] if(distance_d[goal_node]<INF) else -1


iland_n, k = list(map(int, input().split(' ')))
graph_d = {}
ans_l = []

# 実行部分
for _ in range(k):
    l = list(map(int, input().split(' ')))
    # 最短経路の追加
    if(l[0]==0):
        _, start, goal = l
        ans_l.append(dijkstra(graph_d, start, goal))
    # 経路の更新
    if(l[0]==1):
        _, node1, node2, distance = l
        if(node1 not in graph_d.keys()): graph_d[node1]=[(node2, distance)]
        else: graph_d[node1].append((node2, distance))
        if(node2 not in graph_d.keys()): graph_d[node2]=[(node1, distance)]
        else: graph_d[node2].append((node1, distance))

for ans in ans_l: print(ans)