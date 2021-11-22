import sys

time=[]
N=int(input())
for _ in range(N):
    start,end=map(int,sys.stdin.readline().split())
    time.append([start,end])

time=sorted(time,key=lambda a:a[0])
time=sorted(time,key=lambda a:a[1])

tmp=0
cnt=0

for i, j in time:
    if i>=tmp:
        cnt+=1
        tmp=j

print(cnt)