def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
beans_color_d = {}

for _ in range(N):
    taste, color = ILI()
    if(color not in beans_color_d):
        beans_color_d[color] = [taste]
    else:
        beans_color_d[color].append(taste)

ans = 0
color_l = beans_color_d.keys()
for color, taste_l in beans_color_d.items():
    ans = max(ans, min(taste_l))

print(ans)
