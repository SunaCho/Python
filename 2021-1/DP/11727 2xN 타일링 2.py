n=int(input())
dp=[0,1,3,5]
for i in range(4,n+1):
    dp.append(dp[i-1]+2*dp[i-2])

print(dp[n]%10007)

'''
(리스트)
dp=[0,1,3,5]
0은 인덱스, 1은 num=1일 때, 3는 num=2일 때 출력 값
(경우의 수)
1) 2*(n-1) 타일에다 2*1 배치
2) 2*(n-2) 타일에다 1*2 2개 배치 또는 2*2 1개 배치
(점화식)
state(n)=state(n-1)+2*state(n-2)
'''