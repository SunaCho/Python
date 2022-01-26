import sys
from collections import Counter

T=int(sys.stdin.readline())

for i in range(T):
    N=int(sys.stdin.readline())
    lst=[]

    for j in range(N):
        x,y=sys.stdin.readline().split()
        lst.append(y)

    lst_Counter=Counter(lst)
    cnt=1

    for key in lst_Counter:
        cnt*=lst_Counter[key]+1
    
    print(cnt-1)