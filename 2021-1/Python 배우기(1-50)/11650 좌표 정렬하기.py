import sys
num=int(input())
lst=[0 for _ in range(num)]

for i in range(num):
    lst[i]=list(map(int,sys.stdin.readline().split()))

f=sorted(lst,key=lambda x:(x[0],x[1]))

for x, y in f:
    print(x, y)

# 지금까지 input() 만 쓰고 sys import의 필요성을 몰랐는데
# 시간초과를 해결해준다는 걸 알았다.
