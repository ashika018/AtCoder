def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

S = SI()

d = {'A':0, 'B':1, 'C':2}

for i in range(len(S)-1):
    s1, s2 = S[i], S[i+1]
    if(d[s1] > d[s2]):
        print('No')
        exit()

print('Yes')