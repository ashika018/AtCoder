def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()
T = SI().lower()

cnt = 0
for s in list(S):
    if(T[cnt]==s):
        cnt += 1
    if(cnt>=3):
        print('Yes')
        exit()

if(cnt==2 and T[2]=='x'):
    print('Yes')
else:
    print('No')