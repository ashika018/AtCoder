def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 行と列の操作順（行を先に操作するか列を先に操作するか）は結果に影響を及ぼさない。
# bit全探索っぽいが、k行目に対する操作を複数回行えるので、bit全探索では全列挙はできない
# 最初にk行目 or k列目にあった行がどこに移動したかを全列挙する
# → 順列全探索

# また、操作回数に関しては""転倒数""を計算するのがよし

import itertools
import copy

H, W = ILI()
A_map = [ILI() for _ in range(H)]
B_map = [ILI() for _ in range(H)]
INF = float('inf')

# 二つの二次元リストが同じであるか判定する関数
def IsSame(map_a, map_b):
    return map_a==map_b

# 操作回数（==転倒数）を計算する関数(O(N^2))
# 転倒数: https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion
def cal_operation_n(permuted_tuple):
    n = 0
    for i in range(len(permuted_tuple)):
        for j in range(i+1, len(permuted_tuple)):
            if(permuted_tuple[i]>permuted_tuple[j]):
                n += 1
    return n

ans = INF
for permuted_tuple_row in itertools.permutations(range(H)):
    A_map_2 = copy.deepcopy(A_map)
    for r_to, r_from in enumerate(permuted_tuple_row):
        # 行の入れ替え
        A_map_2[r_to] = A_map[r_from]
    for permuted_tuple_col in itertools.permutations(range(W)):
        A_map_3 = copy.deepcopy(A_map_2)
        for c_to, c_from in enumerate(permuted_tuple_col):
            # 列の入れ替え
            for row in range(H):
                A_map_3[row][c_to] = A_map_2[row][c_from]
        if(IsSame(A_map_3, B_map)):
            tmp = cal_operation_n(permuted_tuple_row) + cal_operation_n(permuted_tuple_col)
            ans = min(ans, tmp)

ans = -1 if(ans==INF) else ans
print(ans)