dp=[0,1,1,2]
N=int(input())

for i in range(4,N+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])

'''
DP로 풀었다.
복잡할 줄 알았는데, 쓰고 보니 점화식 형태가 피보나치라서 쉽게 풀었다.
뒷자리 2개에 대입하는 수가 i-1과 i-2 뒷자리 갯수의 합임을 이용했다.
'''