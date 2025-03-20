N = int(input())
A_l = [int(i) for i in input().split(' ')]

A_l.sort()
real_l = range(A_l[0], A_l[0]+N+1)

A_l = set(A_l)
real_l = set(real_l)
ans = list(real_l-A_l)[0]

print(ans)
