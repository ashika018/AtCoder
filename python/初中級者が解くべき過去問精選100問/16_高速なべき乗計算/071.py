# 高速なべき乗計算
city_n, visit_city_n = list(map(int, input().split(' ')))
roadinfo_l = [0]+list(map(int, input().split(' ')))
visit_order_l = [1]+list(map(int, input().split(' ')))+[1]

# x^nを求める
def pow_ashikawa(x, n):
    # x^(2^0)の部分を計算
    ans = 1 if(n%2!=1) else x%1000000007
    x_i = x
    # x^(2^1)~x^(2^t)まで計算
    while n>1:
        x_i = (x_i%1000000007)*(x_i%1000000007)
        n = n//2
        # nを2^iで割った数（余りは無視）が奇数なら、nを二進数で表した時のi桁目は1になる
        if(n%2 == 1):
            ans *= x_i
            ans = ans%1000000007
    return ans

# total_cost_l[k] = 「city1→cityk or cityk→city1の移動」にかかるコスト(1<=k)
total_cost = 0
total_cost_l = [0, 0]
for i in range(1, city_n):
    total_cost += pow_ashikawa(roadinfo_l[i], roadinfo_l[i+1])
    total_cost %= 1000000007
    total_cost_l.append(total_cost)


ans = 0
for i in range(len(visit_order_l)-1):
    city_from, city_to = visit_order_l[i], visit_order_l[i+1]
    if(city_from<city_to): left_city, right_city = city_from, city_to
    else: left_city, right_city = city_to, city_from

    ans += total_cost_l[right_city] - total_cost_l[left_city]
    ans = ans%1000000007

print(ans)