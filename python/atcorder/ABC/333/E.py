# 考察＋イモス法
def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# まず、すべてのポーションを拾うとして、モンスターを全て倒すことができるのか判定
# できない場合 → -1を出力してexit()
# できる場合 → 各ポーションを持っている時間が最短になるようにする。
# つまり、ポーションiを使うところから遡って、ポーションiを拾える地点の中から一番近い地点で拾うとすることでKminを達成する高橋くんの行動が確定
# 確定した高橋くんの行動から、Kminの計算にはイモス法を用いる

event_n = II()
tx_l = [ILI() for _ in range(event_n)]

# モンスターをすべて倒せるかどうかの判定
portions_d = dict([(i,0) for i in range(1, event_n+1)])
for l in tx_l:
    t_i, x_i = l
    if(t_i == 1):
        portions_d[x_i] += 1
    else:
        if(portions_d[x_i]>0):
            portions_d[x_i] -= 1
        else:
            print(-1)
            exit()

# 高橋くんの行動を確定させる
need_portion_d = dict([(i,0) for i in range(1, event_n+1)])
# pick_use_l: 行動iでポーションを拾う場合は1を、何もしない（拾わない）場合は0を、使う場合は-1を格納（イモス法用）
pick_use_l = [0 for _ in range(event_n+1)]
for i in range(len(tx_l)-1, -1, -1):
    t_i, x_i = tx_l[i]
    if(t_i==2):
        need_portion_d[x_i] += 1
        pick_use_l[i] = -1
    else:
        if(need_portion_d[x_i]>0):
            need_portion_d[x_i] -= 1
            pick_use_l[i] = 1

# イモス法
# イモス法の準備(+1と-1を入れていく)と高橋くんの行動をまとめる
itemnum_l = [0 for _ in range(event_n+1)]
behavior = []
for i in range(event_n):
    pickORuse = pick_use_l[i]
    if(pickORuse==1): 
        itemnum_l[i]+=1
        behavior.append(str(pickORuse))
    elif(pickORuse==-1): 
        itemnum_l[i+1]-=1
    else:
        behavior.append(str(pickORuse))
# 足し合わせていく
for i in range(1, len(itemnum_l)):
    itemnum_l[i] = itemnum_l[i-1]+itemnum_l[i]

# 回答
ans = max(itemnum_l)
print(ans)
print(' '.join(behavior))

