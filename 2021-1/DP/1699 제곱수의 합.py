num=int(input())
dp=[i for i in range(num+1)]

for i in range(1,num+1):
    for j in range(1,i):
        if j*j>i:
            break
        if dp[i]>dp[i-j*j]+1:
             dp[i]=dp[i-j*j]+1

print(dp[num])

# 코드는 짧은데 시간 제한 때문에 너무 오래 걸렸다.
# 사실 처음에는 1~316 제곱수 리스트를 만들어서 탐색해 봤는데 역시 시간 초과 걸렸고...
# for 안에 while문 넣었다가 시간 초과 걸려서 바꿨다.