def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

K, G, M = ILI()

glass, cup = 0, 0
for _ in range(K):
    if(glass==G): glass = 0
    elif(cup==0): cup = M
    else: 
        if(cup+glass<=G): cup, glass = 0, cup+glass  
        else: cup, glass = cup-(G-glass), G

print(f'{glass} {cup}')