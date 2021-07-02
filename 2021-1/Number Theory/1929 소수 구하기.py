import sys

isPrime=[False]*1000001

for i in range(2,1000001):
    if i*i>1000000:
        break
    if isPrime[i] is False:
        for j in range(i*i,1000001,i):
            isPrime[j]=True


num=list(map(int,sys.stdin.readline().split()))
for i in range(num[0], num[1]+1,1):
    if isPrime[i]==False:
        print(i)