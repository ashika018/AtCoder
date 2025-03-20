# 実装問題
height = int(input())
puzzle_M = [list(map(int, input().split(' '))) for _ in range(height)]

# STEP1：puzzle_Mの数字を消滅させる（0で置き換える）関数
# 出力：True or False, 新しいpuzzle_M, point
def step1(puzzle_M):
    point = 0
    boolean = False
    for i, l in enumerate(puzzle_M):
        if(l[0]==l[1]==l[2]==l[3]==l[4] and l[0]!=0):
            point += l[2]*5
            puzzle_M[i] = [0,0,0,0,0]
        elif(l[0]==l[1]==l[2]==l[3] and l[0]!=0):
            point += l[2]*4
            puzzle_M[i] = [0,0,0,0,l[4]]
        elif(l[1]==l[2]==l[3]==l[4] and l[1]!=0):
            point += l[2]*4
            puzzle_M[i] = [l[0],0,0,0,0]
        elif(l[0]==l[1]==l[2] and l[0]!=0):
            point += l[2]*3
            puzzle_M[i] = [0,0,0,l[3],l[4]]
        elif(l[1]==l[2]==l[3] and l[1]!=0):
            point += l[2]*3
            puzzle_M[i] = [l[0],0,0,0,l[4]]
        elif(l[2]==l[3]==l[4] and l[2]!=0):
            point += l[2]*3
            puzzle_M[i] = [l[0],l[1],0,0,0]
        else:
            point += 0
    if(point>0):
        boolean = True
    return boolean, puzzle_M, point

# STEP2：消滅した部分を下に詰めていく
# 出力：新しいpuzzle_M
def step2(puzzle_M):
    r, h = len(puzzle_M[0]), len(puzzle_M)
    N_puzzle_M = [[0 for _ in range(r)] for _ in range(h)]
    for col in range(5):
        i = 0
        for row in range(height-1, -1, -1):
            if(puzzle_M[row][col]==0):
                i+=1
            else:
                N_puzzle_M[row+i][col] = puzzle_M[row][col]
    return N_puzzle_M

total_point = 0
while True:
    boolean, puzzle_M, tmp_point = step1(puzzle_M)
    total_point+=tmp_point
    if(not boolean): break
    puzzle_M = step2(puzzle_M)

print(total_point)