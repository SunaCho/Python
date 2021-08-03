# 1167 트리의 지름에서 간선에 가중치가 추가됨.

import sys
import collections

n=int(sys.stdin.readline())
adj={i:[] for i in range(n+1)}
for i in range(n-1):
    a,b,weight=map(int,sys.stdin.readline().split())
    adj[a].append((b,weight))
    adj[b].append((a,weight))


def bfs(num):
    q=collections.deque()
    q.append((num,0))
    visited=[False]*n
    visited[num-1]=True
    result=[0,0]
    while q:
        now, now_distance=q.popleft()
        for i in adj[now]:
            if visited[i[0]-1]==False:
                visited[i[0]-1]=True
                q.append((i[0],i[1]+now_distance))

                if result[1]<now_distance+i[1]:
                    result[0]=i[0]
                    result[1]=now_distance+i[1]
    return result


a=bfs(1)
b=bfs(a[0])
print(b[1])