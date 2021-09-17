import sys

N=int(sys.stdin.readline())
R,G,B=0,1,2 
temp=[]

for _ in range(N):
    lst=[int(i) for i in sys.stdin.readline().split()]
    temp.append(lst)


dp=[[0]*3 for _ in range(N)]
dp[0][R]=temp[0][R]
dp[0][G]=temp[0][G]
dp[0][B]=temp[0][B]

for i in range(1,N):
    dp[i][R]=min(dp[i-1][G], dp[i-1][B])+temp[i][R]
    dp[i][G]=min(dp[i-1][R], dp[i-1][B])+temp[i][G]
    dp[i][B]=min(dp[i-1][G], dp[i-1][R])+temp[i][B]

print(min(dp[N-1]))