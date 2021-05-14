N=int(input())
num=list(map(int,input().split()))
dp=[1]*N
dp[0]=num[0]

for i in range(1,N):
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i],dp[j]+num[i])
        else:
            dp[i]=max(dp[i],num[i])

print(max(dp))

'''
한 문장 바뀌었는데 어떻게 푸는지 모르겠더란다...
11053을 리스트에 원소 모두를 append하는 방식으로 풀어서 틀렸는데
sum을 구하려면 그렇게 풀어야 편하지 않나? 싶어서 우물 잘못 파다가
다시 돌아와서 풀었당....
'''