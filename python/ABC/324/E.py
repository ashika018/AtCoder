def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 考察
# A：まず、S1~Snの各文字列を先頭から見ていき、文字列Tの先頭何文字分が含まれているかをカウント
# B：次に、S1~Snの各文字列を末尾から見ていき、文字列Tの末尾何文字分が含まれているかをカウント
# A[i]+b[j] >= len(T)となる(i,j)の組み合わせの数を確認する

N, T = SLI()
N = int(N)
S_l = [SI() for _ in range(N)]


# A, Bの計算
A_l = []
for string in S_l:
    i = 0
    for character in list(string):
        if(i==len(T)):
            break
        if(character==T[i]):
            i += 1
    A_l.append(i)

B_l = []
for string in S_l:
    i = 0
    str_l = list(string)
    str_l.reverse()
    for character in str_l:
        if(i==len(T)):
            break
        if(character==T[-1-i]):
            i += 1
    B_l.append(i)


# A[i]+b[j] >= len(T)となる(i,j)の組み合わせの数を確認
def binary_search(l, r, key):
    while(r-l>1):
        mid = (l+r)//2
        if(B_l[mid]<key): l = mid
        else: r = mid
    return l+1

A_l.sort()
B_l.sort()

ans = 0
for a in A_l:
    if(B_l[0]+a >= len(T)):
        ans += len(B_l)
        continue
    tmp = len(B_l) - binary_search(0, len(B_l), len(T)-a)
    ans += tmp

print(ans)