#상하좌우 탐색, 대각선은 고려하지 않음
#요새 그래프 문제가 잘 풀려서 좋다! 유형을 풀어 보니까 이런 간단한 문제는 쉽게 풀어서 기분이 좋다.

import sys
N,M=map(int,sys.stdin.readline().split())

board=[]

for _ in range(N):
    board.append(list(sys.stdin.readline()))

board[0][0]=1
quene=[[0,0]]

def bfs():
    while quene:
        x,y=quene[0][0],quene[0][1]
        del quene[0]

        dx=[-1,1,0,0]
        dy=[0,0,-1,1]  
        for i in range(4): #4방향 탐색을 위함
            nowx, nowy=x+dx[i], y+dy[i]
            if 0<=nowx<N and 0<=nowy<M:
                if board[nowx][nowy]=='1':
                    quene.append([nowx,nowy])
                    board[nowx][nowy]=board[x][y]+1

bfs()
print(board[N-1][M-1])