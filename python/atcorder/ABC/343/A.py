def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

A, B = ILI()

for i in range(10):
    if(i != A+B):
        print(i)
        break