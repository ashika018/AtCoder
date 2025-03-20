# 累積和
row_n, col_n, K, total_assets = list(map(int, input().split(' ')))
map_M = [[0 for _ in range(col_n+1)]]+[[0]+list(map(int, input().split(' '))) for _ in range(row_n)]

# 累積和：complative
# complative_sum_M[i][j]：マス(1,1)~マス(i,j)の長方形の地価総額
complative_sum_M = [[0 for _ in range(col_n+1)] for _ in range(row_n+1)]
for i in range(1, row_n+1):
    for j in range(1, col_n+1):
        complative_sum_M[i][j] = map_M[i][j]+complative_sum_M[i-1][j]+complative_sum_M[i][j-1]-complative_sum_M[i-1][j-1]

# 全探索
# forの回数的には最悪、122,085,937回→それ以外の処理はかなり単純なので間に合っている？
ans = 0
for r_1 in range(1, row_n+1):
    for r_2 in range(r_1, row_n+1):
        for c_1 in range(1, col_n+1):
            for c_2 in range(c_1, col_n+1):
                total_LandValue = complative_sum_M[r_2][c_2] - complative_sum_M[r_1-1][c_2] - complative_sum_M[r_2][c_1-1] + complative_sum_M[r_1-1][c_1-1]
                block_n = (r_2-r_1+1)*(c_2-c_1+1)
                total_cost = total_LandValue + block_n*K
                if(total_assets>=total_cost): 
                    ans = max(ans, block_n)
print(ans)