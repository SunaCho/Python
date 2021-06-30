import sys
num=int(input())
lst=[]

for i in range(num):
    name,korean,english,math=map(str,sys.stdin.readline().split())
    korean=int(korean)
    english=int(english)
    math=int(math)
    lst.append((name,korean,english,math))
    
f=sorted(lst,key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(num):
    print(f[i][0])
