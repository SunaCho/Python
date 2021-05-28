N=int(input())

for _ in range(N):
    num=int(input())
    year=[]
    for _ in range(num):
        school, drink=map(str,input().split())
        year.append([school,int(drink)])

    year=sorted(year,key=lambda x:x[1])
    print(year[-1][0])