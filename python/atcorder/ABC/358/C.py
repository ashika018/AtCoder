def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, M = ILI()
S_l = [list(SI()) for _ in range(N)]

ans = float('inf')
for i in range(2**N):
    tmp = 0
    d = dict([(m, False) for m in range(M)])
    for j in range(N):
        if((i>>j)&1):
            tmp+=1
            for k, check in enumerate(S_l[j]):
                if(check=='o'):
                    d[k] = True

    if(all(d.values())):
        ans = min(ans, tmp)

print(ans)
