
# 参考：https://qiita.com/takayg1/items/c811bd07c21923d7ec69

class segTree:
    # init_series:最初の数列, f:モノイド, e:単位元
    def __init__(self, init_series, f, e):
        n = len(init_series)
        self.f = f
        self.e = e
        self.num = 1 << (n-1).bit_length()
        # 数列の値を葉に格納する
        self.tree = [e]*(2*self.num)
        for i in range(n):
            self.tree[self.num+i] = init_series[i]
        # ボトムアップに計算する
        for i in range(self.num-1, 0, -1):
            l, r = self.tree[2*i], self.tree[2*i+1]
            self.tree[i] = self.f(l,r)

    # 値の更新を行う
    # k番目の値をxに更新
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.f(self.tree[k], self.tree[k^1])
            k >>= 1

    # 選択された範囲のモノイド演算
    def query(self, l, r):
        res = self.e
        l += self.num
        r += self.num
        while l<r:
            if(l&1):
                res = self.f(res, self.tree[l])
                l+=1
            if(r&1):
                res = self.f(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res



class segTree:
    # コンストラクタ（クラスから新しいオブジェクトを生成する際に呼び出される特殊なメソッド）
    # ここでは、セグメント木を生成する
    # init_series:最初の数列, f:モノイド, e:単位元
    def __init__(self, init_series, f, e):
        n = len(init_series)
        self.f = f
        self.e = e
        # num: n以上の最小の2の冪乗(n=10の時、self.num=16)
        # bit_length()はint型をbitに直した時の長さを求める。
        # n=10の時、n-1=9, bit(9)=1001 → 9.bit_length()=4
        # 1<<4は1を4bit分左シフトさせるので、self.num=b10000=2**4=16
        self.num = 1 << (n-1).bit_length()
        # 多分(2*self.num - 1)で十分な気がする→0番目のインデックスを使わないみたい
        self.tree = [e]*(2*self.num)
        # 数列の値を葉に格納する
        for i in range(n):
            self.tree[self.num+i] = init_series[i]
        # ボトムアップに計算する
        for i in range(self.num-1, 0, -1):
            l, r = self.tree[2*i], self.tree[2*i+1]
            self.tree[i] = self.f(l,r)

    # 値の更新を行う
    # k番目の値をxに更新
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k>1:
            # (k>>1)==(k//2)、k^1はkの隣のノード指定
            # ^: 排他的論理和（(1,0)→１, (0,1)→1, (0,0)→0, (1,1)→0）
            self.tree[k>>1] = self.f(self.tree[k], self.tree[k^1])
            k >>= 1

    # 選択された範囲のモノイド演算
    def query(self, l, r):
        res = self.e
        l += self.num
        r += self.num
        while l<r:
            # lの最下位bitが1、つまりlが奇数ならば
            if(l&1):
                res = self.f(res, self.tree[l])
                l+=1
            if(r&1):
                res = self.f(res, self.tree[r-1])
            # 
            l >>= 1
            r >>= 1
        return res