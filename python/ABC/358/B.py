def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, A = ILI()
T_l = ILI()

total_t = 0
for i in range(N):
    if(total_t<=T_l[i]):
        total_t = T_l[i]+A
    else:
        total_t += A
    print(total_t)
