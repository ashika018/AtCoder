# 二分探索

# 風船の数がN個であり、N<10**5であるので、
# 最大で10**5以内には全ての風船を打ち終える
# さらに、風船の上がっていく速度は最大で10**9であるから
# 風船の最高到達点は」10**14となる
# 1~10**14のリストに対して、全ての風船を割ることのできる最小の高さを二分探索で探すことで、この問題は解けそう？
# 計算量としてはlogNなので、Maxで14ステップくらい！ → こう見ると、二分探索は偉大ですな、、


num_balloons = int(input())
balloons_info_l = [list(map(int, input().split(' '))) for _ in range(num_balloons)]

# 風船たちが与えられた高さhまでに全て破ることができるか判定する関数
def can_pop_balloons(height):
    # print('star')
    popping_deadlines_l = sorted([(height - balloon_info[0])//balloon_info[1] for balloon_info in balloons_info_l])
    # print(popping_deadlines_l)
    for i, deadline in enumerate(popping_deadlines_l):
        if(i > deadline): return False
    return True

def binary_search(left, right):
    while(right-left > 1):
        mid = (left+right) // 2
        # print(f'-----------------------\nright: {right}, left: {left}')
        # print(mid)
        if(can_pop_balloons(mid)): right = mid
        else: left = mid
    return right

print(binary_search(0, 10**14))