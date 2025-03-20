# 全探索：順列全探索

# クイーンは、横方向に自由に移動できることから、各行に対して1つしかクイーンは存在しない。
# すると、クイーンの配置は0行目にあるクイーンの配置パターンは8通り、1行目にあるクイーンの配置パターンは7通り、...
# となるから全部で、8!通りである → 順列全探索で全パターンの探索が行える

import itertools

k = int(input())
queen_location_set = set([tuple(map(int, input().split(' '))) for _ in range(k)])
# print(queen_location_set)

# 斜めの位置にクイーンがないか計算する関数
# 右上
def queen_check_UR(queen_location_set, x, y):
    if(0<=x<=7 and 0<=y<=7):
        if((x, y) in queen_location_set): return 1+queen_check_UR(queen_location_set, x+1, y+1)
        else: return 0+queen_check_UR(queen_location_set, x+1, y+1)
    else: return 0
# 右下
def queen_check_DR(queen_location_set, x, y):
    if(0<=x<=7 and 0<=y<=7):
        if((x, y) in queen_location_set): return 1+queen_check_UR(queen_location_set, x+1, y-1)
        else: return 0+queen_check_UR(queen_location_set, x+1, y-1)
    else: return 0
# 左上
def queen_check_UL(queen_location_set, x, y):
    if(0<=x<=7 and 0<=y<=7):
        if((x, y) in queen_location_set): return 1+queen_check_UR(queen_location_set, x-1, y+1)
        else:return 0+queen_check_UR(queen_location_set, x-1, y+1)
    else: return 0
# 左下
def queen_check_DL(queen_location_set, x, y):
    if(0<=x<=7 and 0<=y<=7):
        if((x, y) in queen_location_set): return 1+queen_check_UR(queen_location_set, x-1, y-1)
        else: return 0+queen_check_UR(queen_location_set, x-1, y-1)
    else: return 0

# 襲撃できるクイーンの数
def count_attacking_queens(queen_location_set, x, y):
    return queen_check_UR(queen_location_set, x, y) + queen_check_DL(queen_location_set, x, y) + queen_check_DR(queen_location_set, x, y) + queen_check_UL(queen_location_set, x, y) - 4



for permuted_tuple in itertools.permutations(range(8)):
    candidate_queen_location = set([(x, y) for x, y in enumerate(permuted_tuple)])
    queen_location_set_copy = queen_location_set.copy()

    if(queen_location_set_copy <= candidate_queen_location): 
        queen_location_set_copy = queen_location_set_copy | candidate_queen_location
        # print(queen_location_set_copy)
        check = 0
        ans_map = [['.']*8 for _ in range(8)]
        for queen_location in queen_location_set_copy:
            x, y = queen_location
            ans_map[x][y] = 'Q'
            if(count_attacking_queens(queen_location_set_copy, x, y) > 0): check += 1
        print(check)
        if(check == 0):
            for i in range(8):
                print(''.join(i))
