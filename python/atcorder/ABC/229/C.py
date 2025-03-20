"""
n, w = input().split()  # nは入力回数
n, w = int(n), int(w)

num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))
ans = 0
while(w>0):
    cn = 0
    for i in range(n):
        #print(num_list)
        #print(i)
        if(num_list[i][0]>num_list[cn][0]): cn = i

    if(w - num_list[cn][1]>0):
        ans += num_list[cn][0]*num_list[cn][1]
        w -= num_list[cn][1]
        num_list.pop(cn)
        n = len(num_list)
    else:
        ans += num_list[cn][0]*w
        w -= num_list[cn][1]
        #n = len(num_list)
    
    if(len(num_list)==0): break

print(ans)
"""