num=int(input())

dp=[0]*101

dp[0]=0
for i in range(1,4):
    dp[i]=1
for i in range(4,6):
    dp[i]=2

for _ in range(num):
    N=int(input())
    if N>=6:
        for i in range(6,N+1):
            dp[i]=dp[i-5]+dp[i-1]
        print(dp[N])
        
    else:
        print(dp[N])