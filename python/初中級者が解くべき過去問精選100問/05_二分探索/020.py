# 二分探索

# パーツの数が10**5であることから、A,B,Cのパーツの組み合わせは10**15通りとなり、到底間に合わない。
# パーツBに対して、for文を回し,
# [パーツBより真に小さいパーツAの個数]*[パーツBより真に大きいパーツCの個数]を足し合わせていく
# すると計算量は、NlogNとなり、大丈夫そう
import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
    a = bisect.bisect_left(A, b) # 挿入点はどの同じ値よりも左
    c = bisect.bisect_right(C, b) # 挿入点はどの同じ値よりも右
    ans += a * (len(C)-c)
print (ans)