def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

ans_l = []
while True:
    Ai = II()
    ans_l.append(Ai)
    if(Ai==0):
        break

for i in range(len(ans_l)-1, -1, -1):
    print(ans_l[i])