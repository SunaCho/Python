h,m,s=map(int, input().split())
time=int(input())

s+=time%60
time=time//60


if s>=60:
    m+=1
    s-=60

m+=time%60
time=time//60

if m>=60:
    h+=1
    m-=60

h+=time%24

if h>=24:
    h-=24

print(h,m,s)
