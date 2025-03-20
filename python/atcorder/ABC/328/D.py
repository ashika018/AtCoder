"""
S = input()
ans = ''
index = 0

def DFS(S, i, j):
    if(S[i-2:i]=='AB' and S[j]=='C'): DFS(S,i-2,j+1)
    elif(S[i-1]=='A' and S[j:j+2]=='BC'): DFS(S,i-1,j+2)
    else: return [i,j]

while True:
    i = S.find('ABC')
    if(i==-1): break
    elif(len(S)==3): S = ''
    else:
        j=i+3
        l = DFS(S,i,j)
        ans+=S[:l[0]]
        S = S[l[1]:]

ans+=S
print(ans)

"""

# データ構造としてStack(First in last out)を使うとO(n)で答えを求められる
# 1文字目からstackに入れていき、'ABC'ができたところで、'ABC'をpopする。
# これを最後の文字まで続ける

S = input()
stack = []
for s in list(S):
    stack.append(s)
    if(len(stack)>=3):
        if(stack[-3]+stack[-2]+stack[-1]=='ABC'):
            for _ in range(3): __ = stack.pop()

ans = ''.join(stack)
print(ans)