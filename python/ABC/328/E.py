def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 頂点の数Nは最大で8個であり、辺の数は最大でN(N-1)/2本であるから、辺の数は最大で8*7/2 = 28本である
# 全域木の辺の数はN-1本であるから、考えられる組み合わせのパターン数は M C (N-1)本 < 28C7 = 1,184,040
# つまり、全ての全域木のパターンを全探索しても間に合う！
# N-1本の辺が全域木となっているかの判定にUnion-Findを使う（各頂点のrootが同じ）
from itertools import combinations

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

N, M, K = ILI()
edges_l = [ILI() for _ in range(M)]

ans = float('inf')
for combination_l in combinations(edges_l, N-1):
    tmp = 0
    unionfind = UnionFind(N)
    for comb in combination_l:
        node1, node2, cost = comb
        unionfind.union(node1-1, node2-1)
        tmp += cost
        tmp %= K
    
    # この木が全域木であるかどうかを判定
    d = {}
    for node in range(N):
        root = unionfind.root(node)
        if(root in d): d[root] += 1
        else: d[root] = 1
    is_tree = (len(d)==1)

    # ansの更新
    if(is_tree):
        ans = min(ans, tmp%K)
print(ans)