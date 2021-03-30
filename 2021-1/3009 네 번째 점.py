a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

x=[]
y=[]
x.extend([a,c,e])
y.extend([b,d,f])

x.sort()
y.sort()

new_x=[]
new_y=[]

for num in x:
    if num not in new_x:
        new_x.append(num)
    else:
        new_x.remove(num)

for num in y:
    if num not in new_y:
        new_y.append(num)
    else:
        new_y.remove(num)
     
new=new_x+new_y
new=[int (i) for i in new]
print(" ".join(repr(e) for e in new))
