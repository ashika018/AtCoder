def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# (Ai,Bi)をエッジで繋ぐ。
# どこか一つの点を1or0で定めると、辺で繋がっている頂点の値も決まる
# グラフ探索アルゴリズムDFS or BFSで頂点の値を決めていく
# すでに値が決まっている頂点に訪れた際は、隣の頂点と矛盾しないかだけ確認すれば良い
# 全ての頂点が変で繋がっている訳ではないので、全ての頂点からグラフ探索を行う。（ただし、すでにその頂点の値が決まっていたら、その頂点は飛ばす）

import sys
# 再帰の深さ制限を増やす
sys.setrecursionlimit(int(1E+7)) 

N, M = ILI()
A_l = ILI()
B_l = ILI()

# グラフの作成
graph_M = [[] for _ in range(N+1)]
for i in range(M):
    a, b = A_l[i], B_l[i]
    graph_M[a].append(b)
    graph_M[b].append(a)

# 各ノードの値（0 or 1）を格納
node_values_l = [-1 for _ in range(N+1)]

# nodeの含まれるgraphが良い数列ならTrue, 悪い数列ならFalseを返すDFS
def DFS(node, value):
    # ノードに訪問済みのとき
    if(node_values_l[node]!=-1):
        # 頂点の値が矛盾するとき
        if(node_values_l[node]!=value):
            return False
        if(node_values_l[node]==value):
            return True
    # 未探索のノードであるとき
    else:
        node_values_l[node] = value
        n_nodes_l = graph_M[node]
        judge = True
        for n_node in n_nodes_l:
            n_value = 1 if(value==0) else 0
            judge = judge and DFS(n_node, n_value)
        return judge

judge = True
for node_i in range(1, N+1):
    if(node_values_l[node_i]==-1):
        judge = judge and DFS(node=node_i, value=0)

ans = 'Yes' if(judge) else 'No'
print(ans)