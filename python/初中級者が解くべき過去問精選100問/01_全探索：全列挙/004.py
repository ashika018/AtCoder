# 全列挙
# まず、M曲の中から2曲の選ぶ組み合わせは、MC2 = M(M-1)/2。高々、100*100通り
# 生徒の数が高々、100人であることを考慮すると
# 計算量の見積は、10000 * 100 = 10^6となり、間に合いそう

N_students, N_songs = list(map(int, input().split(' ')))
studentscore_l = [list(map(int, input().split(' '))) for _ in range(N_students)]

# 曲の組み合わせのパターンを列挙
songs_conbinations = [(songA_num, songB_num) for songA_num in range(0, N_songs-1) for songB_num in range(songA_num+1, N_songs)]

# 各歌の組み合わせに対して、得点を計算
max_score = 0
for songs_tuple in songs_conbinations:
    score = 0
    for i in studentscore_l:
        score += max(i[songs_tuple[0]], i[songs_tuple[1]])
    if(score > max_score): max_score = score

print(max_score)