# 全探索（全列挙）
N, X = [int(i) for i in input().split(' ')]

ans = 0
for n_1 in range(1, N+1):
    for n_2 in range(n_1+1, N+1):
        n_3 = X-n_1-n_2
        if((n_2<n_3<= N)): #  and (n_3!=n_1) and (n_3!=n_2)
            print(f'n_1:{n_1}, n_2:{n_2}, n_3:{n_3}')
            ans += 1
print(ans)

