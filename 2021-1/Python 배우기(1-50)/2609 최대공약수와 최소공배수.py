a, b = map(int, input().split())
for i in range(a+1,1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

for j in range(b,(a*b)+1):
    if j%a==0 and j%b==0:
        print(j)
        break
