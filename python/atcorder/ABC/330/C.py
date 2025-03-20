def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

D = II()
ans = 10*10

for x in range(int(D**0.5)+1):
    other = int(abs(D-x**2)**0.5)
    for y in range(other-5, other+5):
        ans = min(ans, abs(x**2+y**2-D))

print(ans)