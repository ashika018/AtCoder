s = list(input())
t = list(input())

alp = list("abcdefghijklmnopqrstuvxwyz") #アルファベットは26種類
ans = 0





for i in range(len(alp)):
    s_test = s
    def s_change(x):
        if(ord(x)+i>122): return chr(ord(x)+i-122+96)
        else: return chr(ord(x) + i)
    if(list(map(s_change, s_test))==t): ans += 1

if(ans>0): print("Yes")
else: print("No")
