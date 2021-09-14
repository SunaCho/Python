#C 구현이 익숙하지 않아서 풀어도 코드로 옮기지 못한다. 이번 주까지만 파이썬을 잡고 있어야겠다

import sys
T=int(sys.stdin.readline())

for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    dist=y-x
    cnt=1
    while True:
        if cnt**2<=dist<(cnt+1)**2:
            break
        cnt+=1
    if cnt**2==dist:
        print((2*cnt)-1)
    elif cnt**2<dist<=cnt**2+cnt:
        print(2*cnt)
    else:
        print((2*cnt)+1)