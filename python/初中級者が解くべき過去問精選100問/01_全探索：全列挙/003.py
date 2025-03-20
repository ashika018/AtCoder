# 全探索
# 考えられる文字列の総数は、文字列の長さをNとすると、N+1C2 + 1 = 1 + (N+1)N/2通り

S = input()
S_len = len(list(S))
# 部分文字列の全列挙
# リストの内包表記で二重for文を作るときは、普段と同じ順番で書く。つまり、
# for i in range(0, S_len):
#   for j in range(i+1, S_len+1):
#     all_substrings.append(S[i:j])
# と等しい。
all_substrings = [S[i:j] for i in range(0, S_len) for j in range(i+1, S_len+1)]
# print(all_substrings)

# ACGT文字列かどうかの確認
max_len = 0
for substring in all_substrings:
    if(set(substring) <= set('ACGT')): 
        if(max_len < len(substring)): max_len = len(substring)

print(max_len)