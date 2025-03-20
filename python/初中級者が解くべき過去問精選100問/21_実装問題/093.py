# 実装問題
import copy

height, width, K = list(map(int, input().split(' ')))
puzzle_M = [list(map(int, list(input()))) for _ in range(height)]

# 同じ数が連続して何個続いているのかをカウントする関数
def count_consecutive(l, i):
    if(i>=len(l)-1 or l[i]!=l[i+1]):
        return 1
    if(l[i]==l[i+1]):
        return count_consecutive(l, i+1) + 1

# STEP1：K個以上連続するpuzzle_Mの数字を消滅させる（0で置き換える）関数
# 出力：新しいpuzzle_M, point
def step1(puzzle_M):
    point = 0
    for row, l in enumerate(puzzle_M):
        col = 0
        # 同じ行に消滅する数字が複数ある場合に対応するために、forではなくwhile
        # 例：K=3の時、[4,6,3,3,3,5,9,8,8,8,2,2,2,2,2]
        while(col<width):
            consecutive_n = count_consecutive(l, col)
            if(consecutive_n>=K):
                point += l[col]*consecutive_n
                puzzle_M[row] = puzzle_M[row][:col] + [0]*consecutive_n + puzzle_M[row][col+consecutive_n:]
            col += consecutive_n
    return puzzle_M, point

# STEP2：消滅した部分を下に詰めていく
# 出力：新しいpuzzle_M
def step2(puzzle_M):
    N_puzzle_M = [[0 for _ in range(width)] for _ in range(height)]
    for col in range(width):
        i = 0
        for row in range(height-1, -1, -1):
            if(puzzle_M[row][col]==0):
                i+=1
            else:
                N_puzzle_M[row+i][col] = puzzle_M[row][col]
    return N_puzzle_M

# STEP3：STEP1,２を繰り返す関数
# 出力：total point
def step3(puzzle_M):
    step_n = 0
    total_point = 0
    while True:
        puzzle_M, tmp_point = step1(puzzle_M)
        total_point+=tmp_point*(2**step_n)
        if(tmp_point==0): break
        puzzle_M = step2(puzzle_M)
        step_n += 1
    return total_point

# どのマスを最初に消すと点数が高いか全探索
ans = 0
for row in range(height):
    for col in range(width):
        copy_puzzle_M = copy.deepcopy(puzzle_M)
        copy_puzzle_M[row][col] = 0
        copy_puzzle_M = step2(copy_puzzle_M)
        ans = max(ans, step3(copy_puzzle_M))
print(ans)

