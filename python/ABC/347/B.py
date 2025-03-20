def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()

ans_l = []
l, dl = 0,1
while True:
    r = l+dl
    if(dl>len(S)):
        break
    if(r>len(S)):
        l = 0
        dl += 1
        continue
    ans_l.append(S[l:r])
    l += 1

ans = len(set(ans_l))
print(ans)
