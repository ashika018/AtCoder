def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, S, M, L = ILI()

ans = float('inf')
for s in range(0, (N//6)+2):
    for m in range(0, (N//8)+2):
        for l in range(0, (N//12)+2):
            # nokori = N-6*s-8*m
            # if(nokori<=0): l = 0
            # elif(nokori%12==0): l = nokori//12
            # else: l = nokori//12+1
            if(6*s+8*m+12*l>=N): ans = min(ans, S*s+M*m+L*l)
            

print(ans)