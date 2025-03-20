# 動的計画法：ナップザックDP

N = int(input())
flag_map = [list('*'*(N+1))]+[['*']+list(input()) for _ in range(5)]
color_l = ['R', 'B', 'W']
color_d = {'R':0, 'B':1, 'W':2}
memory_field = [[0,0,0] for _ in range(N+1)]

# memory_field[1][*]は先に埋めておく。
for color in color_l:
    cnt = 0
    for i in range(1,6):
        if(flag_map[i][1]==color): cnt += 1
    memory_field[1][color_d[color]] = 5-cnt

for n in range(1,N):
    for color in color_l:
        cnt = 0
        for i in range(1,6):
            if(flag_map[i][n+1]==color): cnt += 1
        other_color_l = ['R', 'B', 'W']
        other_color_l.remove(color)
        c_1, c_2 = other_color_l[0], other_color_l[1]
        memory_field[n+1][color_d[color]] = min(memory_field[n][color_d[c_1]]+5-cnt, memory_field[n][color_d[c_2]]+5-cnt)

print(min(memory_field[-1]))