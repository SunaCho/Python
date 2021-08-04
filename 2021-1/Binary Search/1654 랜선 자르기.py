import sys

K,N=map(int,sys.stdin.readline().split())
lst=[int(sys.stdin.readline()) for i in range(K)]
lst.sort()

low=1
high=max(lst)

while high>=low:
    middle=(high+low)//2
    c=0
    for i in lst:
        c+=i//middle
    
    if c>=N:
        low=middle+1
    else:
        high=middle-1

print(high)