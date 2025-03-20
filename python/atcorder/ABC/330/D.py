def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()

r_d = dict([(i,0) for i in range(N)])
c_d = dict([(i,0) for i in range(N)])

S_map = [list(SI()) for _ in range(N)]

for i in range(N):
    r,c = 0, 0
    for j in range(N):
        if(S_map[i][j]=='o'): r+=1 
        if(S_map[j][i]=='o'): c+=1
    r_d[i] = r
    c_d[i] = c



ans = 0
for row in range(N):
    for col in range(N):
        if(r_d[row]!=0 and c_d[col]!=0 and S_map[row][col]=='o'): ans+=(r_d[row]-1)*(c_d[col]-1)

print(ans)