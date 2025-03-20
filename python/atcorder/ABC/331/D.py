def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, Q = ILI()
color_map = [ILI() for _ in range(N)]

for _ in range(Q):
    A,B,C,D = ILI()
    