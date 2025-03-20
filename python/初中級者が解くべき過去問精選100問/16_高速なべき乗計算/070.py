# 高速なべき乗計算
x, n = list(map(int, input().split(' ')))

# x^nを求める
def pow_ashikawa(x, n):
    # x^(2^0)の部分を計算
    ans = 1 if(n%2!=1) else x
    x_i = x
    # x^(2^1)~x^(2^t)まで計算
    while n>1:
        x_i = x_i*x_i
        n = n//2
        # nを2^iで割った数（余りは無視）が奇数なら、nを二進数で表した時のi桁目は1になる
        if(n%2 == 1):
            ans *= x_i
    return ans

print(pow_ashikawa(x,n))