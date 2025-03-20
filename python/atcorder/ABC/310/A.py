input_l = input().split(" ")
N, P, Q = int(input_l[0]), int(input_l[1]) , int(input_l[2])
D_l = [int(i) for i in input().split(" ")]

if(min(D_l)+Q <= P): print(min(D_l)+Q)
else: print(P)
