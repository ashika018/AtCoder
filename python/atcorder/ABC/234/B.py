N = int(input())
xy_l = [list(map(int, input().split())) for _ in range(N)]


#2点の組み合わせを全て作る
ans = []
for i in range(N):
    for j in range(i+1, N):
        dx = xy_l[i][0] - xy_l[j][0]
        dy = xy_l[i][1] - xy_l[j][1]
        ans.append((dx**2+dy**2)**0.5)
print(max(ans))

