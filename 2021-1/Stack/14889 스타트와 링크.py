from itertools import combinations
import sys

N=int(sys.stdin.readline())
lst=[]

for i in range(N):
    S=list(map(int,sys.stdin.readline().split()))
    lst.append(S)

num=[i for i in range(N)]
res=sys.maxsize

for i in combinations(num,N//2):
    start=set(i)
    link=set(num)-start
    start=list(start)
    link=list(link)

    score=0
    
    for i in range(1,N//2):
        for j in range(i):
            score+=lst[start[i]][start[j]] + lst[start[j]][start[i]]
            score-= lst[link[i]][link[j]] + lst[link[j]][link[i]]
    res=min(abs(score),res)

print(res)