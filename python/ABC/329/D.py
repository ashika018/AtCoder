def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N, M = ILI()
A_l = ILI()

d = dict((i, 0) for i in range(1, N+1))
vote_n = 0
winners = float('inf')

for vote_to in A_l:
    d[vote_to] += 1
    if((vote_n==d[vote_to] and vote_to<winners) or (vote_n<d[vote_to])):
        vote_n = d[vote_to]
        winners = vote_to
    print(winners)
