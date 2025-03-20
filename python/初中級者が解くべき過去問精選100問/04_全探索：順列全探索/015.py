# 全探索：順列全探索
# N個の街の周り方のパターンはN!通り。これを全探索する
import itertools

city_num = int(input())
city_location_l = [list(map(int, input().split(' '))) for _ in range(city_num)]


# 階乗の計算
def factorial_recursive(n):
    if(n==0): return 1
    else: return n*factorial_recursive(n-1)


distance = 0
# 順列を生成
for permuted_tuple in itertools.permutations(city_location_l):
    x_a, y_a = permuted_tuple[0]
    for city_location in permuted_tuple[1:]:
        x_b, y_b = city_location
        distance += ((x_b-x_a)**2 + (y_b-y_a)**2)**0.5
        x_a, y_a = x_b, y_b

average_distance = distance / factorial_recursive(city_num)

print(average_distance)
