import sys
num=int(input())
lst=[]

for i in range(num):
    age,name=map(str,sys.stdin.readline().split())
    age=int(age)
    lst.append((age,name))
    
f=sorted(lst,key=lambda x:(x[0]))

for x, y in f:
    print(x, y)
