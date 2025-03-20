K = int(input())
str = bin(K)[2:]

while str[0] == '0':
    str = str[1:]
ans = ""
for i in list(str):
    if(i == '1'): ans = ans+'2'
    else: ans = ans+'0'
print(int(ans))