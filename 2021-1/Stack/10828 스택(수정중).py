import sys

stack=[]
N=int(input())
for i in range(N):
    x,y=map(sys.stdin.readline().split())
    if x=='push':
        stack.append(y)
    elif x=='pop':
        stack[-1]=pop
        stack.pop()
        if len(stack)==0:
            print(-1)
        else:
            print(pop)
    elif x=='size':
        print(len(stack))
    elif x=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])