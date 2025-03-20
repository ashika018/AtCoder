N = input()
l = list(N)
ans = 0
for i in range(len(l)-1):
    if(int(l[i])>int(l[i+1])):
        ans+=1
if(ans==len(l)-1): print('Yes')
else:print('No')
