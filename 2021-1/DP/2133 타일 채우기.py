num=int(input())
dp=[0]*(num+1)
dp[0]=0
if num>=2:
    dp[2]=3

if num>=4:
    for i in range(4,num+1,2):
        dp[i]=dp[i-2]*dp[2]
        for j in range(4,i,2):
            dp[i]+=2*dp[i-j]
        dp[i]+=2

print(dp[num])