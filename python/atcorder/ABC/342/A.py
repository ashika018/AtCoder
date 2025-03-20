def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()

for i in range(len(S)-2):
    j, h = i+1, i+2
    if(S[i]!=S[j] and S[i]!=S[h]):
        ans = i+1
        break
    if(S[j]!=S[i] and S[j]!=S[h]):
        ans = j+1
        break
    if(S[h]!=S[i] and S[h]!=S[j]):
        ans = h+1
        break

print(ans)