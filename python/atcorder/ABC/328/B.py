N = int(input())
D = list(map(int, input().split(' ')))

ans = 0
for i in range(1,N+1):
    for j in range(1,D[i-1]+1):
        if((set(list(str(i)))==set(list(str(j)))) and (len(set(list(str(i))))==1)): ans+=1

print(ans)