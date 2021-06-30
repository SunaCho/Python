import sys
from collections import Counter

N=int(input())
lst=[]
for i in range(N):
    lst.append(int(input()))

lst.sort()
lst_new=Counter(lst)
max=0
for i in lst:
    if lst_new[i]>max:
        max=lst_new[i]
        index=i
print(index)
