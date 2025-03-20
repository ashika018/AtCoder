# 動的計画法：ナップザック DP

item_num, bag_capacity = list(map(int, input().split(' ')))
# 0番目のitemを入れておくことで、dpの実装が楽になる（詳しくはメモを参照）
items_list = [[0, 0]]+[list(map(int, input().split(' '))) for _ in range(item_num)]

memory_table = [[0]*(bag_capacity+1) for _ in range(item_num+1)]

def dp(item_i, max_weight):
    value_i, weight_i = items_list[item_i]

    v_option1 = memory_table[item_i-1][max_weight]
    v_option2 = memory_table[item_i-1][max_weight-weight_i]+value_i

    if(max_weight-weight_i<0 or v_option1>v_option2): memory_table[item_i][max_weight] = v_option1
    else: memory_table[item_i][max_weight] = v_option2

# for文を回して、表をボトムアップに埋めていく作業
for item_i in range(1, item_num+1):
    for max_weight in range(1, bag_capacity+1):
        dp(item_i=item_i, max_weight=max_weight)


print(memory_table[-1][-1])