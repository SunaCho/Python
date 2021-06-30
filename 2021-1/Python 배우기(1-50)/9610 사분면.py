num1=0
num2=0
num3=0
num4=0
axis=0

num=int(input())
for _ in range(num):
    a,b=map(int,input().split())
    
    if a>0 and b>0:
        num1+=1
    elif a<0 and b>0:
        num2+=1
    elif a<0 and b<0:
        num3+=1
    elif a>0 and b<0:
        num4+=1
    else:
        axis+=1

print("Q1: %s"%(num1))
print("Q2: %s"%(num2))
print("Q3: %s"%(num3))
print("Q4: %s"%(num4))
print("AXIS: %s"%(axis))
