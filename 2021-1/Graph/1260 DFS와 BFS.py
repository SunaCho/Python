import sys

N,M,V=map(int,sys.stdin.readline().split())
graph=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    from_M, to_N=map(int,sys.stdin.readline().split())
    graph[from_M][to_N]=graph[to_N][from_M]=1

visit_list=[0]*(N+1)

def bfs(start_node):
    quene=[start_node]
    visit_list[start_node]=1
    while quene:
        start_node=quene.pop(0)
        print(start_node,end=' ')
        for i in range(1,N+1):
            if visit_list[i]==0 and graph[start_node][i]==1:
                quene.append(i)
                visit_list[i]=1

def dfs(start_node):
    visit_list[start_node]=1
    print(start_node,end=' ')
    for i in range(1,N+1):
        if visit_list[i]==0 and graph[start_node][i]==1:
            dfs(i)

dfs(V)
visit_list=[0]*(N+1)
print()
bfs(V)