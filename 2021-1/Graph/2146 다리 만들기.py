# 마지막에 접근 방법을 몰라서 헤메다가 결국 솔루션 보고 전부 새로 보완했다.
# BFS를 사용하고 4방향 탐색으로 0과 1이 접하는 부분 확인하는 것까지는 구현했는데, 거리 값의 경우의 수를 처리하는 법을 몰랐다.


import sys
from collections import deque

def numbering(y,x,number):
    global board
    q=deque()
    q.append((y,x))
    board[y][x]=number

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        cy,cx=q.popleft()

        for i in range(4):
            nowx, nowy=cx+dx[i], cy+dy[i]
            if 0<=nowy<N and 0<=nowx<N and board[nowy][nowx]==1:
                board[nowy][nowx]=number
                q.append((nowy,nowx))

def bfs(y,x,number):
    global visited
    q=deque()
    visited[y][x]=True
    q.append((y,x))

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        cy,cx=q.popleft()

        for i in range(4):
            nowx, nowy=cx+dx[i], cy+dy[i]
            if 0<=nowy<N and 0<=nowx<N:
                if board[nowy][nowx]==number and visited[nowy][nowx]==False:
                    q.append((nowy,nowx))
                    visited[nowy][nowx]=True
                elif board[nowy][nowx]==0 and visited[nowy][nowx]==False:
                    visited[nowy][nowx]=True
                    find_bridge(nowy,nowx,number)

def find_bridge(y,x,number):
    global answer
    q=deque()
    q.append((y,x))
    lst=[[0 for _ in range(N)] for _ in range(N)]
    lst[y][x]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        cy,cx=q.popleft()

        if board[cy][cx]!=0 and board[cy][cx]!=number:
            answer=min(answer, lst[cy][cx]-1)
            return
        for i in range(4):
            nowx, nowy=cx+dx[i], cy+dy[i]
            if 0<=nowy<N and 0<=nowx<N and lst[nowy][nowx]==0 and board[nowy][nowx]!=number:
                lst[nowy][nowx]=lst[cy][cx]+1
                q.append((nowy,nowx))

N=int(sys.stdin.readline())
board=[list(map(int,input().split())) for _ in range(N)]

number=2
for y in range(N):
    for x in range(N):
        if board[y][x]==1:
            numbering(y,x,number)
            number+=1

answer=10000 # 100*100 맵에서 다리를 잇는 경우의 수가 소량이라서 BFS 돌려도 된다.
visited=[[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x]==False and board[y][x]>0:
            bfs(y,x,board[y][x])


print(answer)