A=100
B=100
num=int(input())

for i in range(num):
    num1, num2=map(int,input().split())
    if num1>num2:
        B-=num1
    elif num1<num2:
        A-=num2

print(A)
print(B)
