import sys

def gcd(x,y):
    while(y!=0):
        tmp=x%y
        x=y
        y=tmp
    return x

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
for i in range(1,N):
    res=gcd(lst[0],lst[i])
    print('{0}/{1}'.format(lst[0]//res,lst[i]//res))