def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 12:36

X, Y = ILI()
if(-2<=X-Y<=3):
    print('Yes')
else:
    print('No')

