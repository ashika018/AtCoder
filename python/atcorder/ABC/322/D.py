def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 全探索
import math

# 各ポリオミノの左上のブロックを基準(0,0)として、その他のブロックの相対座標を求める関数
def make_polyomino():
    polyomino = []
    judge = True
    for r in range(4):
        s = SI()
        for c in range(4):
            if(s[c]=='#'):
                if(judge):
                    base_c, base_r = c, r
                    judge = False
                polyomino.append((r-base_r, c-base_c))
    return polyomino

polyomino1 = make_polyomino()
polyomino2 = make_polyomino()
polyomino3 = make_polyomino()


# 座標の回転を行う関数
def rotate_point(xy, theta):
    x, y = xy
    theta = math.radians(theta)
    sin_theta, cos_theta = math.sin(theta), math.cos(theta) 
    return_x = int(round(x*cos_theta-y*sin_theta, 0))
    return_y = int(round(x*sin_theta+y*cos_theta, 0))
    return (return_x, return_y)

d_polyomino1 = {0:polyomino1, 1:[rotate_point(xy=xy, theta=90) for xy in polyomino1], 2:[rotate_point(xy=xy, theta=180) for xy in polyomino1], 3:[rotate_point(xy=xy, theta=270) for xy in polyomino1]}
d_polyomino2 = {0:polyomino2, 1:[rotate_point(xy=xy, theta=90) for xy in polyomino2], 2:[rotate_point(xy=xy, theta=180) for xy in polyomino2], 3:[rotate_point(xy=xy, theta=270) for xy in polyomino2]}
d_polyomino3 = {0:polyomino3, 1:[rotate_point(xy=xy, theta=90) for xy in polyomino3], 2:[rotate_point(xy=xy, theta=180) for xy in polyomino3], 3:[rotate_point(xy=xy, theta=270) for xy in polyomino3]}


rc_l = [(i,j) for i in range(4) for j in range(4)]
ans_set = set(rc_l)

for r1,c1 in rc_l:
    for i1 in range(4):
        point_l1 = []
        for xy1 in d_polyomino1[i1]:
            x1, y1 = r1+xy1[0], c1+xy1[1]
            if(not(0<=x1<=3) or not(0<=y1<=3)):
                break
            point_l1.append((x1,y1))

        for r2,c2 in rc_l:
            for i2 in range(4):
                point_l2 = point_l1.copy()
                for xy2 in d_polyomino2[i2]:
                    x2, y2 = r2+xy2[0], c2+xy2[1]
                    if(not(0<=x2<=3) or not(0<=y2<=3)):
                        break
                    point_l2.append((x2,y2))

                for r3,c3 in rc_l:
                    for i3 in range(4):
                        point_l3 = point_l2.copy()
                        for xy3 in d_polyomino3[i3]:
                            x3, y3 = r3+xy3[0], c3+xy3[1]
                            if(not(0<=x3<=3) or not(0<=y3<=3)):
                                break
                            point_l3.append((x3,y3))
                        
                        point_set = set([])
                        judge = True
                        for t in point_l3:
                            if(t in point_set):
                                judge = False
                            point_set = point_set | set([t])
                        
                        if(judge and point_set==ans_set):
                            print('Yes')
                            exit()



print('No')