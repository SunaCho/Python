import sys
A,B=map(int,sys.stdin.readline().split())

def gcd(x,y):
    mod=x%y
    while mod>0:
        x=y
        y=mod
        mod=x%y
    return y

print('1'*gcd(A,B))