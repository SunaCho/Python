import sys

def dfs(x,y,cnt):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    array[x][y]=0
    for i in range(4): #4방향 탐색을 위함
        nowx, nowy=x+dx[i], y+dy[i]
        if nowx<0 or nowy<0 or nowx>=N or nowy>=N or not array[nowx][nowy]:
            continue
        cnt=dfs(nowx,nowy,cnt+1)
    return cnt

N=int(sys.stdin.readline())
array=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]

cnt=0
ans=[]

for i in range(N):
    for j in range(N):
        if array[i][j]==1:
            ans.append(dfs(i,j,1))
print(len(ans))
for i in sorted(ans):
    print(i)