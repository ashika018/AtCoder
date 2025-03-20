def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# マージテク
# データ構造をマージする一般的なテクニック

N, Q = ILI()
C_l = [0]+ILI()
C_l = [set([i]) for i in C_l]

for _ in range(Q):
    a, b = ILI()
    set_a, set_b = C_l[a], C_l[b]
    # 小さい方の集合を大きい方の集合に移動させてマージしていくことで、計算量が削減できる
    if(len(set_a)<len(set_b)):
        set_b |= set_a
        set_a, set_b = set([]), set_b
    else:
        set_a |= set_b
        set_a, set_b = set([]), set_a
    print(len(set_b))
    C_l[a], C_l[b] = set_a, set_b

