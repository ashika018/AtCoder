def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 深さ優先探索っぽい
import copy

N = int(input())
ans_map = [[-1 for _ in range(N+2)]]+[[-1]+[0]*N+[-1] for _ in range(N)]+[[-1 for _ in range(N+2)]]
# 渦巻き状に埋めていけば良い
d = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}
direction = 0
x, y = 1,1
i = 1
while True:
    ans_map[x][y] = i
    dx, dy = d[direction%4]
    if(ans_map[x+dx][y+dy]!=0): 
        direction+=1
        dx, dy = d[direction%4]
    x, y = x+dx, y+dy
    if(x==(N+1)//2 and y==(N+1)//2): 
        ans_map[x][y] = 'T'
        break
    i += 1

for i in range(1, N+1):
    l = ans_map[i][1:N+1]
    l = list(map(str, l))
    print(' '.join(l))
        
