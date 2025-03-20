N = int(input())
S_l = [list(input()) for _ in range(N)]

d = dict((str(i+1), 0) for i in range(N))

for i in range(N):
    l = S_l[i]
    for j in l:
        if(j == 'o'): d[str(i+1)] += 1

ans_l = dict(sorted(d.items(), key = lambda x : x[1], reverse=True)).keys()

print(' '.join(ans_l))

