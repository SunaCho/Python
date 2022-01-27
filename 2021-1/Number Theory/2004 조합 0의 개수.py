import sys

N,M=map(int,sys.stdin.readline().split())

def cnt(N,K):
    count=0
    while N:
        N//=K
        count+=N
    return count

five=cnt(N,5)-cnt(M,5)-cnt(N-M,5)
two=cnt(N,2)-cnt(M,2)-cnt(N-M,2)

ans=min(five,two)
print(ans)