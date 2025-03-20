def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
A_l = ILI()

# l_fromL[i]：A_lのi番目の要素から左肩下がりの階段を作る時、作ることのできる最大の段数
l_fromL = []
i, n = 0, float('inf')
while(i < len(A_l)):
    if(n<A_l[i]):
        n += 1
    else:
        n = A_l[i]
        # n = min(A_l[i], i+1)
    l_fromL.append(n)
    i += 1

# l_fromR[i]：A_lのi番目の要素から右肩下がりの階段を作る時、作ることのできる最大の段数
l_fromR = []
i, n = len(A_l)-1, float('inf')
while(i >= 0):
    if(n<A_l[i]):
        n += 1
    else:
        n = A_l[i]
        # n = min(A_l[i], len(A_l)-i)
    l_fromR.append(n)
    i -= 1
l_fromR.reverse()

# tmp：A_lのi番目の要素をピラミッドの中央とした時に作ることのできる、ピラミッドの大きさ
ans = 0
for i in range(len(l_fromL)):
    tmp = min(l_fromL[i], l_fromR[i])
    ans = max(ans, tmp)

print(ans)
