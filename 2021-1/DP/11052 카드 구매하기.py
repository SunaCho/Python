N=int(input())
num=list(map(int,input().split()))
num=[0]+num

dp=[0]*1001

for i in range(N+1):
    for j in range(i+1):
        dp[i]=max(dp[i],num[j]+dp[i-j])

print(dp[N])

# 와 num 받을 때 뜬금없이 for문 걸어서...
# IndexError 날 이유가 없는데?? 하다가 한참 못 풀었다 바보다