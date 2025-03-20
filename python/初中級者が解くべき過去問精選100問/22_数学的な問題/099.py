# 数学的な問題
# 参考：https://drken1215.hatenablog.com/entry/2020/01/25/221900

M = int(input())

digit_n, sum_digit = 0, 0
for _ in range(M):
    d, c = list(map(int, input().split(' ')))
    digit_n += c
    sum_digit += d*c

print((digit_n-1)+((sum_digit-1)//9))