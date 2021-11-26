import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

if N>=2:
    dp=[1]*(N+1)
    dp[2]=2
    for i in range(3,N+1):
        dp[i]=dp[i-1]+dp[i-2] #피보나치
    start=1
    ans=1
    for _ in range(M):
        vip=int(sys.stdin.readline())
        ans*=dp[vip-start]
        start=vip+1
    print(ans*dp[N-start+1])

else:
    for _ in range(M):
        vip=int(sys.stdin.readline())
    print(1)