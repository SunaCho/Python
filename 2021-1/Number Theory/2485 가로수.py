def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


N=int(input())
lst=[int(input()) for _ in range(N)]

ans=0
distance=[]

for i in range(1, N):
    distance.append(lst[i]-lst[i-1])

lst_set=list(set(distance))

num=lst_set[0]

for i in range(1, len(lst_set)):
    num=gcd(num, lst_set[i])

for i in distance:
    ans+=i//num-1

print(ans)