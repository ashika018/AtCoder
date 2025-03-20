# 累積和
# 言語選択で、pypyを選ぶとMLEする。CPythonを選ぶと使用メモリ量が1/6とかになる
# PyPyは早いけどメモリを食い、Cpythonは遅いけどメモリ量は削減できる

hotel_n, days_n = list(map(int, input().split(' ')))
hotel_distance_l = [int(input()) for _ in range(hotel_n-1)]
to_hotel_l = [int(input()) for _ in range(days_n)]

# 累積和：complative_sum
# d_from_hotel1_l[5]=宿1から宿5までの距離
d_from_hotel1_l = [0, 0]
d_from_hotel1 = 0
for d in hotel_distance_l:
    d_from_hotel1 += d
    d_from_hotel1_l.append(d_from_hotel1)

# クエリに答えていく
travel_d = 0
from_hotel = 1
for i in to_hotel_l:
    to_hotel = from_hotel + i
    travel_d += abs(d_from_hotel1_l[to_hotel]-d_from_hotel1_l[from_hotel])
    travel_d %= 10**5
    from_hotel = to_hotel
print(travel_d)