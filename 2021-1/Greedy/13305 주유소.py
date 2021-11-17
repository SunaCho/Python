import sys

N=int(sys.stdin.readline())
road=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))

cnt=0
M=cost[0]

for i in range(N-1):
    if cost[i]<M:
        M=cost[i]
    cnt+=M*road[i]

print(cnt)