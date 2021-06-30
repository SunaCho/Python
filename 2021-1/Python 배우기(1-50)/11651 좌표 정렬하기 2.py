import sys
num=int(input())
lst=[0 for _ in range(num)]

for i in range(num):
    lst[i]=list(map(int,sys.stdin.readline().split()))

f=sorted(lst,key=lambda x:(x[1],x[0]))

for x, y in f:
    print(x, y)
