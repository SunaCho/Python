import sys

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
lst.sort()

res=0

for i in range(1,N):
    lst[i]+=lst[i-1]

print(sum(lst))