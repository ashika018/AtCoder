def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

H, W, N = ILI()
T = list(SI())
grid_M = [list(SI()) for _ in range(H)]

d = {'L':(0,-1),'R':(0,1),'U':(-1, 0),'D':(1,0)}
def explore(r, c):
    for t in T:
        dr, dc = d[t]
        r += dr
        c += dc
        if(grid_M[r][c]=='#'):
            return False
    return True

ans = 0
for r in range(1, H-1):
    for c in range(1, W-1):
        if(grid_M[r][c]=='#'):
            continue
        if(explore(r=r, c=c)):
            ans += 1

print(ans)
