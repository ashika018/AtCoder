import itertools

K = int(input())

# 0~9の各数字を使うor使わないの選択があるので、全パターンとしては2**10通り
target_l = []
for i in range(2**10):
    number_l = []
    for j in range(10):
        if((i >> j) & 1): number_l.append(j)
    number_l.reverse()
    number_l = list(map(str, number_l))
    target_l.append(''.join(number_l))

target_l.remove('') # 0~9まで全て使われない場合、''が含まれてしまう。これだとintにしようとしたときにエラーを吐いてしまう
target_l = list(map(int, target_l))
target_l.sort()
print(target_l[K])