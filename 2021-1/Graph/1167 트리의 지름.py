import sys
import collections

def bfs(num):
    distance,node=0,0
    q=collections.deque()
    q.append((num,0))
    visited[num]=True 
    while q:
        now, now_distance=q.popleft()
        for i in adj[now]:
            if visited[i[0]]==False:
                visited[i[0]]=True
                q.append((i[0],i[1]+now_distance))

                if now_distance+i[1]>distance: # 거리 최댓값 확인
                    distance=now_distance+i[1]
                    node=i[0]
    return distance,node

def init():
    for i in range(V):
        visited[i]=False
    
V=int(sys.stdin.readline())

adj=[[] for _ in range(V)]
for i in range(V):
    temp=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(temp)-1,2):
        adj[temp[0]-1].append((temp[j]-1,temp[j+1]))

visited=[False]*V #방문 노드 체크
a,b=bfs(0)
init()
print(bfs(b)[0])