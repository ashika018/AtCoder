# 全探索：bit全探索

# 議員の数がNであり、それぞれの人について、「選ぶor選ばない」の2通りの選択肢が存在。
# 派閥の組み方はbit全探索で表すことができそう。
# N < 12であることからも余裕かな

num_members, num_relationships = list(map(int, input().split(' ')))
relationship_set = set([input() for _ in range(num_relationships)])

# bit全探索
max_members = 0
for i in range(2**num_members):
    group_relationship_l = []
    for j in range(num_members-1):
        if((i>>j) & 1):
            for k in range(j+1, num_members):
                if((i>>k) & 1):
                    group_relationship_l.append(str(j+1) + ' ' + str(k+1))
    if(set(group_relationship_l) <= relationship_set):
        max_members = max(max_members, sum([(i>>j) & 1 for j in range(num_members)]))

print(max_members)

# 計算量としては、(2**12)*(12*11/2)*(部分集合かどうかの判定の計算量) < 33万*(部分集合かどうかの判定の計算量)