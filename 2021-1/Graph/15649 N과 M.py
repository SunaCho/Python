import sys

N,M=list(map(int,sys.stdin.readline().split()))
lst=[]

def dfs():
    if len(lst)==M:
        print(' '.join(map(str,lst)))
        return
    for i in range(1,N+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

dfs()