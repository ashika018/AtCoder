def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


N, S, K = ILI()
ans = 0
for _ in range(N):
    Pi,Qi = ILI()
    ans += Pi*Qi

if(ans<S): ans += K

print(ans)