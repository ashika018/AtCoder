def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 再起的に計算する
# ただ、一度計算したものをキャッシュしておくメモ化再帰じゃないとめちゃくちゃ時間がかかる

from functools import cache

N = II()

@cache
def cal(n):
    if(n<=1):
        return 0
    else:
        if(n%2==1):
            n1, n2 = n//2, n//2+1
        else:
            n1, n2 = n//2, n//2
        return n + cal(n1) + cal(n2)

print(cal(n=N))





"""
N =II()
num_l = [N]
pay = 0
i = 0
while num_l:
    print(num_l)
    x = num_l.pop()

    half_x = x/2
    if(half_x != x//2):
        x1, x2 = x//2, x//2+1
    else:
        x1, x2 = int(half_x), int(half_x)
    if(x1 > 1):
        num_l.append(x1)
    if(x2 > 1):
        num_l.append(x2)
    
    pay += x
    i+=1
print(pay)
"""
