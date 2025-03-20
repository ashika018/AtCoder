def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

B = II()

for i in range(1, 20):
    tmp = i**i
    if(tmp==B):
        print(i)
        exit()
print(-1)