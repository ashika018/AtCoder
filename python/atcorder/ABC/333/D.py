def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 1を根とする木とみなす
# 1を親にもつノードを根とする部分木の辺の数を数える
# 各部分木の辺の数の中で1番大きいもの以外を足し合わせて、最後に1を足したら答え
# UnionFindで実装する

class UnionFind():
    def __init__(self,node_n):
        self.parents = [-1]*node_n
        self.size = [1]*node_n
        self.rank = [0]*node_n
        self.group_n = node_n
    
    # 与えられたノードの根を返す
    def root(self, node1):
        if(self.parents[node1]<0): 
            return node1
        else:
            self.parents[node1] = self.root(self.parents[node1]) # 辺の縮約
            return self.parents[node1]
    
    # 二つのノードが同じグループに含まれているかを判断
    def find(self, node1, node2):
        return self.root(node1)==self.root(node2)
    
    # 二つのノードがそれぞれ含まれるグループを併合する関数
    def union(self, node1, node2):
        root1, root2 = self.root(node1), self.root(node2)
        if(root1==root2): 
            return False
        else:
            if(self.rank[root1]<self.rank[root2]):
                root1, root2 = root2, root1 # root2の方がランクが低くなるようにする
            self.parents[root2] = root1
            self.group_n -= 1
            if(self.rank[root1]==self.rank[root2]):
                self.rank[root1] += 1
            self.size[root1] += self.size[root2]
            return True

node_n = II()
unionfind = UnionFind(node_n)

# UnionFind木を生成していく。（この時、頂点1への辺はまだ考えない）
for _ in range(node_n-1):
    node1, node2 = list(map(lambda x: x - 1, ILI()))
    # 頂点1を繋ぐ辺の場合はスキップ
    if(node1==0): continue
    unionfind.union(node1, node2)

# 各グループに含まれるノード数-1がその部分木に含まれる辺の数
edges_l = []
for i, parent in enumerate(unionfind.parents):
    # 部分木の根であるかどうか判定。(頂点1も除外)
    if(parent<0 and i!=0):
        edges_l.append(unionfind.size[i]-1)

edges_l.sort()
ans = 0+len(edges_l) # 頂点1への辺の数=unionfindに格納されたグループ数
for i in range(len(edges_l)-1):
    ans += edges_l[i]

print(ans)
