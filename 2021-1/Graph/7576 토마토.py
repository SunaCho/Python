#4방향 탐색(대각선에 영향 주지 않음), 전체 토마토가 익으면(0이 없으면) 횟수 출력

import sys
from collections import deque

def bfs():
    while quene:
        x,y=quene.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]  
        for i in range(4): #4방향 탐색을 위함
            nowx, nowy=x+dx[i], y+dy[i]
            if 0<=nowx<n and 0<=nowy<m and graph[nowx][nowy]==0:
                quene.append([nowx,nowy])
                graph[nowx][nowy]=graph[x][y]+1

m,n=map(int,sys.stdin.readline().split())

graph=[]
quene=deque([])
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j]==1:
            quene.append([i,j])

bfs()
cnt=0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    cnt=max(cnt,max(i))

print(cnt-1)