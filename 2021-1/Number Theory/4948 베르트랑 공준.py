# 임의의 자연수에 대하여 n보다 크고 2n보다 같거나 작은 소수는 적어도 하나 존재한다.
import math
import sys

def prime(num):
    if num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

lst=list(range(2,246912))
prime_lst=[]

for i in lst:
    if prime(i):
        prime_lst.append(i)

while(1):
    ans=0
    n=int(sys.stdin.readline())
    if n==0:
        break

    for i in prime_lst:
        if n<i<=n*2:
            ans+=1
    
    print(ans)