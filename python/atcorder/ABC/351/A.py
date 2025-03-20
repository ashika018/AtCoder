def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

A_l = ILI()
B_l = ILI()

total_A = sum(A_l)
total_B = sum(B_l)

ans = (total_A-total_B+1)
print(ans)