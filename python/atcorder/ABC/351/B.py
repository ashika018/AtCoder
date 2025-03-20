def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
grid_A = [list(SI()) for _ in range(N)]
grid_B = [list(SI()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(grid_A[i][j]!=grid_B[i][j]):
            print(f'{i+1} {j+1}')
            exit()
