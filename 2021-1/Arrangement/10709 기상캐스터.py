H,W=map(int,input().split())
ans=[]


for i in range(H):
    c=input()
    tmp=[]
    num=-1
    for i in range(W):
        if c[i]=='c':
            tmp.append(0)
            num=i
        elif num==-1:
            tmp.append(-1)
        else:
            tmp.append(i-num)
    ans.append(tmp)

for i in ans:
    print(*i)