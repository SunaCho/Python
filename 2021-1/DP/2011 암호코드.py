num=input()
num_list=list(num)
dp=[0]*(len(num_list)+1)
dp[0]=1
dp[1]=1

if int(num_list[0])==0:
    print("0")
else:
    for i in range(1,len(num_list)):
        if int(num_list[i])>0 and int(num_list[i])%10!=0:
            dp[i+1]+=dp[i]
        temp=10*int(num_list[i-1])+int(num_list[i])
        if temp>=10 and temp<=26:
            dp[i+1]+=dp[i-1]
    print(dp[len(num_list)]%1000000)