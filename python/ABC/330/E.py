def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 考察＋heapq
import heapq

N, Q = ILI()
A_l = [N+10]+ILI()
Q = [ILI() for _ in range(Q)]

# A_l = A1, A2, ..., Anだから、非負整数0~Nの中で、少なくとも一つはAiに使われていない
# （余裕を持って）0~N+5までの出現数をカウントしておく
numcount_d = dict([(i, 0) for i in range(N+6)])
for i in A_l:
    if(i<=N+5):
        numcount_d[i] += 1

# 出現回数が0だった0~N+5の数をheapqにプッシュしていく
zero_l = []
for i, n in numcount_d.items():
    if(n==0):
        heapq.heappush(zero_l, i)

# クエリに答えていく
for l in Q:
    i_k, x_k = l
    A_ik = A_l[i_k]
    if(A_ik<=N+5):
        numcount_d[A_ik] -= 1
        if(numcount_d[A_ik]==0):
            heapq.heappush(zero_l, A_ik)
    A_l[i_k] = x_k
    if(x_k<=N+5):
        numcount_d[x_k] += 1
    while True:
        mex = heapq.heappop(zero_l)
        if(numcount_d[mex]==0):
            print(mex)
            # 取り出したやつを戻しておく必要あり。
            heapq.heappush(zero_l, mex)
            break
