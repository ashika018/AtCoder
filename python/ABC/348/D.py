def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

from collections import deque

H, W = ILI()
map_M = [['#' for _ in range(W+2)]]+[list('#'+SI()+'#') for _ in range(H)]+[['#' for _ in range(W+2)]]
N = II()

medicine_M = [[0 for _ in range(W+2)] for _ in range(H+2)]
for _ in range(N):
    r, c, e = ILI()
    medicine_M[r][c] = e

hitpoint_M = [[0 for _ in range(W+2)] for _ in range(H+2)]

for r in range(H+2):
    for c in range(W+2):
        if(map_M[r][c]=='S'):
            start_r, start_c = r, c
        if(map_M[r][c]=='T'):
            goal_r, goal_c = r, c

# for l in map_M: print(l)
# for l in medicine_M: print(l)
# print(f'start:{start_r},{start_c}')

ans = 'No'
hit_point = 0
queue = deque([])
queue.append([start_r, start_c])
while queue:
    r, c = queue.popleft()
    hit_point = hitpoint_M[r][c]
    if(map_M[r][c]=='T'): 
        ans = 'Yes'
        break
    hit_point = max(hit_point, medicine_M[r][c])
    if(hit_point==0 or map_M[r][c]=='#'): continue
    else:
        map_M[r][c]=='#'
        delta_l = [[-1,0], [1,0], [0,-1], [0,1]]
        for delta in delta_l:
            dr, dc = delta
            if(map_M[r+dr][c+dc]=='#'): continue
            hitpoint_M[r+dr][c+dc] = hit_point-1
            queue.append([r+dr, c+dc])

print(ans)