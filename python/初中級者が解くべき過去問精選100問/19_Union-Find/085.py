# Union-Find

# Union-Findクラスを定義(参考：https://algo-method.com/descriptions/136)
from collections import defaultdict
class UnionFind():
    # オブジェクトが生成された時に実行される関数.nは要素数
    # uf_tree1 = UnionFind(n)とされた時に実行
    def __init__(self, n):
        self.parents = [-1]*n
        self.rank = [0]*n
        self.size = [1]*n
    # ---------------------------------------------------------------
    # これ以降はいわゆるメソッド。文字列.split(' ')とかと同じ
    # メソッドの引数にあるselfはオブジェクト自身を指す
    # つまり、s.split(), l.sort()でいうsやlのこと

    # xが属するグループの根を返す。
    def root(self, x):
        if(self.parents[x]<0):
            return x
        else:
            # 再帰的に根に向かって辿っていく
            self.parents[x] = self.root(self.parents[x]) # 辺の縮約
            return self.parents[x]
    
    # x, yが同じグループに属するかを判定
    def find(self, x, y):
        return self.root(x) == self.root(y)

    # x, yがそれぞれ所属する二つのグループ（Union-Find木）の結合を行う
    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        # x, yがすでに同じUnion-Find木の要素なら何もしない
        if(root_x==root_y):
            return False
        # yが含まれるUnion-Find木の高さの方が小さくなるようにする
        # yが含まれるUnion-Find木の高さ(rank) < xが含まれるUnion-Find木の高さ(rank)
        if(self.rank[root_x]<self.rank[root_y]):
            root_x, root_y = root_y, root_x
        # ノードyが含まれるUnion-Find木をノードxが含まれるUnion-Find木に結合
        self.parents[root_y] = root_x
        # 結合後のUnion-Find木の高さを調整
        if(self.rank[root_x]==self.rank[root_y]):
            self.rank[root_x]+=1
        # Union-Find木に含まれるノード数を更新
        self.size[root_x] += self.size[root_y]
        return True

# 問題部分
node_n, Q = list(map(int, input().split(' ')))
unionfind = UnionFind(node_n)
ans_l = []
for _ in range(Q):
    i, x, y = list(map(int, input().split(' ')))
    if(i==0):
        unionfind.union(x,y)
    else:
        ans = 1 if(unionfind.find(x,y)) else 0
        # ここでprint(ans)すると標準入力に割り込む形で出力されてしまったので、一旦格納。
        ans_l.append(ans)
for ans in ans_l:print(ans)