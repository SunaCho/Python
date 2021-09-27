#이 시리즈를 너무 오랜만에 풀어서 예전 코드+블로그 참고했다.
#BFS

import sys
from collections import deque

def bfs(start_node):
    quene=deque()
    visit_list=[0 for _ in range(n+1)]
    quene.append(start_node)
    visit_list[start_node]=1

    while quene:
        x=quene.popleft()
        for i in tree[x]:
            if visit_list[i]==0:
                visit_list[i]=1
                res[i]=res[x]+1
                quene.append(i)

n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
tree=[[] for _ in range(n+1)]
res=[0 for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

bfs(a)

if res[b]!=0:
    print(res[b])
else:
    print("-1")