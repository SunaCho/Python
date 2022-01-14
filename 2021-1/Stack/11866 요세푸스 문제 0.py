from collections import deque
import sys

quene=deque()
lst=[]

N,K=map(int,sys.stdin.readline().split())
for i in range(1,N+1):
    quene.append(i)
    
while quene:
    for i in range(K-1):
        quene.append(quene.popleft())
    lst.append(quene.popleft())
    
print("<",end='')
for i in range(len(lst)-1):
    print("%d, "%lst[i],end='')
print(lst[-1],end='')
print(">")
