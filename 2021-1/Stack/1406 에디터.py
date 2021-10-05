from sys import stdin

stack=list(stdin.readline().strip())
lst=[]

txt=int(stdin.readline())

for line in stdin:
    if line[0]=='L':
        if stack:
            lst.append(stack.pop())
        else:
            continue
    elif line[0]=='D':
        if lst:
            stack.append(lst.pop())
        else:
            continue
    elif line[0]=='B':
        if stack:
            stack.pop()
        else:
            continue
    elif line[0]=='P':
        stack.append(line[2])

print(''.join(stack+list(reversed(lst))))
