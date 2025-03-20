# 全探索：bit全探索

# 各行について、ひっくり返すorひっくり返さないの組み合わせは、2**10通りしかないので、bit全探索でいけそう
# あとは残りの列について、「ひっくり返してある煎餅の数」と「ひっくり返していない煎餅の数」で多い方を足していく（）
# （ひっくり返していない煎餅の数の方が多かったら、その列はひっくり返せば良いので。）

row_num, col_num = list(map(int, input().split(' ')))
senbei_map = [list(map(int,(input().split(' '))[:col_num])) for _ in range(row_num)]

# 行をひっくり返す関数
# goal : 与えられた0,1のリストに対して、0と1を逆転させる 
# input: list, output: list
def turn_bar(zero_one_l):
    # ＾は排他的論理和を表す
    return [i^1 for i in zero_one_l]

# ある列に含まれる、表向きの煎餅の数をカウントする関数
def count_front_senbei(senbei_map, col):
    front_senbei_num = 0
    for l in senbei_map:
        front_senbei_num += l[col]
    return front_senbei_num

max_front_senbei_sum = 0
for i in range(row_num**2):
    front_senbei_sum = 0
    senbei_map_copy = senbei_map.copy()  # 修正
    for r in range(row_num):
        if((i>>r) & 1): senbei_map_copy[r] = turn_bar(senbei_map_copy[r])
    for c in range(col_num):
        front_senbei = count_front_senbei(senbei_map=senbei_map_copy, col=c)
        front_senbei_sum += max(front_senbei, row_num-front_senbei)
        # print(front_senbei_sum)
    max_front_senbei_sum = max(front_senbei_sum, max_front_senbei_sum)

print(max_front_senbei_sum)
