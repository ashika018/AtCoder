def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()

while True:
    i_100, i_10, i_1 = list(str(N))
    if(int(i_100)*int(i_10)==int(i_1)):
        print(N)
        break
    N+=1