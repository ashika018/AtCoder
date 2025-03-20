def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, L = ILI()
A_l = ILI()

ans = 0
for a in A_l:
    if(a>=L): ans+=1

print(ans)