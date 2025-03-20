# マスの開き方は全部で9!通り。つまり、高々362880通り。
# 全探索で間に合いそう

grid_num = [list(map(int, input().split(' '))) for _ in range(3)]

# マス目の開ける順番に関するパターンをすべて列挙
from itertools import permutations
permutation_list = list(permutations(list(range(1, 10))))
point_dict = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

count = 0
for permutation in permutation_list:
    grid = [[0,0,0], [0,0,0], [0,0,0]]
    for i in permutation:
        x, y = point_dict[i]
        grid[x][y] = grid_num[x][y]
        if(grid[0][0]>0 and grid[0][1]>0 and grid[0][2]>0): # ０行目が全て入れ替わった
            if(x==0 and y==0):
                if(grid[0][1]==grid[0][2]): 
                    count += 1
                    break
            elif(x==0 and y==1):
                if(grid[0][0]==grid[0][2]): 
                    count += 1
                    break
            else:
                if(grid[0][1]==grid[0][0]): 
                    count += 1
                    break
        if(grid[1][0]>0 and grid[1][1]>0 and grid[1][2]>0): # 1行目が全て入れ替わった
            if(x==1 and y==0):
                if(grid[1][1]==grid[1][2]): 
                    count += 1
                    break
            elif(x==1 and y==1):
                if(grid[1][0]==grid[1][2]): 
                    count += 1
                    break
            else:
                if(grid[1][0]==grid[1][1]): 
                    count += 1
                    break
        if(grid[2][0]>0 and grid[2][1]>0 and grid[2][2]>0): # 2行目が全て入れ替わった
            if(x==2 and y==0):
                if(grid[2][1]==grid[2][2]): 
                    count += 1
                    break
            elif(x==2 and y==1):
                if(grid[2][0]==grid[2][2]): 
                    count += 1
                    break
            else:
                if(grid[2][0]==grid[2][1]): 
                    count += 1
                    break
        if(grid[0][0]>0 and grid[1][0]>0 and grid[2][0]>0): # 0列目が全て入れ替わった
            if(x==0 and y==0):
                if(grid[1][0]==grid[2][0]): 
                    count += 1
                    break
            elif(x==1 and y==0):
                if(grid[0][0]==grid[2][0]): 
                    count += 1
                    break
            else:
                if(grid[0][0]==grid[1][0]): 
                    count += 1
                    break
        if(grid[0][1]>0 and grid[1][1]>0 and grid[2][1]>0): # 1列目が全て入れ替わった
            if(x==0 and y==1):
                if(grid[1][1]==grid[2][1]): 
                    count += 1
                    break
            elif(x==1 and y==1):
                if(grid[0][1]==grid[2][1]): 
                    count += 1
                    break
            else:
                if(grid[0][1]==grid[1][1]): 
                    count += 1
                    break
        if(grid[0][2]>0 and grid[1][2]>0 and grid[2][2]>0): # 2列目が全て入れ替わった
            if(x==0 and y==2):
                if(grid[1][2]==grid[2][2]): 
                    count += 1
                    break
            elif(x==1 and y==2):
                if(grid[0][2]==grid[2][2]): 
                    count += 1
                    break
            else:
                if(grid[0][2]==grid[1][2]): 
                    count += 1
                    break
        if(grid[0][0]>0 and grid[1][1]>0 and grid[2][2]>0): # ナナメが全て入れ替わった
            if(x==0 and y==0):
                if(grid[1][1]==grid[2][2]): 
                    count += 1
                    break
            elif(x==1 and y==1):
                if(grid[0][0]==grid[2][2]): 
                    count += 1
                    break
            else:
                if(grid[0][0]==grid[1][1]): 
                    count += 1
                    break
        if(grid[0][2]>0 and grid[1][1]>0 and grid[2][0]>0): # ナナメが全て入れ替わった
            if(x==0 and y==2):
                if(grid[1][1]==grid[2][0]): 
                    count += 1
                    break
            elif(x==1 and y==1):
                if(grid[0][2]==grid[2][0]): 
                    count += 1
                    break
            else:
                if(grid[0][2]==grid[1][1]): 
                    count += 1
                    break

print(count)
ans = 1-(float(count)/float(len(permutation_list)))
print(ans)