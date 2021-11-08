'''
R reverse
D delete the first key
'''

import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    p=sys.stdin.readline()
    n=int(sys.stdin.readline())
    lst=sys.stdin.readline()[1:-2].split(",")

    if lst[0]!='':
        lst=deque(lst)
    else:
        lst=deque()

    dir=True
    error=False

    for i in p:
        if i=="R":
            if dir==True:
                dir=False
            elif dir==False:
                dir=True
        elif i=="D":
            if len(lst)==0:
                print("error")
                error=True
                break
            if dir==True:
                lst.popleft()
            elif dir==False:
                lst.pop()

    if dir==False:
        lst.reverse()
    
    if error==False:
        print("[",end="")
        for i in range(len(lst)):
            print(lst[i], end="")
            if i!=len(lst)-1:
                print(",",end="")
        print("]")
    
    error=False
