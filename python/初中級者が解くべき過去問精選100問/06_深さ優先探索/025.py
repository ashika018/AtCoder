# 深さ優先探索

width, height = list(map(int, input().split(' ')))
map_l = [list(map(int, input().split(' '))) for _ in range(height)]

visited_map = [[0]*width for _ in range(height)]

# DFSの定義
# 入力x, yに対して、そこが海か陸かをまず判定。
# 陸だった場合、どこまでと続きの陸か探索し、訪れたところにフラグをたて置く。
# 海にぶつかったら、return で探索終了する
def DFS(x, y):
    if(map_l[x][y]==0): return
    else:
        map_l[x][y] = -1 # 訪れたことを示すためのフラグ(1が陸、0が海、-1が探索済み)
        dxdy_l = [[x+dx, y+dy] for dx in range(-1, 2) for dy in range(-1, 2) if((0<=x+dx<height) and (0<=y+dy<width))]
        for l in dxdy_l:
            nx, ny = l
            if(map_l[nx][ny]!=-1): _ = DFS(nx, ny)

ans = 0
for w in range(width):
    for h in range(height):
        if(map_l[h][w] == 1):
            DFS(h, w)
            ans += 1

print(ans)