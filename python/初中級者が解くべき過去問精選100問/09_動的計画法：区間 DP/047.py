# 動的計画法：区間 DP
# https://www2.ioi-jp.org/joi/2014/2015-ho/2015-ho-t2-review.pdf

# カットされたケーキの数N <= 2000
# JOI君が選ぶケーキの数 <= 1000
# 選べるケーキの数は一度に2つしかないので、全探索での計算量は<2**1000となりアウト。

# 途中までケーキを取った時のJOI君のスコアはそれ以降のスコアに影響を及ぼさないことから、DPっぽいと感じる
# （重要）つまり、残り1つの状態からJOI君が獲得できる最大スコア→残り二つの状態からJOI君が獲得できる最大スコア→...→残りN個の状態からJOI君が獲得できる最大スコアを計算していく。

# そもそもN<=2000より、O(N^2)くらいが目安

# また、ここでdp[L][R]は残った扇状のケーキを直線にしたもが[L,R]である状況から始めた時の、JOI君が得るスコアの最大値とする。

N = int(input())
A_l = [int(input()) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for d in range(1, N+1): # dは残りのケーキの数。残り1つ→残り2つ→...→のこりNつと増加していく
    for L in range(N):
        R = (L+d)%N
        # JOI君のターン
        if((N-d)%2==0):
            dp[L][R] = max(dp[(L+1)%N][R]+A_l[L], dp[L][R-1]+A_l[R-1])
        # IOIさんのターン
        else:
            if(A_l[L]>A_l[R-1]): dp[L][R] = dp[(L+1)%N][R]
            else: dp[L][R] = dp[L][R-1]

# for l in dp: print(l)
print(max([dp[i][i] for i in range(N)]))