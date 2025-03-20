# 全探索：bit全探索
buildings_num, colors = list(map(int, input().split(' ')))
buildings_heights_l = list(map(int, input().split(' ')))

# n番目の建物がn-1番目以前のどの建物よりも大きいかチェックし、
# n番目の建物より大き鋳物が存在したら、n番目の建物に必要な高さを計算する関数
def cal_required_height(max_height, n_height, n):
    if(n-1==0 or max_height<n_height): return 0
    else: return max_height+1-n_height

# 高々15この建物のうち、どの建物をを見えるようにするかの組み合わせは2**15通り
ans = 1000000000000000000000
for i in range(2**buildings_num):
    n = sum([(i>>j) & 1 for j in range(buildings_num)])
    max_height = 0
    tmp = 0
    if(n >= colors):
        for j in range(buildings_num):
            if((i>>j) & 1):
                required_h = cal_required_height(max_height=max_height, n_height=buildings_heights_l[j], n=j+1)
                tmp += required_h
                max_height = buildings_heights_l[j] + required_h
            else:
                max_height = max(max_height, buildings_heights_l[j])
        ans = min(ans, tmp)

print(ans)
