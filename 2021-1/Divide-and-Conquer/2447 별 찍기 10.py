def star(n):
    lst=[]
    for i in range(3*len(n)):
        if i//len(n)==1:
            lst.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else:
            lst.append(n[i%len(n)]*3)
    return list(lst)

stars=["***","* *","***"]
n=int(input())
k=0
while n!=3:
    n=int(n/3)
    k+=1

for i in range(k):
    stars=star(stars)
for i in stars:
    print(i)