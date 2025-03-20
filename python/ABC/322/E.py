def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 動的計画法
import copy

N, K, P = ILI()
development_info = [[0 for _ in range(K+1)]]+[ILI() for _ in range(N)]
ans = float('inf')

# dp table の生成
dp_cost = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
dp_param = [[[0]*K for _ in range(N+1)] for _ in range(N+1)]
dp_flg = [[[True]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

# 初期値の代入
for i in range(1, N+1):
    dp_cost[1][i] = development_info[i][0]
    dp_param[1][i] = development_info[i][1:]
    dp_flg[1][i][i] = False

    judge = True
    param = dp_param[1][i]
    for n in range(K):
        if(param[n]<P):
            judge = False
    if(judge):
        ans = min(ans, dp_cost[1][i])

for i in range(2, N+1):
    for j in range(1, N+1):
        operation_cost = development_info[j][0]
        operation_param = development_info[j][1:]
        for k in range(1, N+1):
            cost = dp_cost[i][j]
        
            prev_cost = dp_cost[i-1][k]
            prev_param = dp_param[i-1][k].copy()
            prev_flg = dp_flg[i-1][k].copy()
            if(prev_flg[j] and prev_cost+operation_cost<cost):
                dp_cost[i][j] = prev_cost+operation_cost
                dp_param[i][j] = [prev_param[n]+operation_param[n] for n in range(K)]
                prev_flg[j] = False
                dp_flg[i][j] = prev_flg

                judge = True
                param = dp_param[i][j]
                for n in range(K):
                    if(param[n]<P):
                        judge = False
                if(judge):
                    ans = min(ans, dp_cost[i][j])

ans = -1 if(ans==float('inf')) else ans
print(ans)