def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()
d = dict([(s,0) for s in list('abcdefghijklmnopqrstuvxwyz')])
for s in list(S): d[s] += 1


cnt = 0
alphabet = ''
for s in d.keys():
    if(d[s]>cnt):
        alphabet = s
        cnt = d[s]


print(alphabet)