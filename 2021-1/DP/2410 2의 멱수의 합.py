import sys

N=int(sys.stdin.readline())
lst=[2**x for x in range(21)]
dp=[0]*(N+1)
dp[0]=1
for num in lst:
    if num<=N:
        for j in range(num,N+1):
            dp[j]+=dp[j-num]

print(dp[-1]%1000000000)