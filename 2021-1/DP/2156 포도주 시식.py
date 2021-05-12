num=int(input())
dp=[0]
grape=[0]
for i in range(num):
    grape.append(int(input()))
dp.append(grape[1])
if num>1:
    dp.append(grape[1]+grape[2])

for i in range(3,num+1):
    dp.append(max(dp[i-1],dp[i-2]+grape[i],dp[i-3]+grape[i-1]+grape[i]))

print(dp[num])