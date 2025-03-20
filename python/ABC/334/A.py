bat_price, glove_price = list(map(int, input().split(' ')))
buy = max(bat_price, glove_price)
ans = 'Bat' if(buy==bat_price) else "Glove"
print(ans)