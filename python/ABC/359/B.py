def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
A_l = ILI()

ans = 0
for i in range(2*N-2):
    if(A_l[i] == A_l[i+2]): ans += 1
print(ans)