import sys

N,K=map(int,sys.stdin.readline().split())
lst=[]
dp=[10001]*(K+1)
dp[0]=0

for i in range(N):
    lst.append(int(input()))

for i in range(N):
    for j in range(lst[i],K+1):
        if j-i>=0:
            dp[j]=min(dp[j-lst[i]]+1,dp[j])
if dp[-1]!=10001:
    print(dp[-1])
else:
    print('-1')