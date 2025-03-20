def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

def binary_search(l,r,Bi):
    if(A_l[l]>=Bi):
        return l
    if(A_l[-1]<Bi):
        print(-1)
        exit()

    while(r-l>1):
        mid = (l+r)//2
        if(A_l[mid]<Bi):
            l = mid
        else:
            r = mid
    return r

N, M = ILI()
A_l = ILI()
A_l.sort()
B_l = ILI()
B_l.sort()

ans, l, r = 0, 0, N

for Bi in B_l:
    if(l>=N):
        print(-1)
        exit()
    k = binary_search(l=l,r=r,Bi=Bi)
    ans += A_l[k]
    l = k+1


print(ans)