def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 新しい頭の座標をリストの後ろに追加していく
# l[-i] : パーツiの座標　とする
# つまり、新しい、パーツ1の位置をappendしていく

N, Q = ILI()
d = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
l = [(i, 0) for i in range(N, 0, -1)]

move_n = 0
for _ in range(Q):
    input1, input2 = SLI()
    if(input1 == '1'):
        xd, yd = d[input2]
        l.append((l[-1][0]+xd, l[-1][1]+yd))
    else:
        input2 = int(input2)
        x, y = l[0-input2]
        print(f'{x} {y}')
    # print(l)