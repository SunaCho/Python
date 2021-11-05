import sys

def sol():
    lst.sort(reverse=True)
    for i in range(N):
        lst[i]=lst[i]*(i+1)
    return max(lst)

N=int(sys.stdin.readline())
lst=[]
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

print(sol())