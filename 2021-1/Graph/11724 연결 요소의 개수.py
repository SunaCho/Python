import sys
sys.setrecursionlimit(10**6)
#DFS의 재귀깊이 한계로 인해 Python이 정한 깊이(1000)를 변경해야 함!

N,M=map(int,sys.stdin.readline().split())
graph=[[0]*(N+1) for _ in range(N+1)]
visit_list=[0]*(N+1)
count=0

for _ in range(M):
    from_M, to_N=map(int,sys.stdin.readline().split())
    graph[from_M][to_N]=graph[to_N][from_M]=1

def dfs(start_node):
    visit_list[start_node]=1
    for i in range(1,N+1):
        if visit_list[i]==0 and graph[start_node][i]==1:
            dfs(i)

for i in range(1,N+1):
    if visit_list[i]==0:
        dfs(i)
        count+=1

print(count)