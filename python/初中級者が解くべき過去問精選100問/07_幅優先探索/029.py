# 幅優先探索

from collections import deque

row_n, col_n = list(map(int, input().split(' ')))
start_y, start_x = list(map(int, input().split(' ')))
goal_y, goal_x = list(map(int, input().split(' ')))

maze_map = [list(input()) for _ in range(row_n)]
step_num_map = [[0]*col_n for _ in range(row_n)]

def BFS(start_x, start_y, goal_x, goal_y):
    dxdy_l = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque([])
    step_num_map[start_y-1][start_x-1] = 1
    queue.append([start_y-1, start_x-1])
    while queue:
        y, x = queue.popleft()
        if(maze_map[y][x]=='#'): continue
        else:
            for dxdy in dxdy_l:
                dy, dx = dxdy
                if(step_num_map[y+dy][x+dx]>0 or maze_map[y+dy][x+dx]=='#'):continue
                else:
                    step_num_map[y+dy][x+dx] = step_num_map[y][x]+1
                    queue.append([y+dy, x+dx])
    return step_num_map[goal_y-1][goal_x-1]-1


print(BFS(start_x, start_y, goal_x, goal_y))