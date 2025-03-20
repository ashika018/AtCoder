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

iland_n, bridge_n = list(map(int, input().split(' ')))
collaposed_bridges = [tuple(map(int, input().split(' '))) for _ in range(bridge_n)]

# 崩壊順を逆順回すことで、ノード間にリンクを作っていく。
unionfind = UnionFind(iland_n)
ans_l_inversed = [0]
for t in collaposed_bridges[::-1]:
    iland1, iland2 = t
    iland1 -= 1
    iland2 -= 1
    if(not unionfind.find(iland1, iland2)):
        root1, root2 = unionfind.root(iland1), unionfind.root(iland2)
        size1, size2 = unionfind.size[root1], unionfind.size[root2]
        ans_l_inversed.append(ans_l_inversed[-1]+size1*size2)
        unionfind.union(iland1, iland2)
    else:
        ans_l_inversed.append(ans_l_inversed[-1])

# 答えの出力
total_combinations = iland_n*(iland_n-1)//2
ans_l = ans_l_inversed[::-1]
for ans in ans_l[1:]: 
    print(total_combinations - ans)