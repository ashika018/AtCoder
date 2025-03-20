def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II() - 1
sinsuu_5 = ''
while True:
    if(N==0): break
    s = str(N%5)
    sinsuu_5 = s+sinsuu_5
    N = N//5

ans = ''

for i in range(len(sinsuu_5)):
    judge = False
    ans = ans + str(2*int(sinsuu_5[i]))

ans = '0' if(ans=='') else ans
print(int(ans))
