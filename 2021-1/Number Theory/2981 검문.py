import sys
import math
N=int(sys.stdin.readline())
lst=[]
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

tmp=lst[-1]-lst[0]
divisor=[tmp]

for i in range(2,int(math.sqrt(tmp)+1)):
    if tmp%i==0:
        divisor.append(i)
        divisor.append(tmp//i)

divisor=list(set(divisor))
divisor.sort()

for d in divisor:
    for i in range(N):
        if i==N-1:
            print(d,end=" ")
        elif lst[i]%d!=lst[i+1]%d:
            break