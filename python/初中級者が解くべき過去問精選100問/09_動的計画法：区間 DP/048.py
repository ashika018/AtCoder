# 動的計画法：区間 DP

# https://kakedashi-engineer.appspot.com/2020/06/17/aoj1611/
# https://kutimoti.hatenablog.com/entry/2018/03/10/220819
# この二つのサイトを参考にした。正味、自分ノート見るべし。

block_n = int(input())
B_l = list(map(int, input().split(' ')))

dp = [[0]*block_n for _ in range(block_n)]

for d in range(1, block_n):
    for L in range(block_n-d):
        R = L+d
        if((dp[L+1][R-1]==R-L-1) and (abs(B_l[L]-B_l[R])<=1)): 
            dp[L][R] = 2+dp[L+1][R-1]
        else: 
            for k in range(L+1,R): dp[L][R] = max(dp[L][R], dp[L][k]+dp[k+1][R])

# for l in dp: print(l)
print(dp[0][block_n-1])