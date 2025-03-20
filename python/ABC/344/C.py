def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
A = ILI()

M = II()
B = ILI()
        
L = II()
C = ILI()

ABC = []
for a in A:
    for b in B:
        for c in C:
            ABC.append(a+b+c)
ABC.sort()
# print(ABC)


def binary_search(l, r, x):
    while(r-l>1):
        mid = (l+r)//2
        if(ABC[mid]<=x): l = mid
        else: r = mid
        if(ABC[mid]==x):
            break
    return l


Q = II()
X = ILI()
for x in X:
    i = binary_search(l=0, r=len(ABC), x=x)
    if(ABC[i]==x):
        print('Yes')
    else:
        print('No')


