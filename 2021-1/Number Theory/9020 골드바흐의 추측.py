#골드바흐의 체

isPrime=[False]*1000001

for i in range(2,1000001):
    if i*i>1000000:
        break
    if isPrime[i] is False:
        for j in range(i*i,1000001,i):
            isPrime[j]=True

num=int(input())
for i in range(num):
    a=int(input())
    b=a//2
    for j in range(b,1,-1):
        if isPrime[a-j]==False and isPrime[j]==False:
            print(j,a-j)
            break
    