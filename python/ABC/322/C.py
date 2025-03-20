N, M = list(map(int, input().split(' ')))
A_l = list(map(int, input().split(' ')))

def binary_search(left, right, target):
    if(A_l[left]>=target): return A_l[left]
    while(right-left>1):
        mid = (right+left)//2
        if(A_l[mid]>=target): right = mid
        else: left = mid
    return A_l[right]


for i in range(1, N+1):
    b = binary_search(0, M-1, i)
    # print(f'b:{b}, i:{i}')
    ans = b - i
    print(ans)