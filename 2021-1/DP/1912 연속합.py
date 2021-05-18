N=int(input())
num=list(map(int,input().split()))

def dp_partial_sum(arr):
    temp_partial_sum=[0]*len(arr)
    temp_partial_sum[0]=arr[0]
    for i in range(0,len(arr)):
        temp_partial_sum[i]=max(temp_partial_sum[i-1],0)+arr[i]
    print(max(temp_partial_sum))

dp_partial_sum(num)