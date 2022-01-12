import sys

N,M=map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().split()))
res=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if lst[i]+lst[j]+lst[k]>M:
                continue
            else:
                res=max(res,lst[i]+lst[j]+lst[k])

print(res)