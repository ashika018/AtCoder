def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, L, R = ILI()
A_l = ILI()

ans = []

for a in A_l:
    if(L<=a<=R): X = a
    elif(a<L): X = L
    else: X = R
    ans.append(str(X))

print(' '.join(ans))