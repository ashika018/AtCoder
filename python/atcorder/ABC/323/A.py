S = input()

ans = 0
for i in range(1, len(S), 2):
    if(S[i]==str(1)): ans+=1

if(ans>0): print('No')
else:print('Yes')