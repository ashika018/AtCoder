# 最小全域木問題
import heapq
node_n, E_n = list(map(int, input().split(' ')))

# edges_l = [[]]*node_n はだめでした。
edges_l = [[] for _ in range(node_n)]

for _ in range(E_n):
    node1, node2, cost = list(map(int, input().split(' ')))
    edges_l[node1].append((cost, node2))
    edges_l[node2].append((cost, node1))

def prim_algorithm():
    f_node, total_cost = 0, 0
    # node_flg[node]==False : node未確定
    # node_flg[node]==True : node確定済
    node_flg = [True]+[False for _ in range(node_n-1)]
    # Vをheapとして使いたい時は、pushもこの方法じゃなきゃだめ。
    # https://github.com/python/cpython/blob/3.12/Lib/heapq.py のコメントにusageってところがある。
    V = []
    for t in edges_l[f_node]: heapq.heappush(V, t)
    while V:
        # なぜか今回はV=[(a, b)]のaの値が最小となるタブルがheappopで抽出された。なぜ。
        cost, min_node = heapq.heappop(V)
        if(node_flg[min_node]): continue
        node_flg[min_node] = True
        total_cost += cost
        n_nodes_l = edges_l[min_node]
        
        for n_cost, n_node in n_nodes_l:
            if(node_flg[n_node]): continue
            heapq.heappush(V, (n_cost, n_node))
    return total_cost

print(prim_algorithm())