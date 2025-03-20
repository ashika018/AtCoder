# 動的計画法：bit DP

N = int(input())
people_in_charge = input()

d = {'J':2,'O':1,'I':0}

dp = [[0]*(2**3) for _ in range(N)]
for participants_set in range(2**3):
    # PIC: person in charge → 担当者のこと
    PIC_day1 = d[people_in_charge[0]]
    does_PIC_come = (participants_set>>PIC_day1 & 1 == 1)
    # 最初はJ君が鍵を持っているので
    does_J_come = (participants_set>>d['J'] & 1 == 1)
    if(does_PIC_come and does_J_come): dp[0][participants_set] = 1

for i in range(1, N):
    for participants_set in range(2**3):
        PIC_dayi = d[people_in_charge[i]]
        does_PIC_come = (participants_set>>PIC_dayi & 1 == 1)
        if(not does_PIC_come):
            dp[i][participants_set] = 0
        else:
            # 昨日と今日で参加者にダブりがあるマスを全て足し合わせる
            # 判別はbitの論理積をとって、bin(0)=000にならなければOK
            dp[i][participants_set] = sum([dp[i-1][p] for p in range(2**3) if p&participants_set != 0])

ans = sum(dp[N-1])%10007
print(ans)


