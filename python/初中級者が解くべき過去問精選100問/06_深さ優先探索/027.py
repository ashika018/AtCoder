# 深さ優先探索

# 木構造以外の深さ優先探索
import sys
sys.setrecursionlimit(int(1E+7))
# 多次元リストをコピーするときはcopy.deepcopyを使うべし
import copy

east_west_blocks = int(input())
south_north_blocks = int(input())
blocks_map = [list(map(int, input().split(' '))) for _ in range(south_north_blocks)]

def check_xy(x, y):
    return (0<=x<south_north_blocks) and (0<=y<east_west_blocks)

# x, yから始まるルートのうち、最大の長さを返す関数
def DFS(x, y):
    if((not check_xy(x,y)) or (blocks_map[x][y]==0)): return 0
    else:
        blocks_map[x][y] = 0
        a = DFS(x-1,y)
        b = DFS(x+1,y)
        c = DFS(x,y-1)
        d = DFS(x,y+1)
        ans =  1+max(a,b,c,d)
        blocks_map[x][y] = 1
        return ans


max_route = 0
for i in range(south_north_blocks):
    for j in range(east_west_blocks):
        # blocks_map_n = copy.deepcopy(blocks_map) ← こいつが悪さをしていたみたい、、。なんでWAだったか不明、、。
        tmp_route = DFS(i, j)
        max_route = max(max_route, tmp_route)

print(max_route)
