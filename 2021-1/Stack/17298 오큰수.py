import sys

stack=[]
stack.append(0)

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
ans=[-1]*N

for i in range(1,N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()]=A[i]
    stack.append(i)

print(*ans)