def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
P_l = ILI()
d = dict([(p, i) for i, p in enumerate(P_l)])
Q = II()

ans_l = []
for _ in range(Q):
    A, B = ILI()
    if(d[A]<d[B]):
        ans_l.append(A)
    else:
        ans_l.append(B)

for ans in ans_l: print(ans)