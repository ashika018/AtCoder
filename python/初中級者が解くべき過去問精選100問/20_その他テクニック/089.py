# その他テクニック（圧縮）
lamp_n = int(input())
lamp_flashing_state_l = list(map(int, input().split(' ')))

# 圧縮：compression
length = 1
compressed_l = []

# 交互列の長さをカウントし、圧縮したリストに格納していく
for i in range(1, len(lamp_flashing_state_l)):
    if(lamp_flashing_state_l[i-1]==lamp_flashing_state_l[i]):
        compressed_l.append(length)
        length = 1
    else:
        length+=1
compressed_l.append(length)

# 圧縮したリストの長さが3以下であれば、その和が求める最大値になる
if(len(compressed_l)<=3):
    print(sum(compressed_l))
    exit()

# 最大値の探索
# 圧縮したリストの要素を前から三つずつ足していき、その輪の最大値が求めるans
ans = 0
for i in range(1, len(compressed_l)-1):
    ans = max(ans, compressed_l[i-1]+compressed_l[i]+compressed_l[i+1])
print(ans)