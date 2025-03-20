N, K = map(int, input().split())
pl = list(map(int, input().split()))

#print(pl)

for i in range(K, N+1):
    min = sorted(pl[0:i])
    print(min[i-K])
