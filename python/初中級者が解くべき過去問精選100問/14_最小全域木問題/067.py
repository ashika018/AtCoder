# 14_最小全域木問題
import heapq

N = int(input())
x_d, y_d = {}, {}
for i in range(1, N+1):
    xi, yi = list(map(int, input().split(' ')))
    x_d[i] = xi
    y_d[i] = yi
# ソートする
x_d = dict(sorted(x_d.items(), key = lambda x: x[1]))
y_d = dict(sorted(y_d.items(), key = lambda y: y[1]))

# 最低限のノードを辺で繋ぎ、コストも入れておく
x_city = list(x_d.keys())
y_city = list(y_d.keys())
x_l = list(x_d.values())
y_l = list(y_d.values())
# edges_l[from_city] = (cost, to_city)
edges_l = [[] for _ in range(N+1)]
for i in range(0, N-1):
    edges_l[x_city[i]].append((abs(x_l[i]-x_l[i+1]), x_city[i+1]))
    edges_l[x_city[i+1]].append((abs(x_l[i]-x_l[i+1]), x_city[i]))
    edges_l[y_city[i]].append((abs(y_l[i]-y_l[i+1]), y_city[i+1]))
    edges_l[y_city[i+1]].append((abs(y_l[i]-y_l[i+1]), y_city[i]))

# 最小全域木の計算（プリム法）
def prim_algorithm(f_node=1, total_cost=0):
    node_flg = [False for _ in range(N+1)]
    node_flg[f_node] = True
    V = []
    for t in edges_l[f_node]: heapq.heappush(V, t)
    while V:
        cost, city = heapq.heappop(V)
        if(node_flg[city]): continue
        total_cost += cost
        node_flg[city] = True
        for n_cost, n_city in edges_l[city]:
            if(node_flg[n_city]): continue
            heapq.heappush(V, (n_cost, n_city))
    return total_cost

print(prim_algorithm(f_node=1, total_cost=0))