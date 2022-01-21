import sys

T=int(sys.stdin.readline())

def res(N):
    tmp=1
    for i in range(N):
        tmp*=(i+1)
    return tmp

for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    print(res(M)//(res(N)*res(M-N)))