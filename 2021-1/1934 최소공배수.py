'''

case=int(input())
for _ in range(case):
    a,b=map(int,input().split())
    i=max(a,b)
    while(True):
        if i%a==0 and i%b==0:
            print(i)
            break
        i+=1

case=int(input())
for _ in range(case):
    a,b=map(int,input().split())
    c=max(a,b)
    for i in range(c,(a*b+1)):
        if i%a==0 and i%b==0:
            print(i)
            break
'''
        
#아래가 정답이라고 한다. 테스트 케이스가 너무 많아서 시간 초과되는 것 같다.

def LCM(a,b):
    d=GCD(a,b)
    return int((a*b)/d)
def GCD(A,B):
    return GCD(B%A,A) if B%A else A
case=int(input())
for _ in range(case):
    a,b=map(int,input().split())
    print(LCM(a,b))
    



