M = int(input())
s1 = input()
s2 = input()
s3 = input()
s_l = [s1, s2, s3]
# 揃える文字列の候補は10通り
# リールを止める順番は3!なので、6パターン
# つまり、60通り全探索すれば良いのではないか
import itertools

def f(s_l):
    min_t = 10000000000000000000000
    for i in range(10):
        for permuted_tuple in itertools.permutations(range(3)):
            t = 0
            for j in permuted_tuple:
                s = s_l[j]
                if(str(i) not in s): 
                    t = 10000000000000000000000
                    break
                else:
                    while True:
                        if(s[t%M]==str(i)):
                            t += 1
                            break
                        else: t += 1
            min_t = min(min_t, t)
    return min_t

ans = f(s_l)
if(ans==10000000000000000000000): print(-1)
else: print(ans-1)

