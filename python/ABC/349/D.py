def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

L, R = ILI()

tmp = L
ans_l = []
while True:
    # tmp = (2**degree) * (何か)
    # 右と同様 → while(tmp%(2**i)==0 and tmp+(2**i)<=R): degree = i
    for i in range(61):
        if(tmp%(2**i)==0 and tmp+(2**i)<=R):
            degree = i
        else:
            break

    ans_l.append((tmp, tmp+2**degree))
    tmp = tmp + 2**degree
    if(tmp==R):
        break

print(len(ans_l))
for l,r in ans_l:
    print(f'{l} {r}')
