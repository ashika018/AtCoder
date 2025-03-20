def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, M = ILI()
schedule = input().split('0')

ans = 0
for part_sche in schedule:
    part_sche = list(part_sche)
    logo_shirt = 0
    non_logo_shirt = M
    for i in part_sche:
        if(i=='2'):
            logo_shirt += 1
        else:
            non_logo_shirt -= 1
            if(non_logo_shirt<0):
                logo_shirt += 1
    ans = max(ans, logo_shirt)
print(ans)