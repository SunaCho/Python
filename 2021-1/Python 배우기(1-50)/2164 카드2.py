import sys
from collections import deque

N=int(sys.stdin.readline())
quene=deque([i for i in range(1,N+1)])

while(len(quene)>1):
    quene.popleft()
    temp=quene.popleft()
    quene.append(temp)

print(quene[0])