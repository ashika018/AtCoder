def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()
l = S.split('|')
ans = l[0]+l[2]
print(ans)