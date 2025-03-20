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

d = {}
for i in range(N-1):
    s, t = ILI()
    cnt = A_l[i]//s
    A_l[i+1] += t*cnt

print(A_l[-1])