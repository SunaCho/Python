import sys

num=int(sys.stdin.readline())
cnt=0
res=[]
stack=[]
message=True

for i in range(num):
    inpt=int(sys.stdin.readline())

    while cnt<inpt:
        cnt+=1
        stack.append(cnt)
        res.append("+")
    
    if stack[-1]==inpt:
        stack.pop()
        res.append("-")
    else:
        message=False
        break


if message==False:
    print("NO")
else:
    print("\n".join(res))
