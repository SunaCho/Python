import sys

N=int(input())
def cnt(N):
    cnt=0
    while N!=0:
        N//=5
        cnt+=N
    return cnt

print(cnt(N))