a,b=map(int, input().split())
c=int(input())

a += c//60
b += c%60

if b>=60:
    a+=1
    b-=60
if a>=24:
    a-=24

print(a,b)


'''
// 몫만큼 더하기
% 나머지만큼 더하기
+=, -= 그만큼 더하거나 뺀 결과를 저장
'''
