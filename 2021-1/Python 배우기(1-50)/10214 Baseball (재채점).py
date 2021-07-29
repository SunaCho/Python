# 재채점하면서 오답 처리됐다. 이걸 왜 틀렸지......

import sys

T=int(sys.stdin.readline())

for _ in range(T): 
    ax,bx=0,0
    for i in range(9):
        a,b=map(int,sys.stdin.readline().split())
        ax+=a
        bx+=b
    if ax>bx:
        print("Yonsei")
    elif ax<bx:
        print("Korea")
    elif ax==bx:
        print("Draw")