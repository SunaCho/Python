#이건 그래프랑 DP가 합쳐진 문제인 듯

import sys

def dfs(x,y):
    if x==N-1 and y==N-1:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0
        x1,y1=x+lst[x][y],y
        x2,y2=x,y+lst[x][y]
        if 0<=x1<N and 0<=y1<N:
            dp[x][y]+=dfs(x1,y1)
        if 0<=x2<N and 0<=y2<N:
            dp[x][y]+=dfs(x2,y2)
    return dp[x][y]

N=int(sys.stdin.readline())
lst=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
dp=[[-1]*N for i in range(N)]

print(dfs(0,0))