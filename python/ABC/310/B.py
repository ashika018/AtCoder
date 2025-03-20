NM = input().split(" ")
N, M = int(NM[0]), int(NM[1])

products_l = []
for _ in range(N):
    products_l.append([int(i) for i in input().split(" ")])

ans = 0

for i in range(N):
    for j in range(i+1, N):
        productA = products_l[i]
        A_price, A_funNums, A_funs = productA[0], productA[1], set(productA[2:])
        productB = products_l[j]
        B_price, B_funNums, B_funs = productB[0], productB[1], set(productB[2:])
        #AがBの上位互換
        print(f"")
        if((A_price<=B_price) and (B_funs <= A_funs) and ((A_price < B_price) or (B_funs < A_funs))):
            ans += 1
        
        if((A_price>=B_price) and (A_funs <= B_funs) and ((A_price > B_price) or (B_funs > A_funs))):
            ans += 1


if(ans>0): print("Yes")
else: print("No")