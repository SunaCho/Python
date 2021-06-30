num=int(input())

while num!=1: #다 나누어질 때까지
    for i in range(2, num+1):
        if num%i==0:
            print(i)
            num=num//i
            break
