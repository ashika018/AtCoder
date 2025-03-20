def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
A_l = ILI()
pos_d = {}

for i, a in enumerate(A_l):
    pos_d[a] = i

ans_l = []
for i in range(1, N):
    tmp = A_l[i-1]
    # print(f'(pos_d[tmp],pos_d[i])=({pos_d[tmp]},{pos_d[i]})')
    # print(f'(tmp,i)=({tmp},{i})')
    if((pos_d[tmp]<pos_d[i]) and (tmp>i)):
        ans_l.append((pos_d[tmp], pos_d[i]))
        pos_d[i], pos_d[tmp] = pos_d[tmp], pos_d[i]
        A_l[pos_d[tmp]] = tmp

print(len(ans_l))
for t in ans_l:
    print(f'{t[0]+1} {t[1]+1}')
# print(pos_d)