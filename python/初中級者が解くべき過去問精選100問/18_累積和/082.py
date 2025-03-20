# 累積和
# いもす法
data_n = int(input())

def cal_seconds(s_hhmmss):
    h, m, s = list(map(int, s_hhmmss.split(':')))
    return h*60*60 + m*60 + s

# 累積法：compative_sum
# complative_sum_l[i] = 時刻i(00:00:00からi秒後)における山手線を走る車両の数
# まずは+-1をしていくところから。
complative_sum_l = [0 for _ in range(60*60*60+1)]
for _ in range(data_n):
    start, end = list(input().split(' '))
    start, end = cal_seconds(start), cal_seconds(end)
    complative_sum_l[start] += 1
    complative_sum_l[end+1] -= 1
# 次に累積和の計算
for i in range(1, len(complative_sum_l)):
    complative_sum_l[i] += complative_sum_l[i-1]

# 最大値を全探索(上のfor文の中に含めることも可能)
ans = 0
for tmp in complative_sum_l:
    ans = max(ans, tmp)
print(ans)