def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


H, W, K = ILI()
grid_map = [list(SI()) for _ in range(H)]


# 累積和（水平方向用と垂直方向用）を求めるリスト
O_map_h = [[0]*(W+1) for _ in range(H+1)]
O_map_v = [[0]*(W+1) for _ in range(H+1)]

dot_map_h = [[0]*(W+1) for _ in range(H+1)]
dot_map_v = [[0]*(W+1) for _ in range(H+1)]


# 累積和の+1, -1をセットしていく
for r in range(H):
    for c in range(W):
        if(grid_map[r][c]=='o'):
            O_map_h[r][c] += 1
            O_map_v[r][c] += 1
            c_ = c+K if(c+K<W) else W
            O_map_h[r][c_] -= 1
            r_ = r+K if(r+K<H) else H
            O_map_v[r_][c] -= 1

        if(grid_map[r][c]=='.'):
            O_map_h[r][c] += 1
            O_map_v[r][c] += 1
            c_ = c+K if(c+K<W) else W
            O_map_h[r][c_] -= 1
            r_ = r+K if(r+K<H) else H
            O_map_v[r_][c] -= 1

            dot_map_h[r][c] += 1
            dot_map_v[r][c] += 1
            c_ = c+K if(c+K<W) else W
            dot_map_h[r][c_] -= 1
            r_ = r+K if(r+K<H) else H
            dot_map_v[r_][c] -= 1


# 累積和の足し合わせを行う
for c in range(W):
    for r in range(H):
        O_map_h[r][c+1] += O_map_h[r][c]
        dot_map_h[r][c+1] += dot_map_h[r][c]

for r in range(H):
    for c in range(W):
        O_map_v[r+1][c] += O_map_v[r][c]
        dot_map_v[r+1][c] += dot_map_v[r][c]


# 答えの全探索
ans = float('inf')
for r in range(H):
    for c in range(W):
        if(O_map_h[r][c]>=K):
            ans = min(ans, dot_map_h[r][c])
        if(O_map_v[r][c]>=K):
            ans = min(ans, dot_map_v[r][c])

ans = -1 if(ans==float('inf')) else ans
print(ans)