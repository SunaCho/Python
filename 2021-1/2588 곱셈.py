#2588 곱셈

#1

a=int(input())
b=int(input())

k=str(b)

for i in range(2,-1,-1):
    print(a*int(k[i]))
    
print(a*b)

#2

a=int(input())
b=int(input())

k=str(b)
print(a*int(k[2]))
print(a*int(k[1]))
print(a*int(k[0]))

print(a*b)


"""
아래에 곱하는 수를 문자열로 바꾼 다음에 위 수와 곱하기
정수로 바꾸어 곱할 때 또는 정수로 입력받을 때 int를 바깥에 쓰기
"""
