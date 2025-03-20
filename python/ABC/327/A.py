def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
s = SI()

for i in range(N-1):
    if((s[i]=='a' and s[i+1]=='b') or (s[i]=='b' and s[i+1]=='a')):
        print('Yes')
        exit()
print('No')