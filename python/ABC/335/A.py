def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

s = SI()

a, b = s[:len(s)-4], int(s[len(s)-4:])+1
ans = a+str(b)

print(ans)
