import sys


N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

ans=0
A.sort()
for i in range(N):
    x=A[i]
    y=B.pop(B.index(max(B))) #정렬한 A에 대해 가장 큰 값과 작은 값을 차례로 곱함
    ans+=x*y

print(ans)