# 深さ優先探索

# DFSは、操作jを行う際に用いる。
# 問題分に木構造と書いてあるので、子はただ一つの親を持つ。
# 木構造であることから、visited_lやseen_lなどは必要なしだが、今回は問題文の不備により必要。


# デフォルト値だと小さすぎるので、再帰処理の上限を引き上げる
import sys
sys.setrecursionlimit(int(1E+7))

node_num, num_operations = list(map(int, input().split(' ')))
def make_tree():
    d = dict([(i,  []) for i in range(1, 1+node_num)])
    for _ in range(node_num-1):
        a, b = list(map(int, input().split(' ')))
        d[a].append(b)
        # 問題文では、どちらが親のノードか記載されていないので、(a=親,b=子)と(a=子,b=親)のどちらのパターンも入れておく
        # 木構造であるので根さえわかれば、visited_lを駆使して正しく探索できる
        d[b].append(a)
    return d

tree_d = make_tree()
visited_l = [False]*node_num
value_l = [0]*node_num
for _ in range(num_operations):
    node, x = list(map(int, input().split(' ')))
    value_l[node-1] += x

def DFS(f_node):
    visited_l[f_node-1] = True
    if(len(tree_d[f_node])==0): return
    else:
        n_nodes_l = tree_d[f_node]
        for n_node in n_nodes_l:
            if(visited_l[n_node-1]): continue
            else:
                value_l[n_node-1] += value_l[f_node-1]
                _ = DFS(n_node)

_ = DFS(1)

print(' '.join(list(map(str, value_l))))



