# 深さ優先探索
# 深さ優先探索にはスタックを用いるケースと、再帰関数で記述するケースがある。
# スタックを用いる場合、https://qiita.com/ajim/items/e7303423644bd5129dfc を参照

from collections import deque

node_num = int(input())

def make_tree(node_num):
    d = {}
    for _ in range(node_num):
        l = list(map(int, input().split(' ')))
        if(l[1]==0): d[l[0]] = []
        else: d[l[0]] = l[2:]
    return d

tree_d = make_tree(node_num=node_num)

# 深さ優先探索(Depth First Search)
# DFS1 は再帰関数を使った実装
seen = [False]*node_num
discovery_times_l = [0]*node_num
completion_times_l = [0]*node_num
# outputに完了時刻をreturnする
def DFS1(node, time):
    print(node)
    next_nodes_l = tree_d[node]
    time += 1
    discovery_times_l[node-1] = time
    if(len(next_nodes_l) == 0):
        completion_times_l[node-1] = time+1
        return time+1
    else:
        for n_node in next_nodes_l:
            if(seen[n_node-1]): 
                completion_times_l[node-1] = completion_times_l[n_node-1]+1
            else:
                seen[n_node-1] = True
                completion_time = DFS1(n_node, time)+1
                completion_times_l[node-1] = completion_time
                
        return completion_time

f_node = 1
time = 0
t = DFS1(node=f_node, time=time)
print('~~~~~~~~~~~~~~~~~')
for i in range(node_num): print(f'{i+1} {discovery_times_l[i]} {completion_times_l[i]}')