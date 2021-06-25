import sys
lst=input().strip()

sum=0
stack=[0]

for i in range(1,len(lst)):
    if lst[i]=='(':
        stack.append(0)
    elif lst[i]==')':
        if stack[-1]==0:
            if len(stack)>1:
                stack[-2]+=1
            stack.pop()
        elif stack[-1]!=0:
            if len(stack)>1:
                stack[-2]+=stack[-1]
            sum+=1+stack[-1]
            stack.pop()

print(sum)