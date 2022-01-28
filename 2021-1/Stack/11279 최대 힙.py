#-*-coding:utf-8-*-
# 일반 리스트 대신 힙 구현하기 (시간제한)

import sys
import heapq

heap=[]
N=int(sys.stdin.readline())
for _ in range(N):
    M=int(sys.stdin.readline())
    if M==0:
        if len(heap)==0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap,(-1)*M)