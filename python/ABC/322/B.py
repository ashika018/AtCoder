N, M = list(map(int, input().split(' ')))
S = input()
T = input()

def f():
    if(S==T[:N] and S==T[M-N:]): return 0
    elif(S==T[:N]): return 1
    elif(S==T[M-N:]): return 2
    else: return 3

print(f())
