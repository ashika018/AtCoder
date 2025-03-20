def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()
num = int(S[3:])
if(1<=num<316 or 316<num<=349):
    print('Yes')
else:
    print('No')
