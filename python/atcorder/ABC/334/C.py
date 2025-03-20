# 数学的考察
# 累積和

# 三角不等式より、すでに揃っている靴下は、組み替えないのが最適
# つまり、A1~Akの靴下を組み合わせて、奇妙さを最小にする

# kが偶数の時は小さい順に並べて、隣り合うもの同士を組み合わせれば良い
# kが奇数の時、どれか一つの要素を取り除き、奇妙さが最小になるものを全探索で求める
# ただし、普通に奇妙さの和を求めようとすると、O(N)かかり、全探索と合わせてO(N^2)になる
# 累積和で先に求めておく

N, K = list(map(int, input().split(' ')))
A_l = list(map(int, input().split(' ')))

if(K%2==0):
    ans = sum([A_l[i+1]-A_l[i] for i in range(0, len(A_l), 2)])
else:
    s = 0
    sum_odd_l = [0]
    # [0, A3-A2, 以前+(A5-A4), 以前+(A7-A6), ..., 以前+(Ak-Ak-1)]
    # Ak-Ak-1(kは奇数)までの総和を求めたいとき → sum_odd_l[k//2]
    for i in range(1, len(A_l), 2):
        s += A_l[i+1]-A_l[i]
        sum_odd_l.append(s)

    s = 0
    sum_even_l = [0]
    # [0, A2-A1, 以前+(A4-A3), 以前+(A6-A5), ..., 以前+(Ak-1-Ak-2)]
    # Ak-Ak-1(kは偶数)までの総和を求めたいとき → sum_odd_l[k//2]
    for i in range(0, len(A_l)-1, 2):
        s += A_l[i+1]-A_l[i]
        sum_even_l.append(s)

    # 全探索
    # A_iを含まずにペアをつくる
    ans = float('inf')
    for i in range(1, len(A_l)+1):
        # iが奇数のとき、A_iは奇数(下の例ではA5を抜く。i=5)
        # ペアとしては(A2-A1), (A4-A3), (A7-A6), (A9-A8), ..
        if(i%2==1):
            ans = min(ans, sum_even_l[(i-1)//2]+sum_odd_l[-1]-sum_odd_l[i//2])
        # iが偶数のとき、A_iは偶数(下の例ではA6を抜く。i=6)
        # ペアとしては(A2-A1), (A4-A3), (A7-A5), (A9-A8)
        else:
            ans = min(ans, sum_even_l[(i-2)//2]+A_l[i]-A_l[i-2]+sum_odd_l[-1]-sum_odd_l[(i+1)//2])

print(ans)

