# 累積和

N = int(input())
A__l = list(map(int, input().split(' ')))
# 累積和：complative_sum
# complative_sum_l[5]=a1~a5の和
complative_sum_l = [0]
total_sum = 0
for a_i in A__l:
    total_sum += a_i
    complative_sum_l.append(total_sum)

for contiguous_blocks_n in range(1, N+1):
    ans = -1
    for i in range(N-contiguous_blocks_n+1):
        ans = max(ans, complative_sum_l[i+contiguous_blocks_n]-complative_sum_l[i])
    print(ans)
