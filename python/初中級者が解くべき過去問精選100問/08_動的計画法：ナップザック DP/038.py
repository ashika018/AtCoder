# 動的計画法：ナップザック DP
# 参考；http://www.sakurai.comp.ae.keio.ac.jp/classes/algorithms-class/2003/11Knapsack.pdf

n = int(input())
ans_l = []

for _ in range(n):
    X = input()
    Y = input()
    memory_fields = [[0]*(len(X)+1) for _ in range(len(Y)+1)]
    max_length = 0
    for y in range(1, len(Y)+1):
        for x in range(1, len(X)+1):
            option_l = []
            option1 = memory_fields[y][x-1]
            option2 = memory_fields[y-1][x]
            option_l.append(option1)
            option_l.append(option2)
            if(X[x-1]==Y[y-1]):
                option3 = memory_fields[y-1][x-1]+1
                option_l.append(option3)
            memory_fields[y][x] = max(option_l)
            max_length = max(max_length, memory_fields[y][x])
    ans_l.append(max_length)

for ans in ans_l: print(ans)
