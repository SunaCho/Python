#집합으로도 간단하게 풀 수 있을 것 같다. (if i in set...)
import sys

n=int(input())
lst=list(map(int,sys.stdin.readline().split()))
lst.sort()

def binary(num):
    left=0
    right=n-1
    while left<=right:
        middle=(left+right)//2
        if lst[middle]==num:
            return 1
        elif lst[middle]>num:
            right=middle-1
        else:
            left=middle+1
    return 0

input()
for num in list(map(int,sys.stdin.readline().split())):
    print(binary(num),end=' ')