def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# L <= min(10**5, OO)より、Lは高々10**5。
# つまり価格の高い順に全探索していけば、10**5+1回目にはansが見つかる
# AとBを価格の高い順に並び替えて、全探索していく。
# このとき、「price=AとBの価格の和」が暫定のansより小さければ、2個目のfor文はbreakしても良い
# こうした工夫をすることで、無駄な計算を削減できる

N, M, L = ILI()
A = dict([(i+1, price) for i, price in enumerate(ILI())])
A = dict(sorted(A.items(), key=lambda item: item[1], reverse=True))
B = dict([(i+1, price) for i, price in enumerate(ILI())])
B = dict(sorted(B.items(), key=lambda item: item[1], reverse=True))
A_dishes, A_prices, B_dishes, B_prices = list(A.keys()), list(A.values()), list(B.keys()), list(B.values())

L_d = {}
for _ in range(L):
    ci, di = ILI()
    L_d[(ci, di)] = A[ci]+B[di]

# 全探索
ans = 0
for i_A in range(N):
    for i_B in range(M):
        price = A_prices[i_A]+B_prices[i_B]
        if(price<ans):
            break
        if((A_dishes[i_A], B_dishes[i_B]) not in L_d):
            ans = max(ans, price)
            break

print(ans)