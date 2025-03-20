N = int(input())
S = input()

def f():
    for i in range(N):
        if(i == N-2): return -1
        if(S[i]=='A' and S[i+1]=='B' and S[i+2]=='C'): return i+1

print(f())