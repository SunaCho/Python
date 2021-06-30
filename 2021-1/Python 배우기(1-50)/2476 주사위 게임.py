N=int(input())

num_new=[]
result=[]

for _ in range(N):
    num=list(map(int,input().split()))
    num.sort()
    
    for i in num:
        if i not in num_new:
            num_new.append(i)
          
        else:
            for x in range(2):
                num_new.append(i)

    if len(num_new)==5:
        result.append(10000+1000*num_new[0])
    elif len(num_new)==4:
        result.append(1000+100*num_new[1])
    else:
        num_new.sort()
        result.append(100*num_new[2])
            
    num_new.clear()


result.sort()
print(result[N-1])
