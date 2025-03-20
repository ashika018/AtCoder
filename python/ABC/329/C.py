def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
S = SI()

# 各小文字がmaxで何回連続していたかをカウントして、保存しておけば良い
d = dict([(s, 0) for s in list('abcdefghijklmnopqrstuvxwyz')])
s = S[0]
d[s] += 1
i, cnt = 1, 1
while(i<N):
    if(S[i]!=S[i-1]):
        cnt = 1
        s = S[i]
    else:
        cnt += 1
    d[s] = max(d[s], cnt)
    i+=1

ans = 0
for _, v in d.items():
    ans += v
print(ans)