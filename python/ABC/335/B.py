def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()

for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            if(x+y+z<=N):
                print(f'{x} {y} {z}')