# 累積和
# いもす法
city_n, trip_days = list(map(int, input().split(' ')))
visit_order = [0]+list(map(int, input().split(' ')))
fareinfo_l = [[0,0,0]] + [list(map(int, input().split(' '))) for _ in range(city_n-1)]

# いもす法の実装
imos_l = [0 for _ in range(city_n+1)]
for i in range(1, trip_days):
    # city_i→city_j(j<i)という場合は、city_j→city_iとみなす（いもす法のアルゴリズム的に）
    if(visit_order[i]<=visit_order[i+1]): start, goal = visit_order[i], visit_order[i+1]
    else: start, goal = visit_order[i+1], visit_order[i]
    imos_l[start] += 1
    imos_l[goal] -= 1
for i in range(len(imos_l)-1):
    imos_l[i+1] += imos_l[i]

# 運賃の最小値を計算
ans = 0
for city_i in range(1, city_n):
    visited_n = imos_l[city_i]
    Ai, Bi, Ci = fareinfo_l[city_i]
    ans += min(Ai*visited_n, Bi*visited_n+Ci)
print(ans)