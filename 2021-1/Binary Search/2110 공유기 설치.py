import sys

N,C=map(int,sys.stdin.readline().split())
lst=[int(sys.stdin.readline()) for i in range(N)]
lst.sort()

right=lst[-1]-lst[0]
left=1
ans=0

while right>=left:
    mid=(right+left)//2
    cnt=1
    c=lst[0]
    for i in range(1,N):
        if lst[i]>=c+mid:
            cnt+=1
            c=lst[i]

    if cnt<C:
        right=mid-1
    else:
        left=mid+1
        ans=mid

print(ans)