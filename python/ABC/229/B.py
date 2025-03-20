A,B = input().split()
A_list, B_list = list(str(A)), list(str(B))
a, b = len(A_list), len(B_list)

ans = 0
for i in range(min(a, b)):
    if(int(A_list[a-1])+int(B_list[b-1])>9): ans+=1
    a -= 1
    b -= 1
if(ans == 0): print("Easy")
else: print("Hard")
    