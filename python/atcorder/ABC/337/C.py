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


d = {}
for i, a in enumerate(A_l):
    d[a] = i+1

person = d[-1]
ans_l = [str(person)]
while True:
    if(person not in d):
        break
    n_person = d[person]
    ans_l.append(str(n_person))
    person = n_person

ans = ' '.join(ans_l)
print(ans)
