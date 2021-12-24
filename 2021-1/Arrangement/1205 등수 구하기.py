N, new, P=map(int,input().split())

if N:
    lst=list(map(int,input().split()))
    lst.append(new)
    lst.sort(reverse=True)
    num=lst.index(new)+1
    if num>P:
        print(-1)
    else:
        if N==P and new==lst[-1]:
            print(-1)
        else:
            print(num)

else:
    print(1)