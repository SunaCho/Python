import sys

quene=[]
N=int(input())

for i in range(N):
    cmd=list(map(str,sys.stdin.readline().split()))
    if cmd[0]=='push':
        quene.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if quene:
            print(quene.pop(0))
        else:
            print("-1")
    elif cmd[0]=='size':
        print(len(quene))
    elif cmd[0]=="empty":
        if len(quene)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if quene:
            print(quene[0])
        else:
            print("-1")
    elif cmd[0]=='back':
        if quene:
            print(quene[-1])
        else:
            print("-1")