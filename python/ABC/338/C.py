def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
Q_l = ILI()
A_l = ILI()
B_l = ILI()
INF = float('inf')

max_an = INF
for i in range(N):
    if(A_l[i]==0): tmp_a = INF
    else: tmp_a = Q_l[i]//A_l[i]
    max_an = min(max_an, tmp_a)

ans = 0
for an in range(max_an+1):
    max_bn = INF
    for i in range(N):
        if(B_l[i]==0): tmp_b = INF
        else: tmp_b = (Q_l[i]-A_l[i]*an)//B_l[i]
        max_bn = min(max_bn, tmp_b)
    ans = max(ans, an+max_bn)

print(ans)