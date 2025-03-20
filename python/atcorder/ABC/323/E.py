def SI():
    return input()
def II():
    return int(input())
def ILI():
    return list(map(int, input().split(' ')))
def SLI():
    return input().split(' ')

# 時刻tに曲が切り替わる確率を動的計画法で求める
# dp[t]：時刻tに曲が切り替わる確率
# dp[t] = (dp[t-T1]+dp[t-T2]+...+dp[t-Tn])/n

N, X = ILI()
music_times = ILI()
MOD = 998244353

# dp tableの生成
dp = [0 for _ in range(X+1)]
dp[0] = 1

# 逆元の扱い
# ax+by=gcd(a,b)の解(x,y)とgcd(a,b)を求める関数
def ex_euclid(a, b):
    if(b==0):
        return(1, 0, a)
    else:
        x_, y_, gcd = ex_euclid(b, a%b)
        return(y_, x_-(a//b)*y_, gcd)
N_inverse, _, _ = ex_euclid(N, MOD)
N_inverse %= MOD

for i in range(X):
    for t in music_times:
        if(i+t>=len(dp)):
            continue
        dp[i+t] += dp[i]*N_inverse
        dp[i+t] %= MOD

# 求めたい確率は(dp[X]+dp[X-1]+..+dp[X-T1+1])/N
T1 = music_times[0]
ans = 0
for i in range(T1):
    if(X-i<0): break
    ans += dp[X-i]*N_inverse
    ans %= MOD

print(ans)
