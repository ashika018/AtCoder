
N, Q = list(map(int, input().split(' ')))
S = input()
question_l = [list(map(int, input().split(' '))) for _ in range(Q)]

# i番目の要素が1→i+1番目とi番目の文字が同じ
ans_l = [0]
for i in range(1,N):
    if(S[i]==S[i-1]): ans_l.append(ans_l[i-1]+1)
    else: ans_l.append(ans_l[i-1])

for Q_l in question_l:
    start, end = Q_l
    ans = ans_l[end-1]-ans_l[start-1]
    print(ans)