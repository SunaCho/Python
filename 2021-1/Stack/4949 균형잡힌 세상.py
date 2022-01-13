import sys

while True:
    s=sys.stdin.readline().rstrip()
    stack=[]
    flag=1
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flag=0
                break
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                flag=0
                break
    if s=='.':
        break
    print("yes" if flag and not(stack) else "no")