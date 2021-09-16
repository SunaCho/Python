import sys

T=int(sys.stdin.readline())

for i in range(T):
    N,M=map(int,sys.stdin.readline().split())
    imp=list(map(int,sys.stdin.readline().split()))
    lst=[0]*N
    lst[M]=1
    cnt=0

    while True:
        if imp[0]==max(imp):
            cnt+=1
            if lst[0]==1:
                print(cnt)
                break
            else:
                del imp[0]
                del lst[0]
        else:
            imp.append(imp[0])
            del imp[0]
            lst.append(lst[0])
            del lst[0]