#11021

num=int(input())

for i in range(num):
    a,b=map(int, input().split())
    result=a+b
    print("Case #%s: %s"%(i+1,result))

#11022
    
num=int(input())

for i in range(num):
    a,b=map(int, input().split())
    result=a+b
    print("Case #%s: %s + %s = %s"%(i+1,a,b,result))


'''
for 구문 안에서 돌리면 변수를 여러 개 만들 필요 없음
%s 이후 여러 개 대입하려면 %(소괄호 안 콤마로 연결)
'''
