def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
S = SI()

S_ = sorted(S)

ans = 0
# 最初は、10**7まで回していたが、それだと余裕でTLEする。
# 10*13-1(13桁の数値の最大値)に平方根を取った回数分チェックすれば良い
# (10**13)**0.5<4*10^6
for i in range(int((10**N)**0.5)+1):
    i_square = str(int(i)**2)
    i_square += ''.join(['0']*(len(S_)-len(i_square)))
    i_square = sorted(i_square)
    if(S_==i_square):
        ans += 1

print(ans)
