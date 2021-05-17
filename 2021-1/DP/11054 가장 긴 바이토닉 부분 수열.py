N=int(input())
num=list(map(int,input().split()))
dp_increase=[1]*N
dp_decrease=[1]*N

for i in range(N):
    for j in range(i):
        if num[i]>num[j]:
                dp_increase[i]=max(dp_increase[i],dp_increase[j]+1)

for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        if num[i]>num[j]:
            dp_decrease[i]=max(dp_decrease[i],dp_decrease[j]+1)

result=[0]*N

def ResultAppend():
    for i in range(N):
        result[i]=dp_increase[i]+dp_decrease[i]-1

ResultAppend()
print(max(result))