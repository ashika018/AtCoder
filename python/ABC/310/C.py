N = int(input())
str_l = [input() for _ in range(N)]

for i in range(len(str_l)):
    string = str_l[i]
    r_string = "".join(list(reversed(string)))
    n_l = sorted([string, r_string])
    new_string = "".join(n_l)
    str_l[i] = new_string

print(len(set(str_l)))