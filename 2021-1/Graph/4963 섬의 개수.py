#2667은 상하좌우였다면 이 문제는 대각선도 고려해야 함. dx와 dy 리스트 내 조합 변경!

import sys
sys.setrecursionlimit(10**6)


while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break

    ans=[]
    lands=[]
    visited=[[0 for _ in range(w)] for _ in range(h)]
    cnt=0

    for i in range(h):
        raw=[int(x) for x in sys.stdin.readline().split()]
        for j in range(w):
            if raw[j]==1:
                lands.append([i,j])
        ans.append(raw)

    
    def dfs(y,x):
        dx=[-1,1,0,0,-1,-1,1,1]
        dy=[0,0,-1,1,-1,1,-1,1]

        visited[y][x]=1
        for i in range(8): #8방향 탐색을 위함
            nowx, nowy=x+dx[i], y+dy[i]
            if nowx<0 or nowy<0 or nowx>=w or nowy>=h:
                continue
            if ans[nowy][nowx]==1 and visited[nowy][nowx]==0:
                dfs(nowy,nowx)

    for land in lands:
        if visited[land[0]][land[1]]==0:
            dfs(land[0],land[1])
            cnt+=1

    print(cnt)