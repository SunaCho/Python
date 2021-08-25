import sys

isPrime=[False]*1000001

for i in range(2,1000001):
    if i*i>1000000:
        break
    if isPrime[i] is False:
        for j in range(i*i,1000001,i):
            isPrime[j]=True


lst=[]
N=int(sys.stdin.readline())
M=int(sys.stdin.readline()) 


for i in range(N,M+1):
    if N==1:
        for i in range(2,M+1):
            if isPrime[i]==False:
                lst.append(i)
        break

    elif N>=2:
        if isPrime[i]==False:
            lst.append(i)

lst.sort()
if len(lst)!=0:
    print(sum(lst))
    print(lst[0])
else:
    print('-1')