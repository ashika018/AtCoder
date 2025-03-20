def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# N < 10^18より、N以下の立方数は高々10^6個しかない
# → 各立方数が回文であるかの判定はO(10)でいける
# → 全探索

N = II()

candidates = []
for num in range(10**6+1, 0, -1):
    tmp = str(num**3)
    flg = True
    for i in range(len(tmp)//2):
        if(tmp[i]!=tmp[-1-i]):
            flg = False
            break
    if(flg): 
        candidates.append(int(tmp))


for num in candidates:
    if(num<=N):
        print(num)
        break