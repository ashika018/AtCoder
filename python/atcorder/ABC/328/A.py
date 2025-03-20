N, X = list(map(int, input().split(' ')))
S_l = list(map(int, input().split(' ')))

print(sum([s for s in S_l if s<=X]))