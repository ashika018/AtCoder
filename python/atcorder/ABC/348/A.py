def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()

ans = ''
for i in range(1, N+1):
    tmp = 'o' if(i%3!=0) else 'x'
    ans += tmp

print(ans)

