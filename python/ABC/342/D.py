def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


N = II()
A_l = ILI()


# 1~2*10**5の間の数について、素数かどうかの判定を行う
# is_prime_l[i]=True→iは素数、is_prime_l[i]=False→iは偶数
is_prime_l = [False]+[True for _ in range(2*(10**5))]
i=2
while True:
    if(i>(2*(10**5))**0.5): break
    k = 2
    # iの倍数を消していく
    while(i*k<len(is_prime_l)):
        is_prime_l[i*k] = False
        k += 1
    i += 1


ans, zero_n = 0, 0
d = {}
for i, Ai in enumerate(A_l):
    if(Ai==0):
        ans += N-1-zero_n
        zero_n += 1
        continue

    tmp = Ai
    tmp_l = []
    # 素因数分解
    for j in range(2, int(Ai**0.5)+10):
        if(tmp%j==0):
            cnt = 0
            while(tmp%j==0):
                cnt+=1
                tmp//=j
            # 約数の累乗が奇数なら
            if(cnt%2==1):
                tmp_l.append(j)
    
    if(is_prime_l[Ai]): tmp_t = tuple([Ai])
    else: tmp_t = tuple(tmp_l)
    
    if(tmp_t in d): d[tmp_t] += 1
    else: d[tmp_t] = 1


for v in d.values():
    ans += v*(v-1)/2

print(int(ans))

