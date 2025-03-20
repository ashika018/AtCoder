# 動的計画法：ナップザック DP
# https://docs.google.com/spreadsheets/d/1rfkWdLoGFr0PJHveAZVE1AiWTiLjZaWq_SP7eC54TEQ/edit
# 上記ページで手で動かしてみたが、なんかアルゴリズムが間違ってそう。。
N = int(input())
numbers_l = list(map(int, input().split(' ')))

target = numbers_l[-1]

memory_fields = [[0]*21 for _ in range(N)]
memory_fields[0][0] = 1

for i in range(1, N):
    n = numbers_l[i-1]
    print(n)
    for j in range(0, 21):
        if(0<=j-n): memory_fields[i][j] += memory_fields[i-1][j-n]
        if(j+n<=20): memory_fields[i][j] += memory_fields[i-1][j+n]
        if(n==0): memory_fields[i][j] -= memory_fields[i-1][j+n]

print(memory_fields[-1][target])
'''
for l in memory_fields:
    print(l)
'''