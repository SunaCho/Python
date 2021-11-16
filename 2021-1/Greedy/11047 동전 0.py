import sys

N,K=map(int,sys.stdin.readline().split())
lst=[]
cnt=0

for i in range(N):
    lst.append(int(input()))

for i in range(N-1, -1, -1):
    if K==0:
        break
    if lst[i]>K:
        continue
    cnt+=K//lst[i]
    K%=lst[i]

print(cnt)