num=list(map(int,input().split()))
num.sort()

if num[0]==num[1]==num[2]:
    print(10000+num[1]*1000)

elif num[0]==num[1] or num[1]==num[2]:
    print(1000+num[1]*100)

else:
    print(num[2]*100)
