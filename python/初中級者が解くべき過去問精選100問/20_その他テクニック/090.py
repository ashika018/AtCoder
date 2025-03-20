# その他テクニック（単純な幾何計算）
# https://kakedashi-engineer.appspot.com/2020/05/14/s8pc5b/

N, M = list(map(int, input().split(' ')))
N_circle_l = [list(map(int, input().split(' '))) for _ in range(N)]
M_circle_l = [list(map(int, input().split(' '))) for _ in range(M)]
INF = float('inf')

# 2点間の距離を計算
def cal_distance(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return(((x1-x2)**2+(y1-y2)**2)**0.5)

# M個の円の2点間距離の中で、最初なものを見つける
tmp1 = INF
for i in range(len(M_circle_l)-1):
    for j in range(i+1, len(M_circle_l)):
        xy1, xy2 = M_circle_l[i], M_circle_l[j]
        tmp1 = min(tmp1, cal_distance(xy1,xy2)/2)

# N個の円とM個の円について。
tmp2 = INF
for xy1 in M_circle_l:
    for N_circle in N_circle_l:
        xy2, r2 = N_circle[:2], N_circle[2]
        tmp2 = min(tmp2, cal_distance(xy1, xy2)-r2)

# N個の円の中で半径が最小のものを見つける
tmp3 = INF
if(len(N_circle_l)>0):
    tmp3 = min([N_circle_l[i][2] for i in range(len(N_circle_l))])

ans = min(tmp1, tmp2, tmp3)
print(ans)
