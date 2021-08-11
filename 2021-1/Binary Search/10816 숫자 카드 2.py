#10815 응용
#이분탐색은 아무리 돌려도 시간 초과가 뜬다. 리스트로 너무 풀고 싶었다... 블로그 참고해서 딕셔너리로 풀었다.

'''
import sys

n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
lst.sort()
dic={}

for c in lst:
    if c not in dic:
        dic[c]=1
    else:
        dic[c]+=1

m=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

for i in nums:
    left=0
    right=n-1
    while left<=right:
        middle=(left+right)//2
        if lst[middle]==i:
            break
        if lst[middle]>i:
            right=middle-1
        else:
            left=middle+1
    if lst[middle]==i:
        print(dic[i],end=" ")
    else:
        print(0,end=" ")

'''


import sys
n=int(input())
lst_1=list(map(int,sys.stdin.readline().split()))
m=int(input())
lst_2=list(map(int,sys.stdin.readline().split()))

dic=dict()
for i in lst_1:
    try:
        dic[i]+=1
    except:
        dic[i]=1

for i in lst_2:
    try:
        print(dic[i],end=" ")
    except:
        print(0,end=" ")