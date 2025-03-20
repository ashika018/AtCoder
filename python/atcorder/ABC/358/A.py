def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S, T = SLI()
if(S=='AtCoder' and T=='Land'):
    print('Yes')
else:
    print('No')