'''
실패 코드

N=int(input())
num=list(map(int,input().split()))
dp_length=[]

for i in range(0, N):
    dp=[]
    dp.append(num[i])
    for j in range(i+1,N):
        if num[j]>dp[-1]:
            dp.append(num[j])
    dp_length.append(len(dp))

print(max(dp_length))

저장으로는 반례가 끝이 없어서 (1,5,2,3 등) LIS 개념을 배웠다.
'''

N=int(input())
num=list(map(int,input().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))