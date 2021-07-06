import sys
from collections import deque
input=lambda: sys.stdin.readline().strip()

N=int(input())
Deque=deque()

for i in range(N):
    a,*b=input().split()

    if a=='push_front':
        Deque.appendleft(int(b[0]))

    elif a=='push_back':
        Deque.append(int(b[0]))

    elif a=='pop_front':
        if Deque:
            print(Deque.popleft())
        else:
            print("-1")

    elif a=='pop_back':
        if Deque:
            print(Deque.pop())
        else:
            print("-1")

    elif a=='size':
        print(len(Deque))

    elif a=="empty":
        if len(Deque)==0:
            print(1)
        else:
            print(0)

    elif a=='front':
        if Deque:
            print(Deque[0])
        else:
            print("-1")

    elif a=='back':
        if Deque:
            print(Deque[-1])
        else:
            print("-1")
