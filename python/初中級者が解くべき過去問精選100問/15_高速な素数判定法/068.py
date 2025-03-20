# 高速な素数判定法
# 参考ページ：https://qiita.com/drken/items/a14e9af0ca2d857dad23

n = int(input())
k = n

root_k = int(k**0.5)
ans_l = []
i = 2
while i<=root_k:
    if(k%i==0):
        while(k%i==0):
            k = k/i
            ans_l.append(str(i))
    i += 1

s = ' '.join(ans_l)
print(f'{n}: {s}')