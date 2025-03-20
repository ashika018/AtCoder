N = int(input())
str_list = [input() for _ in range(N)]
dict = {}

for i in str_list:
    if(i in dict): dict[i] += 1
    else: dict[i] = 1

#print(dict)
print(max(dict, key=dict.get))

