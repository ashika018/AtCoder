def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, A, B = ILI()
D_l = list(set(map(lambda x: (x%(A+B))+1,ILI())))
D_l.sort()

MAX, MIN = max(D_l), min(D_l)
if(MAX-MIN+1<=A):
    print('Yes')
    exit()

for i in range(1, len(D_l)):
    holiday_length = (A+B-D_l[i]+1) + (D_l[i-1])
    if(holiday_length<=A):
        print('Yes')
        exit()

print('No')
