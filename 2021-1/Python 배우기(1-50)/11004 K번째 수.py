import sys
N,K=map(int,sys.stdin.readline().split())
lst=map(int,sys.stdin.readline().split())
lst=sorted(lst)
print(lst[K-1])
