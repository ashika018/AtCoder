# 二分探索
s_len = int(input())
s = sorted(list(map(int, input().split(' '))))
t_len = int(input())
t = list(map(int, input().split(' ')))


def binary_search(data, target):
    left, right = 0, len(data)-1
    while left <= right:
        mid = (left+right)//2
        if(data[mid]==target): return 1
        elif(data[mid]<target): left = mid + 1
        else: right = mid -1
    return 0

ans = 0
for i in t:
    ans += binary_search(s, i)
print(ans)