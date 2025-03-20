# 高速な素数判定法

# エラトステネスのふるい
# https://manabitimes.jp/math/992

# 1~10**5の間の数について、素数かどうかの判定を行う
# is_prime_l[i]=True→iは素数、is_prime_l[i]=False→iは偶数
is_prime_l = [False]+[True for _ in range(10**5)]
i=2
while True:
    if(i>(10**5)**0.5): break
    k = 2
    # iの倍数を消していく
    while(i*k<len(is_prime_l)):
        is_prime_l[i*k] = False
        k += 1
    i += 1


# num_2017LikeNumbers_l[i]=5 → 1~iのうち2017 like numberは5個存在。
num_2017LikeNumbers_l = [0 for i in range(10**5)]
for i in range(2, 10**5):
    # 偶数は2017 like numberにはなれない（偶数だから）
    if(i%2==0): 
        num_2017LikeNumbers_l[i] = num_2017LikeNumbers_l[i-1]
        continue
    is_i_2017LikeNumber = (is_prime_l[i] and is_prime_l[(i+1)//2])
    if(is_i_2017LikeNumber): 
        num_2017LikeNumbers_l[i] = 1+num_2017LikeNumbers_l[i-1]
    else: 
        num_2017LikeNumbers_l[i] = num_2017LikeNumbers_l[i-1]
    

Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split(' ')))
    print(num_2017LikeNumbers_l[r]-num_2017LikeNumbers_l[l-1])
