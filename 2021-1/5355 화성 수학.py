num=int(input())
for _ in range (num):
    data=list(map(str, input().split()))
    answer=0
    for i in range(len(data)):
        if i==0:
            answer+=float(data[i])

        else:
            if data[i]=="#":
                answer-=7
            elif data[i]=="%":
                answer+=5
            elif data[i]=="@":
                answer*=3
                
    print("%0.2f"%(answer))

# underscore는 사용하지 않는 값에 대해 이용
# 문자열 탐색에 리스트 이용
