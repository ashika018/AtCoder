# 逆元を使う問題
# 細々した数式はノートを見るべし

# ax+by=gcd(a,b)の解(x,y)とgcd(a,b)を求める関数
def ex_euclid(a, b):
    if(b==0):
        return(1, 0, a)
    else:
        x_, y_, gcd = ex_euclid(b, a%b)
        return(y_, x_-(a//b)*y_, gcd)

X, Y = list(map(int, input().split(' ')))
# A=(2X-Y), B=(2Y-X)/3として、(A+B)CA=(A+B)!/A!B!を計算する
A, A_ = int((2*X-Y)/3), (2*X-Y)/3
B, B_ = int((2*Y-X)/3), (2*Y-X)/3
p = 1000000007
if(A!=A_ or B!=B_ or A<0 or B<0):
    print(0)
    exit()

# 分子：numerator
numerator = 1
for i in range(1, A+B+1):
    numerator = numerator*(i%p)
    numerator %= p
# 分母：denominator
denominator1 = 1
for i in range(1, A+1):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator1 = denominator1*(i_inverse%p)
    denominator1 %= p
denominator2 = 1
for i in range(1, B+1):
    i_inverse, _, _ = ex_euclid(i, p)
    denominator2 = denominator2*(i_inverse%p)
    denominator2 %= p

print((numerator*denominator1*denominator2)%p)
