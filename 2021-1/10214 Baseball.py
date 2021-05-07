T=int(input())

for _ in range(T): 
    ax,bx=0,0
    for i in range(9):
        a,b=map(int,input().split())
        if a>b:
            ax+=1
        elif a<b:
            bx+=1
    if ax>bx:
        print("Yonsei")
    elif ax<bx:
        print("Korea")
    else:
        print("Draw")