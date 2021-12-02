import sys

N,M=map(int,sys.stdin.readline().split())
lst=[int(sys.stdin.readline()) for _ in range(N)]

left=min(lst)
ans=right=max(lst)*M

while left<=right:
    tot=0
    mid=(left+right)//2
    for i in range(N):
        tot+=mid//lst[i]
    if tot>=M:
        right=mid-1
        ans=min(ans,mid)
    else:
        left=mid+1

print(ans)