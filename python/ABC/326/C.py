def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


# 累積和+圧縮を考える
# 座標yにプレゼントが置かれていたとき、座標y-M+1より右側にxを設定すれば、座標yに置いてあるプレゼントを獲得できる
# → 座標y-M+1に+1、座標y+1に-1を格納していく
# リストでやると、リストの長さが10**9となり、累積話を求めるときにTLEしそう
# 辞書に格納していく。（長さは最大2N<10**6）
# xは十数だったので、累積話は厳しそう、、。

# そもそも、xの候補って、A1, A2,..,Anのいずれか。
# A_l = [A1, A2, ..,An]をソートして、Ai+M-1より大きい最小Akを二分探索で見つけてくれば良い。
# ans = max(k-i) (1<=i<=N)となる

N, M = ILI()
A_l = ILI()
A_l.sort()

def binary_search(l, r, Ai):
    find = Ai+M-1
    while(r-l>1):
        mid = (l+r)//2
        if(find < A_l[mid]): r = mid
        else: l = mid
    return r

ans = 0
for i in range(N): # i=N-1の挙動が怖かったので、range(N-1)としていたが、それだとN=1の時にWAになる。
    Ai = A_l[i]
    k = binary_search(0, len(A_l), Ai)
    # print(f'(Ai, k)=({Ai},{k})')
    ans = max(ans, k-i)
print(ans)