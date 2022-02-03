#-*-coding:utf-8-*-
# 음... 간단해 보이는데 이걸... 어떻게 분할정복으로 풀지? 고민한 문제


import sys
x,y,z=map(int,sys.stdin.readline().split())

def func(x,n):
    if n==1:
        return x%z
    else:
        tmp=func(x,n//2)
        if n%2==0:
            return (tmp*tmp)%z
        else:
            return (tmp*tmp*x)%z

print(func(x,y))