# 全探索：工夫して通り数を減らす全列挙

# 暗証番号のパターン数は、高々N(N-1)(N-2)/6 通り。
# ただし、N<=30000 であるから、到底間に合わない
# そもそも各桁0~9の10通りで、3桁であるから、高々10^3通り。
# これらの各組み合わせについて、実現可能かどうか全探索するのが良い

N = int(input())
S = input()

# 暗証番号のすべての組み合わせを列挙
key_combinations = [str(i)+str(j)+str(k) for i in range(10) for j in range(10) for k in range(10)]

# ある暗証番号がS内に存在するかどうかを判断する関数
def key_check(key):
    i = 0
    j = 0
    while i < N:
        if(S[i] == key[j]):
            j += 1
            if(j==3): return 1
        i += 1
    return 0

# 暗証番号の数をカウントしていく
total_keys_num = 0
for key in key_combinations:
    total_keys_num += key_check(key)
print(total_keys_num)
