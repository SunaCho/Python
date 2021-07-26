# 재채점하면서 오답 처리되어서 다시 풀었다.

import sys

T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    dp=[[0]*n for i in range(2)]
    a=[list(map(int,sys.stdin.readline().split())) for i in range(2)]

    dp[0][0]=a[0][0]
    dp[1][0]=a[1][0]

    for i in range(1,n):
        dp[0][i]=max(dp[1][i-1]+a[0][i],dp[0][i-1])
        dp[1][i]=max(dp[0][i-1]+a[1][i],dp[1][i-1])
    print(max(dp[0][-1],dp[1][-1]))