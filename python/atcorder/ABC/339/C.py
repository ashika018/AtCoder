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

start_passengers, total = 0, 0
for a in A_l:
    total += a
    if(total<0):
        start_passengers = min(start_passengers, total)

ans = -start_passengers+sum(A_l)
print(ans)