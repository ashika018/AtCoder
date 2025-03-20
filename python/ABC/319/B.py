N = int(input())

string = ''
for i in range(0, N+1):
    for j in range(1, 10):
        if((N%j == 0) and (i%(N/j)==0)):
            string += str(j) 
            break
        if(j == 9): string += '-'

print(string)

