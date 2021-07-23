import sys
sys.setrecursionlimit(10**6)

def dfs(start,tree,parent):
    for i in tree[start]:
        if parent[i]==0:
            parent[i]=start
            dfs(i,tree,parent)

N=int(sys.stdin.readline())
tree=[[] for _ in range(N+1)]
parent=[0 for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1,tree,parent)

for i in range(2,N+1):
    print(parent[i])