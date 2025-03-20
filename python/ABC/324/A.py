N = int(input())
A_l = list(map(int, input().split(' ')))

ans = 'Yes'
for a in A_l:
    if(a != A_l[0]): ans = 'No'

print(ans)