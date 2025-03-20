def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

s1, s2 = list(input())
t1, t2 = list(input())

d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
s_d = abs(d[s1]-d[s2])
t_d = abs(d[t1]-d[t2])

ans='No'
if((s_d==1 or s_d==4) and (t_d==1 or t_d==4)): ans='Yes'
if((s_d==2 or s_d==3) and (t_d==2 or t_d==3)): ans='Yes'
print(ans)