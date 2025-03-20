def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()

bit = ''
while True:
    if(N==1):
        break
    if(N%2==1):
        bit = '1' + bit
    else:
        bit = '0' + bit
    N = N//2

# print(bit)
ans = 0
for i in range(len(bit)-1, -1, -1):
    if(bit[i]=='1'):
        break
    ans += 1

print(ans)