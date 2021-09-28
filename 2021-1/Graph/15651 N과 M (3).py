N,M=list(map(int,input().split()))
lst=[]
 
def dfs():
    if len(lst)==M:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(1,N+1):
        # if i not in lst 를 빼 줌 (중복도 가능)
        lst.append(i)
        dfs()
        lst.pop()
dfs()