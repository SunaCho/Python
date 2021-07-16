#dfs로 탐색하다 다시 초기치가 발견되면 Break

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n=int(input())
    lst=[0]+list(map(int,sys.stdin.readline().split()))
    visit_lst=[0]*(n+1)
    team=0

    for i in range(1,n+1):
        if visit_lst[i]:
            continue
        temp=i
        loop=[i]
        visit_lst[i]=1
        while True:
            tmp=lst[temp]
            if visit_lst[tmp]:
                break
            temp=tmp
            loop.append(temp)
            visit_lst[temp]=1
        
        if loop and tmp in loop:
            team+=len(loop[loop.index(tmp):])
    print(n-team)