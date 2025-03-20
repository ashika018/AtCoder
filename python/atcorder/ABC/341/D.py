def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

import math

N, M, K = ILI()

x = math.lcm(N, M)
y = x//N + x//M - 2

i1, i2 = 1, 1
cnt = 1
while cnt<=(K-1)%y:
    if(N*i1<M*i2):
        i1+=1
    else:
        i2+=1
    cnt+=1

# print(f'x:{x}, y:{y}, K:{K}, l:{l}')
ans = x*((K-1)//y) + min(N*i1, M*i2)
print(ans)