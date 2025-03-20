def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


# O(MN)かかるものを、imos法でO(M+N)に落とす
N, M = ILI()
X_l = ILI()

# 累積和：complative_sum
# complative_sum[i]:島i~島i+1間の橋を封鎖した場合の累積和
complative_sum = [0 for _ in range(N+2)]
for i in range(M-1):
    iland1, iland2 = min(X_l[i], X_l[i+1]), max(X_l[i], X_l[i+1])
    d = iland2-iland1
    # complative_sum[iland1]~complative_sum[iland2-1]に+(N-d)
    # それ以外に、+d
    complative_sum[0] += d
    complative_sum[iland1] -= d
    complative_sum[iland1] += N-d
    complative_sum[iland2] -= N-d
    complative_sum[iland2] += d
    complative_sum[N+1] -= d


# 累積和を計算
ans = float('inf')
for i in range(1, len(complative_sum)-1):
    complative_sum[i] += complative_sum[i-1]
    ans = min(ans, complative_sum[i])

print(ans)
