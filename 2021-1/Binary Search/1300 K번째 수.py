N=int(input())
k=int(input())
start, end=1, k

while start<=end:
    middle=(start+end)//2
    s=0
    for i in range(1,N+1):
        s+=min(middle//i, N)
    if s>=k:
        ans=middle
        end=middle-1
    else:
        start=middle+1

print(ans)