def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


N = II()

i = 0
while True:
    if(2**i<N<=2**(i+1)):
        M = 2*i+1
        break
    i+=1
print(M)

l, r = 0, 0
judge = 1
for _ in range(M):
    mid = (l+r)//2
    if(judge):
        juice_l = [str(mid-l)] + [str(i) for i in range(l, mid)]
        print(''.join(juice_l))