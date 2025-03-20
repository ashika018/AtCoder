def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


N = II()
S_l = [SI() for _ in range(N)]

ans = 0
for s in S_l:
    if(s=='Takahashi'):
        ans += 1
print(ans)