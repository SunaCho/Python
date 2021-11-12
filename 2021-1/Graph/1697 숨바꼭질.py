import sys
from collections import deque

def bfs(): 
    lst=deque()
    lst.append(N)
    while lst:
        num=lst.popleft()
        if num==K:
            print(time[num])
            return
        for i in (num-1, num+1, num*2):
            if 0<=i<100001 and not time[i]:
                time[i]=time[num]+1
                lst.append(i)

time=[0]*100001
N,K=map(int,sys.stdin.readline().split())
bfs()