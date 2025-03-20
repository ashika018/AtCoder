def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
points_l = []
for _ in range(N):
    point = ILI()
    points_l.append(point)

for i in range(N):
    max_length = 0
    for j in range(N):
        p1, p2 = points_l[i], points_l[j]
        tmp_length = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        if(max_length<tmp_length):
            ans_p = j+1
            max_length = tmp_length
    print(ans_p)
