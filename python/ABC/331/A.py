def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

M, D = ILI()
y,m,d = ILI()

if(m<M and d<D): print(f'{y} {m} {d+1}')#' '.join([str(y),str(m),d+1]))
elif(m==M and d==D): print(f'{y+1} {1} {1}') #print(' '.join([y+1, 1, 1]))
elif(m==M and d<D): print(f'{y} {m} {d+1}')#print(' '.join([y, M, d+1]))
elif(m<M and d==D): print(f'{y} {m+1} {1}')#print(' '.join([y, M+1, 1]))
