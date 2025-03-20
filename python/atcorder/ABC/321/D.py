import sys
input = sys.stdin.readline
N, M, P = list(map(int, input().split(' ')))
A_l = list(map(int, input().split(' ')))
B_l = list(map(int, input().split(' ')))
B_l.sort()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# コンテスト後追加部分

# 副菜0~副菜jまでの値段の合計を先に計算して、リストにまとめておくことでpoint1の部分を高速化できる。
# 計算量をN**2からNlogNにするための工夫
sum_l = [0 for _ in range(M+1)]
for i in range(M):
    sum_l[i+1] = sum_l[i] + B_l[i]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 主菜i に対して、主菜の値段+副菜の値段>Pとなるような副菜jの位置を見つける二分探索
def binary_search(left, right, i):
    if(i + B_l[-1] < P): return len(B_l)
    if(i + B_l[0] > P): return 0
    while right-left >1:
        mid = (right+left)//2
        if(B_l[mid]+i >= P): right = mid
        else: left = mid
    return right

total = 0
for i in A_l:
    j = binary_search(0, len(B_l), i)
    # total += i*j + sum(B_l[:j]) ← point1；ここがTLEの原因
    total += i*j + sum_l[j]
    total += (P)*(len(B_l)-j)

print(total)