N = int(input())

d = {}

for _ in range(N):
    size, num = list(map(int, input().split(' ')))
    if(size not in d.keys()): d[size] = num
    else: d[size] += num

d = dict(sorted(d.items()))
flag = dict([(k, 1) for k in d.keys()])

ans = 0

for size in d.keys():
    # print(flag)
    if(flag[size]):
        while True:
            flag[int(size)] = 0
            num = d[int(size)]
            ans += num % 2

            num = num // 2
            size = size * 2

            if(size not in d.keys()):
                check = 0
                while True:
                    if(num==0): 
                        check = 1
                        break
                    ans += num % 2
                    num = num // 2
                    size = size * 2
                    if(size in d.keys()):
                        d[size] += num
                        check = 0
                        break
                if(check): break
            else:
                d[int(size)] += num

print(ans)
