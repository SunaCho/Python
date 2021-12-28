import sys

N,M=map(int,sys.stdin.readline().split())
lst=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=lst[i-1][j-1]+max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])

print(dp[-1][-1])
