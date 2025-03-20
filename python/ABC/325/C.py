def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 深さ優先探索
import sys
sys.setrecursionlimit(10**6)

H, W = ILI()
sensor_map = [list(SI()) for _ in range(H)]

def DFS(x, y):
    if(sensor_map[x][y]=='.'):
        return
    else:
        sensor_map[x][y] = '.'
        dxdy_l = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,1), (1,0), (1,-1)]
        for dx, dy in dxdy_l:
            nx, ny = x+dx, y+dy
            #  and sensor_map[nx][ny]=='#' 無しだと、普通にTLEしていた
            if(0<=nx<H and 0<=ny<W and sensor_map[nx][ny]=='#'):
                _ = DFS(nx, ny)

ans = 0
for r in range(H):
    for c in range(W):
        if(sensor_map[r][c]=='#'):
            ans += 1
            _ = DFS(r, c)

print(ans)