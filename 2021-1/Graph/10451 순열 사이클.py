import sys
sys.setrecursionlimit(10**6)

def dfs(to_N,from_N):
    global cycle
    next=graph[to_N]
    if visit_list[next]:
        if next==from_N:
            cycle+=1
            return
    else:
        visit_list[next]=1
        dfs(next,from_N)


T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    graph=[0]+list(map(int,sys.stdin.readline().split()))
    cycle=0
    visit_list=[0]*(N+1)
    for i in range(1,N+1):
        if visit_list[i]:
            continue
        visit_list[i]=1
        dfs(i,i)
    print(cycle)