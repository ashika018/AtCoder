N = int(input())

flag_2, flag_3 = 0, 0
while True:
    if(N%3==0): N/=3
    else: flag_3 = 1
    if(N%2==0): N/=2
    else:flag_2 = 1
    if(flag_2==1 and flag_3==1): break

if(N==1): print('Yes')
else: print('No')