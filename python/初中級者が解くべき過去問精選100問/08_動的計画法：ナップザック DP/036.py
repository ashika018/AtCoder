# 動的計画法：ナップザック DP
# 参考ページ：https://kunassy.com/python_dp_bubunwa/#toc14

# ポイントは同じ商品を何個でも選ぶことができるという点
# 前問：i番目の商品を考える時は、表のi-1行目の情報を参照していた
# 本問：i番目の商品を考える時は、表のi行目の情報も参照すれば良い。

item_num, capacity_weight = list(map(int, input().split(" ")))
items_l = [[0, 0]] + [list(map(int, input().split(' '))) for _ in range(item_num)]

memory_fields = [[0]*(capacity_weight+1) for _ in range(item_num+1)]

def dp(i, max_weight):
    value_i, weight_i = items_l[i]
    option1 = memory_fields[i-1][max_weight] # 上からおろしてくる
    if(max_weight-weight_i<0): memory_fields[i][max_weight] = option1
    else:
        option2 = memory_fields[i-1][max_weight-weight_i] + value_i # 左上から下ろしてくる
        option3 = memory_fields[i][max_weight-weight_i] + value_i # 左から引用する
        memory_fields[i][max_weight] = max(option1, option2, option3)

for item_i in range(1, item_num+1):
    for max_weight in range(1, capacity_weight+1):
        dp(i=item_i, max_weight=max_weight)

print(memory_fields[-1][-1])