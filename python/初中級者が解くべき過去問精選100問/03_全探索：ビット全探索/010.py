# 全探索：ビット全探索

length = int(input())
numbers_l = list(map(int, input().split(' ')))
num_goals = int(input())
goals_l = list(map(int, input().split(' ')))

ans_l = ['no']*num_goals

# 数列(numbers_l)の各数字を使うか使わないかの全パターンを二進数で表現する
# (使う or 使わない)の選択をlength回行わなければならないので、全パターンは2**length通りである
for i in range(2**length):
    sum_ans = 0
    for j in range(length):
        # i を右シフトし、最下位bitのフラグが立っているかのチェック（最下位の位が1かどうかチェック）
        if((i>>j) & 1):
            sum_ans += numbers_l[j]

    # 答えを生成
    for k in range(num_goals):
        if(goals_l[k] == sum_ans): ans_l[k] = 'yes'

for ans in ans_l: print(ans)