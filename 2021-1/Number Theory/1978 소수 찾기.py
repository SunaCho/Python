import sys

isPrime=[False]*1000001

isPrime[1]=True
for i in range(2,1000001):
    if i*i>1000000:
        break
    if isPrime[i] is False:
        for j in range(i*i,1000001,i):
            isPrime[j]=True

N=int(input())
primelist=[int(i) for i in input().split()]

prime=0
for i in range(N):
    if isPrime[primelist[i]]==False:
        prime+=1

print(prime)