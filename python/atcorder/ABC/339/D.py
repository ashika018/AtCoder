def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 最初の発想
# player1, player2の場所の組み合わせが限られているのえ、それらを全列挙し、
# それをノードとするようなグラフを作成し全探索すれば良い！というもの。
# → player1, 2を区別するかしないか、二つの座標の組み合わせをどう表すかでごちゃごちゃする。→結局できなかった。

# 普通に、グリッド上の全探索で良いのでは？？
# ただ、探索するマップは4次元（player1のx,yとplayer2のx,y）となる


# ライブラリのインポート
from collections import deque


# 入力の受け取り
N = II()
grid = [['#' for _ in range(N+2)]]+[['#']+list(SI())+['#'] for _ in range(N)] + [['#' for _ in range(N+2)]]


# 初期位置を取得
start_pos = []
for r in range(1, N+1):
    for c in range(1, N+1):
        if(grid[r][c]=='P'):
            start_pos.append((r,c))
pos1, pos2 = start_pos


# グラフを幅優先探索
def judge(x,y):
    return grid[x][y]!='#'

def BFS(start_pos1=pos1, start_pos2=pos2):
    start_x1, start_y1 = start_pos1
    start_x2, start_y2 = start_pos2
    step_num_d = [[[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    step_num_d[start_x1][start_y1][start_x2][start_y2] = 0

    queue = deque([])
    queue.append([start_pos1, start_pos2])
    while queue:
        pos1, pos2 = queue.popleft()
        x1, y1 = pos1
        x2, y2 = pos2
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            n_x1, n_y1 = (x1+dx, y1+dy) if(judge(x1+dx, y1+dy)) else (x1, y1)
            n_x2, n_y2 = (x2+dx, y2+dy) if(judge(x2+dx, y2+dy)) else (x2, y2)

            if(step_num_d[n_x1][n_y1][n_x2][n_y2]>=0): continue
            step_num_d[n_x1][n_y1][n_x2][n_y2] = 1+step_num_d[x1][y1][x2][y2]
            queue.append([(n_x1, n_y1), (n_x2, n_y2)])

            if((n_x1, n_y1)==(n_x2, n_y2)):
                return step_num_d[n_x1][n_y1][n_x2][n_y2]

    return -1

# ans
ans = BFS()
print(ans)