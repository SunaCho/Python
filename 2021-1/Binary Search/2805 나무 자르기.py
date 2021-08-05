# 이전 문제랑 비슷하게 풀었는데 시간 초과가 뜬다. 일단 pypy3으로 제출했다.

import sys

N,M=map(int,sys.stdin.readline().split())
woods=list(map(int,sys.stdin.readline().split()))

left=0
right=max(woods)
res=[]

while right>=left:
    c=0
    middle=(left+right)//2
    for i in woods:
        if i>middle:
            c+=i-middle
    
    if c==M:
        res.append(middle)
        break
    elif c>M:
        res.append(middle)
        left=middle+1
    else:
        right=middle-1

print(max(res))