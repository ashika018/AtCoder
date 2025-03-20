def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, T = ILI()

players_point = [0 for _ in range(N+1)]
points_distriburion = {0:N}

ans = 1
ans_l = []
for _ in range(T):
    player, pls = ILI()
    prev_point = players_point[player]
    new_point = prev_point + pls
    players_point[player] = new_point

    points_distriburion[prev_point] -= 1
    if(new_point not in points_distriburion):
        points_distriburion[new_point] = 1
    else:
        points_distriburion[new_point] += 1


    if(points_distriburion[prev_point]==0 and points_distriburion[new_point]>1):
        ans -= 1
    elif(points_distriburion[prev_point]>0 and points_distriburion[new_point]==1):
        ans += 1
    else:
        ans = ans

    ans_l.append(ans)

for ans in ans_l:
    print(ans)