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

sorted_A = sorted(A)
sorted_sumA = [0]
total=0
for a in sorted_A[::-1]:
    total+=a
    sorted_sumA.append(total)
sorted_sumA = sorted_sumA[::-1]
# print(sorted_sumA)

def binary_search(l,r,key):
    while(abs(r-l)>1):
        mid = (r+l)//2
        if(sorted_A[mid]<=key): l=mid
        else: r=mid
    return l

ans_l = []
for a in A:
    index = binary_search(l=0, r=len(sorted_A), key=a)
    ans_l.append(str(sorted_sumA[index+1]))

print(' '.join(ans_l))