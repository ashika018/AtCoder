# 全探索：順列全探索
import itertools

N = int(input())
p = int(''.join(input().split(' ')))
q = int(''.join(input().split(' ')))


key_l = []
for permuted_tuple in itertools.permutations(range(1, N+1)):
    # tuple型はイミュータブル（不可変）なデータ型なので、一度リストにしないとjoinとかを使うことができない
    # joinは文字列のリストにしか適応できない
    n = int(''.join([str(i) for i in list(permuted_tuple)]))
    key_l.append(n)

key_l.sort()
d = {key_l[i]: i for i in range(len(key_l))}

print(max(d[p]-d[q], d[q]-d[p]))