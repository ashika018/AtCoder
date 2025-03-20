A, M, L, R = list(map(int, input().split(' ')))
l = L-A
r = R-A
print(r//M - (l-1)//M)