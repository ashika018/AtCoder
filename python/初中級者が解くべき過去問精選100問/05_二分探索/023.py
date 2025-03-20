# 二分探索

# 投げないという選択肢については、0点という的があると考えることで対処可能

# まず、境界値Mまでのすべての自然数に対して、その点数を生成できるかどうかを全探索するのはムリ(M < 10**8)
# 次に、4回投げた得点パターンについて全探索を行うのは、N**4の計算量となり破滅
# では、二分探索を考える。
# 3回投げる全パターンについて全探索を行い、最後の一回について二分探索で、Mを超えないギリギリの値を探すというのは、
# 計算量がN**3logNとなりアウト
# より計算量を減らす方法として、ダーツを2本ずつまとめて一本のダーツと考える。
# すると、2本のダーツを1本にまとめた得点のパターンはN**2通り。
# 一本は全探索で、もう一本を二分探索することで、計算量はN**2log(N**2) = 2*(N**2)logNとなり、O(N**2logN)で計算できる

import bisect


points_num, point_limit = list(map(int, input().split(' ')))
points_l = [0] + [int(input()) for _ in range(points_num)]

new_points_l = [p1 + p2 for p1 in points_l for p2 in points_l]
new_points_l.sort()


def binary_search(left, right, point_now, point_limit=point_limit):
    while(right - left > 1):
        mid = (left+right)//2
        if(point_now + new_points_l[mid] <= point_limit): left = mid
        else: right = mid-1
    return new_points_l[left] + point_now

max_point = 0
for point in new_points_l:
    if(point>point_limit): break
    # tmp_point = binary_search(0, len(new_points_l)-1, point, point_limit)
    tmp_point = point+new_points_l[bisect.bisect(new_points_l, point_limit-point)-1]
    max_point = max(tmp_point, max_point)

print(max_point)

# 2023/09/19 16:32 自作のbinary_searchを使うと、正しい答えは求められているが、TLEしてしまう
# 2023/09/19 16:32 bisectを使ってみると、時間内に収まった。
