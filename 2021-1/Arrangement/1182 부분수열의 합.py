from itertools import combinations
import sys

N,S=map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().split()))
cnt=0
for i in range(1,N+1):
    all=combinations(lst,i)
    for j in all:
        if sum(j)==S:
            cnt+=1

print(cnt)