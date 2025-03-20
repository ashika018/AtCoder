# 最短経路問題：ダイクストラ法

node_n, edge_n, start_node = list(map(int, input().split(' ')))
graph_d = {}
for _ in range(edge_n):
    from_node,to_node,distance = list(map(int, input().split(' ')))
    if(from_node not in graph_d): graph_d[from_node] = [(to_node, distance)]
    else: graph_d[from_node].append((to_node, distance))

V = [i for i in range(node_n)]
# S = []

# 各頂点までの最短経路を保存し、更新していく辞書
# 始点だけは0にしておく
INF = float('inf')
shortest_path = dict([(i, INF) for i in range(node_n)])
shortest_path[start_node] = 0

ans_d ={}
while(True):
    # 始点からの経路が判明している頂点のうち始点からの距離が最小となる頂点vを取り出す
    from_node_d = INF
    for node in V:
        # ここの<=がキモ。そもそもパスが存在しない時にINF同士の比較をしないといけない。
        # <だと、INF同士の比較だとFALSEになって都合が悪い。
        if(shortest_path[node]<=from_node_d): 
            from_node = node
            from_node_d = shortest_path[from_node]
    # V\SをVから要素を取り除いていくことで再現
    V.remove(from_node)
    ans_d[from_node] = from_node_d

    if(len(V)==0): break
    for node_tuple in graph_d[from_node]:
        to_node, from_to_distance = node_tuple
        shortest_path[to_node] = min(shortest_path[to_node], from_node_d+from_to_distance)

d = dict(sorted(ans_d.items()))
for ans in d.values(): print(ans)

