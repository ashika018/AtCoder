
N, Q = map(int, input().split())
tall = list(map(int, input().split()))
tall.sort()
l_t = len(tall)
x_list = [int(input()) for _ in range(Q)]

def b_search(max, min, f):
    if(f<=tall[0]): return l_t
    if(tall[l_t-1]<f): return 0
    m = (max+min)//2
    if(tall[m]<f and f<=tall[m+1]): return l_t-(m+1)
    elif(tall[m]<f): return b_search(max, m, f)
    else: return b_search(m, min, f)

for i in x_list: print(b_search(l_t-1, 0, i))
