# 幅優先探索

# ネズミはチーズを食べるごとに体力が1上昇する。
# チーズの硬さは1~Nであり、自分の体力より硬いチーズは食べることができない。
# → チーズの硬さ = 食べるチーズの順番
# つまり、S→硬さ1のチーズ→硬さ2のチーズ→...→硬さNのチーズと移動していくのが、最短時間。
from collections import deque

height, width, N = list(map(int, input().split(' ')))
city_map = [['X']*(width+2)]+[['X']+list(input())+['X'] for _ in range(height)]+[['X']*(width+2)]

for i in range(len(city_map)):
    if('S' in city_map[i]):
        r = i
        c = city_map[i].index('S')


def BFS(start_r, start_c, goal, step_n):
    queue = deque([])
    queue.append([start_r, start_c])
    step_map = [[-1]*(width+2) for _ in range(height+2)]
    step_map[start_r][start_c] = step_n

    while queue:
        r, c = queue.popleft()
        if(city_map[r][c]=='X'): continue
        else:
            delta_l = [[-1,0], [1,0], [0,-1], [0,1]]
            for delta in delta_l:
                dr, dc = delta
                if(step_map[r+dr][c+dc]>-1 or city_map[r+dr][c+dc]=='X'): continue
                else: 
                    step_map[r+dr][c+dc] = 1+step_map[r][c]
                    queue.append([r+dr, c+dc])
                    if(city_map[r+dr][c+dc]==str(goal)): return [step_map[r+dr][c+dc], r+dr, c+dc]


step_n = 0
for i in range(1, N+1):
    step_n, r, c = BFS(r, c, str(i), step_n)

print(step_n)