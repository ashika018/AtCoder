# 全探索：工夫して通り数を減らす全列挙

# ピザの注文パターンの全組み合わせは、AピザをX枚、BピザをY枚、ABピザを０枚買うパターンから、
# ABピザを2枚ずつ増やしていき、Aピザ・Bピザを1枚ずつ減らしていく。
# これをAピザ・Bピザともに0枚になるまで続けると、考えられるすべての組み合わせが列挙できる
# 計算量は、max(必要なAピザの枚数, 必要なBピザの枚数)に比例するから、高々10^5

A_price, B_price, AB_price, A_needed, B_needed = list(map(int, input('').split(' ')))

# ピザの注文パターンの全列挙
pizza_combination = []
A_quantity, B_quantity, AB_quantity = A_needed, B_needed, 0
while True:
    pizza_combination.append([A_quantity, B_quantity, AB_quantity])
    if(A_quantity==0 and B_quantity==0): break
    A_quantity = max(A_quantity-1, 0)
    B_quantity = max(B_quantity-1, 0)
    AB_quantity += 2

# 料金の計算
min_price = 10000000000000000000000000000000
for i in pizza_combination:
    total_price = A_price*i[0] + B_price*i[1] + AB_price*i[2]
    if(total_price < min_price): min_price = total_price

print(min_price)