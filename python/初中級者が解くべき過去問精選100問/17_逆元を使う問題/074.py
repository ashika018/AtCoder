# 逆元を扱う問題

# 要するに1<=a1<=a<=2<=...<=ak<=nを満たすようなa1~akの組み合わせの数を考えれば良い
# つまりn-1個の|とk個の⚪︎の並び方の総和、つまり(n+k-1)Ck = (n+k-1)!/(n-1)!(k)! (mod 1000000007)を計算する

# ax+by=gcd(a,b)の解(x,y)とgcd(a,b)を求める関数
def ex_euclid(a, b):
    if(b==0):
        return(1, 0, a)
    else:
        x_, y_, gcd = ex_euclid(b, a%b)
        return(y_, x_-(a//b)*y_, gcd)

n = int(input())
k = int(input())
p = 1000000007

# 分子：numerator
numerator = 1
for i in range(1, n+k):
    numerator = numerator*(i%p)
    numerator %= p
# 分母：denominator
denominator1 = 1
for i in range(1, n):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator1 = denominator1*(i_inverse%p)
    denominator1 %= p
denominator2 = 1
for i in range(1, k+1):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator1 = denominator1*(i_inverse%p)
    denominator1 %= p

print((numerator*denominator1*denominator2)%p)