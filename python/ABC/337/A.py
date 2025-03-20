def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
X_sum, Y_sum = 0, 0

for _ in range(N):
    X, Y = ILI()
    X_sum += X
    Y_sum += Y

if(X_sum>Y_sum): ans = 'Takahashi'
elif(X_sum<Y_sum): ans = 'Aoki'
else: ans = 'Draw'

print(ans)