# 逆元のmodとUnion-Find

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

# ax+by=gcd(a,b)の解(x,y)とgcd(a,b)を求める関数
def ex_euclid(a, b):
    if(b==0):
        return(1, 0, a)
    else:
        x_, y_, gcd = ex_euclid(b, a%b)
        return(y_, x_-(a//b)*y_, gcd)

row, col = list(map(int, input().split(' ')))
grid = [["0" for _ in range(col+2)]] + [['0']+list(input())+['0'] for _ in range(row)] + [["0" for _ in range(col+2)]]

# unionfindの生成と赤マスの数え上げ
unionfind = (UnionFind(row*col))
red_l = []
for i in range(1, row+1):
    for j in range(1, col+1):
        # i行j列がgreenの時
        if(grid[i][j]=='#'):
            for d in [(0,1), (1,0)]:
                dr,dc = d
                if(grid[i+dr][j+dc]=='#'):
                    # i行j列のノード番号は、col*(i-1)+j-1とする。（行方向に0,1,2,...と番号を振る ）
                    node1, node2 = col*(i-1)+j-1, col*(i+dr-1)+j+dc-1
                    unionfind.union(node1, node2)
        else:
            red_l.append((i,j))

# 各赤マスを緑に塗り替えた時の連結成分を足し算していく
total_groups = 0
red_n = len(red_l)
for t in red_l:
    i, j = t
    tmp = 0 #i行j列のマスを赤→緑にした時に、結合されるグループ数
    root_l = []
    for d in [(-1,0),(1,0),(0,1),(0,-1)]:
        dr, dc =d
        if(grid[i+dr][j+dc]=='#'):
            node = col*(i+dr-1)+j+dc-1
            root = unionfind.root(node)
            # このマスが含まれるグループを、すでに結合していないか確認
            if(root not in root_l):
                tmp += 1
                root_l.append(root)
    total_groups += unionfind.group_n - red_n + 1 - tmp

MOD = 998244353
red_n_inverse, _, _ = ex_euclid(red_n, MOD)
ans = (total_groups%MOD) * (red_n_inverse%MOD)
print(ans%MOD)