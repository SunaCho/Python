import sys

isPrime=[False]*1000001

for i in range(2,1000001):
    if i*i>1000000:
        break
    if isPrime[i] is False:
        for j in range(i*i,1000001,i):
            isPrime[j]=True

while True:
    num=int(sys.stdin.readline())
    if num==0:
        break
    for i in range(2,1000001):
        if isPrime[i] is False:
            j=num-i
            if isPrime[j] is False:
                print(num,"=",i,"+",j)
                break