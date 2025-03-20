def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, K = ILI()
A_l = ILI()

ans_l = []
for a in A_l:
    if(a%K==0):
        ans_l.append(str(a//K))

ans = ' '.join(ans_l)
print(ans)