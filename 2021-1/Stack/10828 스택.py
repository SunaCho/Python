import sys

stack=[]
N=int(input())

for i in range(N):
    cmd=list(map(str,sys.stdin.readline().split()))
    if cmd[0]=='push':
        stack.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print("-1")
