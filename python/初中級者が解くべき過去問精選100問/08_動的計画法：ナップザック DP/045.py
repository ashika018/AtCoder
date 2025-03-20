# 動的計画法：ナップザックDP

# 行にnを、列にコードブックの要素をとるmemory_fieldsを考える。
# 1<=n<=20000, 1<=len(コードブック)<=16であるから、memory_fieldsの要素数は最大で32*(10^4)
# さらに一つ上の段から最小を計算する際に、一つ上の段の全ての要素を閲覧するので、そこでかかる計算量はlen(コードブック)<=16
# よって、この計算にかかる最大の計算量は、32*(10^4)*16 = 5.12*10^6

x_num, codebook_length = list(map(int, input().split(' ')))
codebook = [int(input()) for _ in range(codebook_length)]
xn_l = [0]+[int(input()) for _ in range(x_num)]

dp = [[[0,0]]*codebook_length for _ in range(x_num+1)]
# n=0だけ代入しておく
for i in range(codebook_length): dp[0][i][1] = 128

for n in range(1, x_num+1):
    for codebook_i in range(codebook_length):
        # minを見つける
        min_sum = 10000000000000000000000
        for i in range(codebook_length):
            yn = dp[n-1][i][1]+codebook[codebook_i]
            if(yn<0): yn = 0
            if(yn>255): yn = 255
            tmp = (yn-xn_l[n])**2+dp[n-1][i][0]
            if(tmp<min_sum):
                min_y = yn
                min_sum = tmp
        dp[n][codebook_i] = [min_sum, min_y]

ans_l = []
for l in dp[-1]: ans_l.append(l[0])
print(min(ans_l))







