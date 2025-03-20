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

max1, max2 = max(A_l), 0
for a in A_l:
    if(a<max1):
        max2 = max(max2, a)

print(max2)