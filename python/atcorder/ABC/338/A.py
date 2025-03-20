def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()

S_zero = S[0]
if(len(S)>1): S_others = S[1:]
else: S_others = 'a'

if(S_zero.isupper() and S_others.islower()):
    print('Yes')
else:
    print('No')

