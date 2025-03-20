# 動的計画法：ナップザック DP

# 動的計画法とは、for文でボトムアップに表を埋めていくアルゴリズム。計算量は表のマス目数に一致
# メモ化再帰とは、すべての計算パターンについてメモしたものをトップダウンに再起的に計算する手法。
n = int(input())

fib_l = []
def f_fib(n):
    if(n==0 or n==1): return 1
    else: return fib_l[n-1] + fib_l[n-2]

for i in range(n+1):
    fib_l.append(f_fib(i))

print(fib_l[n])
