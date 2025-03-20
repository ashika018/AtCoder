# 累積和
sori_n, Q = list(map(int, input().split(' ')))
needed_tonakai_l = list(map(int, input().split(' ')))
needed_tonakai_l.sort()

# 累積和：complative_sum
# complative_sum_l[3] = ソリ3台動かすのに必要なトナカイの数の最小値
total_n = 0
complative_sum_l = [0]
for tonakai_n in needed_tonakai_l:
    total_n += tonakai_n
    complative_sum_l.append(total_n)

def binary_search(l, r, key):
    while(r-l>1):
        mid = (r+l)//2
        if(complative_sum_l[mid]<=key): l = mid
        else: r = mid
    return l

# クエリに回答
for _ in range(Q):
    X = int(input())
    ans = binary_search(0, len(complative_sum_l), X)
    print(ans)