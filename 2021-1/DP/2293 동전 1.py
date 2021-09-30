import sys

N,K=map(int,sys.stdin.readline().split())
lst=[]
dp=[0]*(K+1)
dp[0]=1

for i in range(N):
    lst.append(int(input()))
for i in lst:
    for j in range(1,K+1):
        if j-i>=0:
            dp[j]+=dp[j-i]

print(dp[K])