#한 전봇대를 기준으로 정렬 후 가장 증가하는 부분 수열(LIS, 11053번) 찾기

N=int(input())
lst_1=[]
lst_2=[]

dp=[0]*N

for i in range(N):
    lst_1.append(list(map(int,input().split())))
    lst_1.sort(key=lambda x:x[0])

for i in range(N):
    lst_2.append(lst_1[i][1])

for i in range(N):
    for j in range(i):
        if lst_2[i]>lst_2[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(N-max(dp))