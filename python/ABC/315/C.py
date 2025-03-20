icecream_caps = int(input())
#flavor_taste_l = dict([input().split(' ') for i in range(icecream_caps)])
flavor_taste_l = []
for i in range(icecream_caps):
    flavor_taste = [int(j) for j in input().split(' ')]
    flavor_taste_l.append(flavor_taste)

sorted_l = sorted(flavor_taste_l, key = lambda x: x[1])
#print(sorted_l)
#print(sorted_l[-2::-1])
first_FT = sorted_l[-1]
second_DFT = [-1, -1]
second_SFT = [-1, -1]
for FT in sorted_l[-2::-1]:
    if((FT[0] != first_FT[0]) and (FT[1] > second_DFT[1])): second_DFT = FT
    if((FT[0] == first_FT[0]) and (FT[1] > second_SFT[1])): second_SFT = FT

print(int(first_FT[1] + max(second_DFT[1], second_SFT[1]/2)))