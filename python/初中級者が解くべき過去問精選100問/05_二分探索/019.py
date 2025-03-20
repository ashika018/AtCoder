# 二分探索

road_length = int(input()) # d
shop_num = int(input()) # n
order_num = int(input()) # m
shop_location_l = sorted([0]+[int(input()) for i in range(shop_num-1)]+[road_length])
# print(shop_location_l)
order_location_l = [int(input()) for i in range(order_num)]
# print('#################################################')
def binary_search(left, right, target):
    mid = (left+right)//2

    if(shop_location_l[mid]<=target<=shop_location_l[mid+1]): return min(target-shop_location_l[mid], shop_location_l[mid+1]-target)
    elif(shop_location_l[mid+1]<target): return binary_search(mid+1, right, target)
    else: return binary_search(left, mid, target)


total_length = 0
for order_location in order_location_l:
    total_length += binary_search(left=0, right=shop_num-1, target=order_location)
print(total_length)