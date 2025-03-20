# 累積和
city_n, train_n, Q = list(map(int, input().split(' ')))

# train_M[i][j]: 始点=city_i、終点=city_jの電車の本数
train_M = [[0 for _ in range(city_n+1)] for _ in range(city_n+1)]
for _ in range(train_n):
    L_i, R_i = list(map(int, input().split(' ')))
    train_M[L_i][R_i] += 1

# 累積和：complative_sum
# complative_sum_M[i][j]：city_i<=始点<=終点<=city_jを満たす電車の本数
# matrixの周りを0で埋めておくことで、indexをはみ出ないようにする
complative_sum_M = [[0 for _ in range(city_n+2)] for _ in range(city_n+2)]
for l in range(city_n, 0, -1):
    for r in range(1, city_n+1):
        complative_sum_M[l][r] = train_M[l][r]+complative_sum_M[l+1][r]+complative_sum_M[l][r-1]-complative_sum_M[l+1][r-1]

# クエリに答えていく
for _ in range(Q):
    city1, city2 = list(map(int, input().split(' ')))
    print(complative_sum_M[city1][city2])