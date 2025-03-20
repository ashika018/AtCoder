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

dic = dict([(s,s) for s in list('abcdefghijklmnopqrstuvxwyz')])
Q = II()
for _ in range(Q):
    c, d = SLI()
    for k, v in dic.items():
        if(v==c):
            dic[k] = d

ans_s = ''
for s in list(S):
    ans_s+=dic[s]

print(ans_s)