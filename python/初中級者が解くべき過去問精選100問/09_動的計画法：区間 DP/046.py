# 動的計画法：区間 DP
M_num = int(input())
M_info = [list(map(int, input().split(' '))) for _ in range(M_num)]

dp = [[10**10]*M_num for _ in range(M_num)]
# n行n列（対角成分）は0
for i in range(M_num): dp[i][i] = 0

for delta in range(1, M_num): # lとrの差分。差分は1からM_num-1まで
    for l in range(M_num-delta):
        r = l+delta
        for k in range(l, r):
            # dp[k+1][r]であることに注意
            # 
            dp[l][r] = min(dp[l][r], dp[l][k] + (M_info[l][0]*M_info[k][1]*M_info[r][1]) + dp[k+1][r])

print(dp[0][-1])