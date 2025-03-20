def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

H, W, N = ILI()
map_M = [['.' for _ in range(W)] for _ in range(H)]

direction_d = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

i = 0
row, col = 0, 0
for _ in range(N):
    # print(f'(row,col)=({row},{col})')
    if(map_M[row][col]=='.'):
        map_M[row][col]='#'
        i+=1
        d_r, d_c = direction_d[i%4]
    else:
        map_M[row][col]='.'
        i-=1
        d_r, d_c = direction_d[i%4]
    row, col = (row+d_r)%H, (col+d_c)%W
    

for l in map_M:
    s = ''.join(l)
    print(s)