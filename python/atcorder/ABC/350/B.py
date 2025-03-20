def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, Q = ILI()
T_l = ILI()

tooth_d = dict([(i, True) for i in range(1, N+1)])
for t in T_l:
    if(tooth_d[t]):
        tooth_d[t] = False
    else:
        tooth_d[t] = True

tooth_num = 0
for boolean in tooth_d.values():
    if(boolean):
        tooth_num += 1

print(tooth_num)
