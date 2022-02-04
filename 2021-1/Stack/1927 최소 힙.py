import sys
import heapq

heap=[]

for _ in range(int(sys.stdin.readline())):
    N=int(sys.stdin.readline())
    if N==0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,N)