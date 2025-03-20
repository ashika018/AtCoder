# 動的計画法：ナップザック DP
# https://zenn.dev/fjnkt98/articles/685c9a991d4e61

days_n, selected_pasta_date_n = list(map(int, input().split(' ')))
selected_pasta_data = dict([tuple(map(int, input().split(' '))) for _ in range(selected_pasta_date_n)])
selected_pasta_date_set = set(selected_pasta_data.keys())

# ↓ 当初、これでやっていたらデータの上書きをする際に複数箇所が書き変わってしまった。
'''
l = [[0,0],[0,0],[0,0]]
memory_fields = [l for _ in range(days_n)]
'''
memory_fields = [[[0,0],[0,0],[0,0]] for _ in range(days_n)]

# day=1の時だけ別で作っておく
day1_field = [[0,0],[0,0],[0,0]]
if(1 in selected_pasta_date_set): 
    pasta_code = selected_pasta_data[1]-1
    day1_field[pasta_code] = [1,0]
else: day1_field = [[1,0],[1,0],[1,0]]
memory_fields[0] = day1_field

# dayの取り方に注意しないと、計算結果がズレる羽目になる。
# 上でday1の処理はしたので、二日目以降の処理をする
for day in range(1, days_n):
    selected_pasta_code = -1
    if(day+1 in selected_pasta_date_set): 
        selected_pasta_code = selected_pasta_data[day+1]-1
    for pasta_code in range(3):
        # その日のパスタが指定されているのかどうかの判定
        if((selected_pasta_code!=-1) and (pasta_code!=selected_pasta_code)): continue
        for flag in range(2):
            if(flag==0):
                pasta_code_l = [i for i in range(3) if i != pasta_code]
                memory_fields[day][pasta_code][flag] = sum([memory_fields[day-1][i][0]+memory_fields[day-1][i][1] for i in pasta_code_l])
                # print(f'-----------------')
                # print(f'day:{day}, pasta_code:{pasta_code}, flag:{flag}')
                # for l in memory_fields: print(l)
            else:
                memory_fields[day][pasta_code][flag] = memory_fields[day-1][pasta_code][0]
                # print(f'-----------------')
                # print(f'day:{day}, pasta_code:{pasta_code}, flag:{flag}')
                # for l in memory_fields: print(l)
    

ans = sum([sum(l) for l in memory_fields[-1]])%10000
print(ans)
