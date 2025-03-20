N, M = list(map(int, input().split(' ')))
A_d = dict([(i, p) for i, p in enumerate(list(map(int, input().split(' '))))])
A_d = dict(sorted(A_d.items(), key = lambda x : x[1], reverse=True))
S_l = [list(input()) for _ in range(N)]

S_point_l = []
bonus = 0
for l in S_l:
    bonus += 1
    point = 0
    point += bonus
    for i, s in enumerate(l):
        if(s=='o'): point += A_d[i]

    S_point_l.append(point)

max_point = max(S_point_l)
for i, l in enumerate(S_l):
    ans = 0
    point = S_point_l[i]
    for k, v in A_d.items():
        if(max_point-point<=0): break
        else:
            if(l[k]=='x'): 
                point += v
                ans += 1
    print(ans)

