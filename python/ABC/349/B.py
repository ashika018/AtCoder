def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()

count_d = dict([(s,0) for s in list('abcdefghijklmnopqrstuvxwyz')])
for s in list(S):
    count_d[s] += 1

for i in range(1, 101):
    tmp = 0
    for s, cnt in count_d.items():
        if(i==cnt):
            tmp += 1
    if(tmp!=0 and tmp!=2):
        print('No')
        exit()

print('Yes')