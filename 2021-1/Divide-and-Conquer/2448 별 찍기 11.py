import math

stars=['  *   ', ' * *  ', '***** ']
def triangle(shift):
    count=len(stars)
    for i in range(count):
        stars.append(stars[i]+stars[i])
        stars[i]= ("   " * shift + stars[i] + "   " * shift)

n=int(input())
k=int(math.log(int(n/3),2))
for i in range(k):
    triangle(int(pow(2,i)))
for i in range(n):
    print(stars[i])