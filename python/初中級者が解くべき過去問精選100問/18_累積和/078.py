# 累積和
row_n, col_n = list(map(int, input().split(' ')))
Q = int(input())
map_M = [['x']*(col_n+1)]+[['x']+list(input()) for _ in range(row_n)]
Q_l = [list(map(int, input().split(' '))) for _ in range(Q)]

# 累積和：complative_sum
# complative_sum_M[i][j]：(1,1)と(i,j)によって構成される長方形のグリッド内に含まれる'I','O','J'の数
complative_sum_M=[[[0, 0, 0] for _ in range(col_n+1)] for _ in range(row_n+1)]
for r in range(1, row_n+1):
    for c in range(1, col_n+1):
        if(map_M[r][c]=='I'): I, O, J = 1, 0, 0
        elif(map_M[r][c]=='O'): I, O, J = 0, 1, 0
        else: I, O, J = 0, 0, 1
        I1, O1, J1 = complative_sum_M[r-1][c]
        I2, O2, J2 = complative_sum_M[r][c-1]
        I3, O3, J3 = complative_sum_M[r-1][c-1]
        complative_sum_M[r][c] = [I+I1+I2-I3, O+O1+O2-O3, J+J1+J2-J3]

# クエリに答えていく
for l in Q_l:
    r1,c1,r2,c2 = l
    I1, O1, J1 = complative_sum_M[r2][c2]
    I2, O2, J2 = complative_sum_M[r1-1][c2]
    I3, O3, J3 = complative_sum_M[r2][c1-1]
    I4, O4, J4 = complative_sum_M[r1-1][c1-1]
    print(f'{J1-J2-J3+J4} {O1-O2-O3+O4} {I1-I2-I3+I4}')
