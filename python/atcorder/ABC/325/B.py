def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
d = dict([(i, 0) for i in range(24)])
for _ in range(N):
    W, X = ILI()
    for i in range(9, 18):
        hour = (i + X) % 24
        d[hour] += W

ans = 0
for hour, value in d.items():
    ans = max(ans, value)
print(ans)