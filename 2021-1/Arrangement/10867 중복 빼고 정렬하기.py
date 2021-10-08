N=int(input())
lst=list(map(int,input().split()))

lst=list(set(lst))
lst.sort()

for i in lst:
    print(i, end=" ")

#별 거 아닌 문제라서 민망하지만... 백신 맞고 컨디션이 나빠서 마지막 print 리스트 붙이는 것도 헤맸다. 아이고야.