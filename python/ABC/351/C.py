def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

N = II()
A_l = ILI()

ball_l = []
for n in range(N):
    ball_l.append(A_l[n])
    while True:
        if(len(ball_l)<=1):
            break
        ball1, ball2 = ball_l.pop(), ball_l.pop()
        if(ball1!=ball2):
            ball_l.append(ball2)
            ball_l.append(ball1)
            break
        else:
            ball_l.append(ball1+1)

print(len(ball_l))