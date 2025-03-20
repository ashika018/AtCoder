def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 全探索すれば間に合う

A = [ILI() for _ in range(9)]

# 各行のチェック
for r in range(9):
    d = dict([(i,0) for i in range(1,10)])
    for c in range(9):
        if(d[A[r][c]]!=0):
            print('No')
            exit()
        else:
            d[A[r][c]] +=1

# 各列のチェック
for c in range(9):
    d = dict([(i,0) for i in range(1,10)])
    for r in range(9):
        if(d[A[r][c]]!=0):
            print('No')
            exit()
        else:
            d[A[r][c]] +=1

# 3×3のブロックを確認していく
# i = 0, 3, 6
for i in range(0, 7, 3):
    for j in range(0, 7, 3):
        d = dict([(i,0) for i in range(1,10)])
        for r in range(i, i+3):
            for c in range(j, j+3):
                if(d[A[r][c]]!=0):
                    print('No')
                    exit()
                else:
                    d[A[r][c]] +=1
print('Yes')
