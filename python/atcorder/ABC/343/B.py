def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
edges_l = [[] for _ in range(N+1)]

for i in range(N):
    l = ILI()
    for j, num in enumerate(l):
        if(num==1):
            edges_l[i+1].append(j+1)

for i in range(1, N+1):
    l = list(map(str, sorted(edges_l[i])))
    ans = ' '.join(l)
    print(ans)

