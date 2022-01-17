from collections import deque
import sys

N,M=map(int,sys.stdin.readline().split())
index=list(map(int,sys.stdin.readline().split()))
cnt=0
quene=deque([i for i in range(1,N+1)])

for i in index:
    while 1:
        if quene[0]==i:
            quene.popleft()
            break
        else:
            if quene.index(i)<=len(quene)//2:
                quene.rotate(-1)
            else:
                quene.rotate(1)
            cnt+=1

print(cnt)