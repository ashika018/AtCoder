# 全探索：工夫して通り数を減らす全列挙
import math
import sys

point_num = int(input())
point_l = [tuple(map(int, input().split(' '))) for _ in range(point_num)]

# 2点の組み合わせを列挙する
points_pair_l = [[point_l[i], point_l[j]] for i in range(0, len(point_l)-1) for j in range(i+1,len(point_l))]

points_set = set(point_l)
max_area = 0


for points_pair in points_pair_l:
    x1, y1 = points_pair[0]
    x2, y2 = points_pair[1]

    # 垂直ベクトの計算
    vVector_x, vVector_y = -(y2-y1), x2-x1
    # d = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 正方形の頂点の場所を推定
    x3_p, y3_p, x4_p, y4_p = x1+vVector_x, y1+vVector_y, x2+vVector_x, y2+vVector_y
    x3_m, y3_m, x4_m, y4_m = x1-vVector_x, y1-vVector_y, x2-vVector_x, y2-vVector_y

    # 推定した点の位置に柱が存在するのかを確認
    if(({(x3_p, y3_p), (x4_p, y4_p)}.issubset(points_set)) or ({(x3_m, y3_m), (x4_m, y4_m)}.issubset(points_set))):
        area = vVector_x**2 + vVector_y**2
        if(area > max_area): max_area = area

print(max_area)