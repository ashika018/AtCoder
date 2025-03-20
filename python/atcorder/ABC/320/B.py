S = input()

max_len = 0
for i in range(0, len(S)):
    for j in range(i+1, len(S)+1):
        part_s = S[i:j]
        if(part_s==part_s[::-1]): max_len = max(max_len, len(part_s))
print(max_len)