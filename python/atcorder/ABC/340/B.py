def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

Q = II()

A = []
for _ in range(Q):
    judge, num = ILI()
    if(judge==1):
        A.append(num)
    else:
        print(A[-num])
