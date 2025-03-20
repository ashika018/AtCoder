def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


N = II()
A = ILI()

d_toR = {}
for i in range(N-1):
    d_toR[A[i]] = A[i+1]
d_toR[A[-1]] = -1

d_toL = {}
for i in range(len(A)-1, 0, -1):
    d_toL[A[i]] = A[i-1]
d_toL[A[0]] = -1

Q = II()
start = A[0]
for _ in range(Q):
    query = ILI()
    if(query[0]==1):
        x, y = query[1], query[2]
        tmp = d_toR[x]
        d_toR[x] = y
        d_toR[y] = tmp
        d_toL[tmp] = y
        d_toL[y] = x
    else:
        x = query[1]
        if(x==start):
            start = d_toR[x]
        tmp1, tmp2 = d_toR[x], d_toL[x]
        d_toR[x] = -1
        d_toL[x] = -1
        if(tmp2!=-1):
            d_toR[tmp2] = tmp1
        if(tmp1!=-1):
            d_toL[tmp1] = tmp2

ans_l = []
n = start
while True:
    if(n==-1): break
    ans_l.append(str(n))
    n = d_toR[n]

ans = ' '.join(ans_l)
print(ans)