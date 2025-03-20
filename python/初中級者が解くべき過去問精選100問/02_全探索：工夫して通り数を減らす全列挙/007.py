# 全探索：工夫して通り数を減らす全列挙
def I(): return int(input())
def TI(): return tuple(map(int,input().split()))
n = I()
xy = [TI() for _ in range(n)]
set_xy = set(xy)
ans = 0
for i in range(n):
    x1,y1 = xy[i]
    for j in range(i+1,n):
        x2,y2 = xy[j]
        vectorx,vectory = x2-x1,y2-y1
        if (x1-vectory,y1+vectorx) in set_xy and (x2-vectory,y2+vectorx) in set_xy:
            ans = max(ans,vectorx**2+vectory**2)
print(ans)
