# 逆元を使う問題

# ax+by=gcd(a,b)の解(x,y)とgcd(a,b)を求める関数
def ex_euclid(a, b):
    if(b==0):
        return(1, 0, a)
    else:
        x_, y_, gcd = ex_euclid(b, a%b)
        return(y_, x_-(a//b)*y_, gcd)

# ax+by=cの解を求める関数
# 求めたいものが「ax+by=cかつcはgcd(a,b)の倍数」の場合、出力されたx,yにc//gcd(a,b)を掛け算したものが解
# 今回は使わない
def ax_by_c(a,b,c):
    x, y, gcd_ab = ex_euclid(a,b)
    return x*(c//gcd_ab), y*(c//gcd_ab)


# row_n+col_n-2 C col_n-1 (mod p)求める
# (row_n+col_n-2)!/(col_n-1)!*(row_n-1)! (mod p)
# オーバーフローに注意
row_n, col_n = list(map(int, input().split(' ')))
p = 1000000007

# 分子：numerator
numerator = 1
for i in range(1, row_n+col_n-1):
    numerator = numerator*(i%p)
    numerator %= p

# 分母：denominator
denominator1 = 1
for i in range(1, row_n):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator1 = denominator1*(i_inverse%p)
    denominator1 %= p
denominator2 = 1
for i in range(1, col_n):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator2 = denominator2*(i_inverse%p)
    denominator2 %= p

print((numerator*denominator1*denominator2)%p)