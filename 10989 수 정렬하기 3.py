import sys

N=int(sys.stdin.readline())
res=[0]*10001

for i in sys.stdin:
    res[int(i)]+=1

for i in range(10001):
    if res[i]>0:
        for j in range(res[i]):
            print(i)

# input 대신 sys.stdin.readline() 사용
# for문으로 수를 저장하니까 무조건 메모리 초과가 떠서
# 리스트를 만들어서 인덱스를 출력하는 걸로 짰다