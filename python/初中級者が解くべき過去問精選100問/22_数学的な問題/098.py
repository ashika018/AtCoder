# 数学的な問題
# 参考：https://kakedashi-engineer.appspot.com/2020/06/04/sumitrust2019e/

people_n = int(input())
A_l = list(map(int, input().split(' ')))
MOD = 1000000007 

ans = 1
cnt_people_l = [0, 0, 0]
for n in A_l:
    cap_color_l = []
    for i in range(3):
        if(cnt_people_l[i]==n):
            cap_color_l.append(i)
    # i番目の人がいうようなパターンが存在しない場合
    if(len(cap_color_l)==0):
        print(0)
        exit()
    ans *= len(cap_color_l)
    ans %= MOD
    cnt_people_l[cap_color_l[0]] += 1

print(ans)