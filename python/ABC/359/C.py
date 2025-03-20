def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

start_x, start_y = ILI()
goal_x, goal_y = ILI()
# そもそも同じタイルに入っている時
if(goal_y==start_y):
    if((start_x+start_y)%2==1):
        tmp_start_x = start_x-1
    else:
        tmp_start_x = start_x
    if((goal_x+goal_y)%2==1):
        tmp_goal_x = goal_x-1
    else:
        tmp_goal_x = goal_x
    if(tmp_goal_x==tmp_start_x):
        print(0)
        exit()
# ゴールがスタートより左側にある時
if(goal_x<start_x):
    if((start_x+start_y)%2==1):
        start_x -= 1
    if((goal_x+goal_y)%2==0):
        goal_x += 1

    dx = abs(start_x-goal_x)
    dy = abs(start_y-goal_y)
    if(dx<=dy):
        print(dy)
        exit()
    else:
        print((dx-dy)//2+dy+1)
        exit()
# ゴールがスタートより右側にある場合
elif(start_x<goal_x):
    if((start_x+start_y)%2==0):
        start_x += 1
    if((goal_x+goal_y)%2==1):
        goal_x -= 1

    dx = abs(start_x-goal_x)
    dy = abs(start_y-goal_y)
    if(dx<=dy):
        print(dy)
        exit()
    else:
        print((dx-dy)//2+dy+1)
        exit()
# ゴールとスタートのx軸が同じの時
else:
    print(abs(start_y-goal_y))
    exit()