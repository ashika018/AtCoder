# 全探索（全列挙）
N = int(input())

ans = 0

for odd in range(1, N+1, 2):
    divisors_n = 0
    for i in range(1, odd+1, 2):
        if(odd % i == 0): divisors_n += 1
    if(divisors_n == 8): ans += 1

print(ans)