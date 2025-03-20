N, H, X = [int(i) for i in input().split(' ')]
p_l = [int(i) for i in input().split(' ')]
for i, p in enumerate(p_l):
    if(p + H >= X):
        print(i + 1)
        break
