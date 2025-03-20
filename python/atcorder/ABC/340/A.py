def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

A, B, D = ILI()

ans_l = []
tmp = A
while True:
    ans_l.append(str(tmp))
    if(tmp==B): break
    tmp += D

print(' '.join(ans_l))
