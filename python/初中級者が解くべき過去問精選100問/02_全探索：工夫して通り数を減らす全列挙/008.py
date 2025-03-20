# 全探索：工夫して通り数を減らす全列挙

# 入口と出口の候補はA1,A2,...,An,B1,B2,...,Bnのいずれかなので、
# (入口, 出口)の組み合わせの数は高々、60C2 = 60*59/2通りである。
# この中で、最も移動距離が小さくなるものを選べば良い。

N = int(input())
ab_l = [list(map(int, input().split(' '))) for _ in range(N)]


#入り口と出口を受け取り、移動距離の総和を返す関数
#対称性より、 entrance < exit としても一般性を失わない
def move_length(entrance, exit):
    ans = 0
    for i in ab_l:
        if(entrance<=i[0] and i[1]<=exit): ans += exit - entrance
        elif(i[0]<entrance and i[1]<=exit): ans += exit - i[0] + entrance - i[0]
        elif(entrance<=i[0] and exit<i[1]): ans += i[1] - entrance + i[1] - exit
        else: ans += i[1] - i[0] + i[1] - exit + entrance - i[0]
    return ans



#まず、[Ai, Bj]の二次元配列ab_p_lを作る
abp_l = [[ab_l[i][0], ab_l[j][1]] for i in range(N) for j in range(N)]

ans = 1000000000000000000000000
for k in abp_l:
    ans = min(ans, move_length(k[0], k[1]))

print(ans)
