h,m=map(int,input().split())


if m>=45:
    print("%s %s"%(h,m-45))
else:
    if h==0:
        print("%s %s"%(23, 15+m))
    else:
        print("%s %s"%(h-1, 15+m))
