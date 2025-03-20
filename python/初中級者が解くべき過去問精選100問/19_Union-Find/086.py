# Union-Find

class UnionFind():
    def __init__(self, node_n):
        self.parents = [-1]*node_n
        self.size = [1]*node_n
        self.rank = [0]*node_n
    
    def root(self, x):
        if(self.parents[x]<0): return x
        else:
            self.parents[x] = self.root(self.parents[x]) # 辺の縮約
            return self.parents[x]

    def find(self, x, y):
        return self.root(x)==self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if(root_x==root_y): return False
        else:
            if(self.rank[root_x]<self.rank[root_y]):
                root_x, root_y = root_y, root_x
            self.parents[root_y] = root_x
            if(self.rank[root_x]==self.rank[root_y]):
                self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
            return True

node_n, edge_n = list(map(int, input().split(' ')))
edges_l = [tuple(map(int, input().split(' '))) for _ in range(edge_n)]

ans = 0
for i in range(edge_n):
    # edge_iを含まない場合の無効連結グラフをもとに、UnionFindを生成
    union_find = UnionFind(node_n)
    tmp_edges_l = edges_l[0:i] + edges_l[i+1:]
    for t in tmp_edges_l:
        node1, node2 = t[0]-1, t[1]-1
        union_find.union(node1, node2)
    # 全てのノードが同じグループに属するか判断
    for node1 in range(node_n-1):
        node2 = node1 + 1
        if(not union_find.find(node1, node2)):
            ans += 1
            break
print(ans)