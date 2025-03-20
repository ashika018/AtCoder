# 動的計画法：bit DP
# すごい参考になった。→https://qiita.com/karutetto332/items/90fc8186c915afd1e9e8

# V:頂点, E:辺
V_num, E_num = list(map(int, input().split(' ')))

# 有向グラフを二次元配列で格納」
graph_M = [[10**10]*V_num for _ in range(V_num)]
for _ in range(E_num):
    s,t,d = list(map(int, input().split(' ')))
    graph_M[s][t] = d

# DPテーブルの作成
# dp[S][v]→{0,1,2,..,n-1}の部分集合Sを巡回する|S|!通りの経路の中で、最後に頂点vに到達するもののうち、最短ルートの距離を表す
dp = [[10**10]*V_num for _ in range(2**V_num)]
# 頂点0から出発することにする
# {}==0, {0}=1, {1}=10,...より、dp[{0}][0] = dp[1][0]
dp[1][0] = 0

# dpを回していく部分
for subset in range(1, 2**V_num):
    for v in range(V_num):
        for k in range(V_num):
            # subsetにvが含まれているかの判定
            # 頂点vに訪れたことがあるかの判定
            # subsetのv桁目が1であるかどうか
            # 頂点kに訪れたことがあり、頂点vには訪れたことがないか
            if((subset>>k & 1 ==1) and (subset>>v & 1 != 1)):
                # new_subset = subset ∪ {v}
                # つまり、subsetのk桁目を1にする
                new_subset = subset | 1<<v
                dp[new_subset][v] = min(dp[new_subset][v], dp[subset][k]+graph_M[k][v])

# 最後に頂点0に戻るコストも追加
ans = min([dp[(2**V_num)-1][v]+graph_M[v][0] for v in range(V_num)])
# 巡回経路が存在しなければ-1
if(ans>10**10): ans = -1

print(ans)
