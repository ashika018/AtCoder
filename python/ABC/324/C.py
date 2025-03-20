def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, T_ = SLI()
N = int(N)
S_l = [SI() for _ in range(N)]

ans_l = []
for i, S in enumerate(S_l):
    l, r = 0, 0
    while(l<min(len(S), len(T_))):
        if(T_[l]==S[l]):
            l += 1
        else:
            break
    while(r<min(len(S), len(T_))):
        if(T_[-1-r]==S[-1-r]):
            r += 1
        else:
            break
    if((len(T_)==len(S)) and (l==r==len(T_))):
        ans_l.append(str(i+1))
    elif((len(S)==len(T_)-1) and (l+r>=len(S))):
        ans_l.append(str(i+1)) 
    elif((len(S)-1==len(T_)) and (l+r>=len(T_))):
        ans_l.append(str(i+1))
    elif((len(S)==len(T_)) and (l+r==len(S)-1)):
        ans_l.append(str(i+1))
    else: continue

print(len(ans_l))
ans_s = ' '.join(ans_l)
print(ans_s)
