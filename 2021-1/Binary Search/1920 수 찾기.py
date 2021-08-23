import sys

N=int(sys.stdin.readline())
lst_i=sorted(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
lst_f=map(int,sys.stdin.readline().split())

def binary(l,lst_i,start,end):
    if start>end:
        return 0
    M=(start+end)//2
    if l==lst_i[M]:
        return 1
    elif l<lst_i[M]:
        return binary(l,lst_i,start,M-1)
    else:
        return binary(l,lst_i,M+1,end)

for l in lst_f:
    start=0
    end=len(lst_i)-1
    print(binary(l,lst_i,start,end))