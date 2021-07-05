import sys
from collections import deque

Deque=deque()
N=int(input())

for i in range(N):
    cmd=list(map(str,sys.stdin.readline().split()))

    if cmd[0]=='push_front':
        Deque.appendleft(int(cmd[1]))

    elif cmd[0]=='push_back':
        Deque.append(int(cmd[1]))

    elif cmd[0]=='pop_front':
        if Deque:
            print(Deque.popleft(0))
        else:
            print("-1")

    elif cmd[0]=='pop_back':
        if Deque:
            print(Deque.pop(0))
        else:
            print("-1")

    elif cmd[0]=='size':
        print(len(Deque))

    elif cmd[0]=="empty":
        if len(Deque)==0:
            print(1)
        else:
            print(0)

    elif cmd[0]=='front':
        if Deque:
            print(Deque[0])
        else:
            print("-1")

    elif cmd[0]=='back':
        if Deque:
            print(Deque[-1])
        else:
            print("-1")