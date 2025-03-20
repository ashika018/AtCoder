def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')


# 入力の受け取り
H, W = ILI()
grid = [['x' for _ in range(W+2)]]+[['x']+list(SI())+['x'] for _ in range(H)]+[['x' for _ in range(W+2)]]

# 磁石の周りをマーキング（'o'）
for r in range(1,H+1):
    for c in range(1,W+1):
        if(grid[r][c]=='#'):
            drdc_l = [(i,j) for i in range(-1,2) for j in range(-1,2)]
            for dr, dc in drdc_l:
                if(1<=r+dr<=H and 1<=c+dc<=W):
                    grid[r+dr][c+dc] = 'o'

visited_flg = [[True for _ in range(W+2)] for _ in range(H+2)]
# 'x'→立ち入り禁止、'#'→磁石、'o'→磁石によって影響を受けるポイント
# x, yから始まるルートのうち、最大の長さを返す関数
def DFS(r, c):
    print(f'(r,c)=({r},{c})')
    if(grid[r][c]=='x' or grid[r][c]=='#'): return 0
    elif(grid[r][c]=='o'): return 1
    else:
        visited_flg[r][c] = False
        ans = 1
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            if((visited_flg[r+dr][c+dc]) or (grid[r+dr][c+dc]=='o')):
                ans += DFS(r+dr, c+dc)
        return ans

ans = -1
for r in range(1, H+1):
    for c in range(1,W+1):
        if(grid[r][c]=='.' and visited_flg[r][c]):
            print(DFS(r,c))
            ans = max(ans, DFS(r,c))
print(ans)

for l in visited_flg:
    print(l)