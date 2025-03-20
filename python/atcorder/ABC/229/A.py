
n = 2  # nは入力回数
str_list = [input() for _ in range(n)]
if((str_list[0]=="#." and str_list[1] ==".#") or (str_list[0]==".#" and str_list[1] =="#.")): print("No")
else: print("Yes")
