N, M = map(int, input().split())
l_n = []
for i in range(M): l_n += list(map(int, input().split()))

j = 1
while j<=N:
    if(l_n.count(j)>=3): break
    else: j += 1
if(j>=N): print("Yes")
else: print("No")