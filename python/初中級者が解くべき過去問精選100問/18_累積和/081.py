# 累積和
# いもす法
questionnaire_n = int(input())

# 累積和：complative
complative_sum_l = [0 for _ in range(10**6+2)]
# l, rから所定の場所に+1 or -1していく
for _ in range(questionnaire_n):
    l, r = list(map(int, input().split(' ')))
    complative_sum_l[l] += 1
    complative_sum_l[r+1] -= 1
# complative_sum_lを左から足し、累積和を計算
for i in range(1, 10**6+2):
    complative_sum_l[i] += complative_sum_l[i-1]

# 最大値の探索(上のfor文内に組み込むことも可能)
ans = 0
for tmp in complative_sum_l:
    ans = max(ans, tmp)

print(ans)
