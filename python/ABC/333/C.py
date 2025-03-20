def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
ans_l = []
# 20個の数字の中から3つ取り出す組み合わせを全列挙
# 20C3 = 4000くらい
for i in range(20):
    for j in range(i, 20):
        for k in range(j, 20):
            n1 = int(''.join(['1' for _ in range(i+1)]))
            n2 = int(''.join(['1' for _ in range(j+1)]))
            n3 = int(''.join(['1' for _ in range(k+1)]))
            ans_l.append(n1+n2+n3)
ans_l.sort()
# print(ans_l[:10])
print(ans_l[N-1])

