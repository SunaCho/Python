import sys


N=int(sys.stdin.readline())
dp=[0]*(N+1)
T=[]
P=[]

for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    T.append(a)
    P.append(b)

K=0
for i in range(N):
    K=max(K,dp[i])
    if T[i]+i>N:
        continue
    dp[i+T[i]]=max(K+P[i],dp[i+T[i]])

print(max(dp))