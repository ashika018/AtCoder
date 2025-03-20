# 幅優先探索

from collections import deque

node_num = int(input())

# まずはデータの構造を把握（木構造なのかネットワークなのか、有向グラフか無向グラフか）し、データ構造を作る
# データ構造によっては、リストでグラフを表現することもある
# Nodeクラスを作ることもあるみたい
def make_tree():
    d = {}
    for _ in range(node_num):
        l = list(map(int, input().split(' ')))
        if(l[1]==0): d[l[0]] = []
        else: d[l[0]] = l[2:]
    return d

tree_d = make_tree()
flag = [False]*node_num # あるノードを通過したかどうかを判断
seen = [0]*node_num # あるノードを見たかどうかの判断

# 幅優先探索(Breadth First Search)の実装
# 幅優先探索は再帰関数を使うことはない。
def BFS(f_node):
    queue = deque([])
    ans_d = dict([(node, -1) for node in range(1, node_num+1)])
    # 探索の最初のノードをあらかじめキューに入れておく
    queue.append(f_node)
    ans_d[f_node] = 0
    
    # 探索の開始
    while queue:
        node = queue.popleft()
        if(flag[node-1]): continue
        else:
            flag[node-1] = True
            next_node_l = tree_d[node]
            for n_node in next_node_l:
                queue.append(n_node)
                if(seen[n_node-1]): continue
                else:
                    ans_d[n_node] = ans_d[node]+1
                    seen[n_node-1] = 1
    return ans_d

ans_d = BFS(1)
for node, d in ans_d.items(): print(f'{node} {d}')