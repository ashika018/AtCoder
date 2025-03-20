N, X = list(map(int, input().split(' ')))
A_l = list(map(int, input().split(' ')))

def f():
    for i in range(0, 101):
        l = A_l.copy()
        l.append(i)
        l.sort()
        total = sum(l[1:len(l)-1])
        if(total>=X):
            return i
    return -1

print(f())