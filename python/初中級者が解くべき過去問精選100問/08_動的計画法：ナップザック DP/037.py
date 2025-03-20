# 動的計画法：ナップザック DP
# 参考ページ：https://kunassy.com/python_dp_bubunwa/#toc1

total_price, coin_n = list(map(int, input().split(' ')))
coin_l = [0]+list(map(int, input().split(' ')))

memory_fields = [[0]+[10**10]*(total_price) for _ in range(coin_n+1)]

def dp(i, price):
    coin = coin_l[i]
    option1 = memory_fields[i-1][price]
    if(price-coin<0): memory_fields[i][price] = option1
    else: 
        option2 = memory_fields[i-1][price-coin] + 1
        memory_fields[i][price] = min(option1, option2)


for i in range(1, coin_n+1):
    for price in range(1, total_price+1):
        dp(i=i, price=price)


print(memory_fields[coin_n][price])