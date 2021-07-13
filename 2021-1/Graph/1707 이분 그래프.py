#이분 그래프란 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프이다.
#https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html 공부함

import sys
sys.setrecursionlimit(10**6)

def bfs(start_node):
    quene=[start_node]
    visit_list[start_node]=1

    while quene:
        V=quene.pop(0)
        for i in connect[V]: #정점의 색 구분
            if visit_list[i]==-1:
                if visit_list[V]==1:
                    visit_list[i]=2
                elif visit_list[V]==2:
                    visit_list[i]=1
                quene.append(i)
            elif visit_list[i]==visit_list[V]:
                return 0
    return 1

K=int(sys.stdin.readline())
for _ in range(K):
    V,E=map(int,sys.stdin.readline().split())
    connect=[set() for _ in range(V+1)]
    for _ in range(E):
        from_M, to_N=map(int,sys.stdin.readline().split())
        connect[from_M].add(to_N)
        connect[to_N].add(from_M)

    visit_list=[-1]*(V+1)
    flag=True
    for i in range(1,V+1):
        if visit_list[i]==-1:
            temp=bfs(i)
            if not temp:
                flag=False
                break

    if flag:
        print("YES")
    else:
        print("NO")