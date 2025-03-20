# 動的計画法：ナップザックDP
days_n, clothes_n = list(map(int, input().split(' ')))
temprature_l = [-1]+[int(input()) for _ in range(days_n)]
clothesinfo_l = [[-1,-1,-1]]+[list(map(int, input().split(' '))) for _ in range(clothes_n)]

# memory_fieldsは一つ多めに要素を格納しておくことで、日数をそのままindexとして使えるようにする
memory_fields = [[0]*(clothes_n+1) for _ in range(days_n+1)]
# 1日目の処理だけ済ましておく
l = [0]+[0 if(clothesinfo_l[i][0]<=temprature_l[1]<=clothesinfo_l[i][1]) else -1 for i in range(1, clothes_n+1)]
memory_fields[1] = l

# 表を埋めていく部分
for day in range(2, days_n+1):
    for cloth in range(1, clothes_n+1):
        temp_today = temprature_l[day]
        wearable_temp_L = clothesinfo_l[cloth][0]
        wearable_temp_H = clothesinfo_l[cloth][1]
        cloth_point = clothesinfo_l[cloth][2]
        if((temp_today<wearable_temp_L) or (wearable_temp_H<temp_today)): 
            memory_fields[day][cloth] = -1
        else:
            value = max([memory_fields[day-1][J]+abs(cloth_point-clothesinfo_l[J][2]) for J in range(1, clothes_n+1) if memory_fields[day-1][J]!=-1])
            memory_fields[day][cloth] = value
        
print(max(memory_fields[-1]))


