num=int(input())
num_list=[]

for i in range(num):
    a=int(input())
    num_list.append(a)

num_list.sort()

for j in range(len(num_list)-1):
    while num_list[j]!=num_list[j+1]:
        if (j+1)/num>0.5:
            print("Junhee is not cute!")
        else:
            print("Junhee is cute!")
        break
    
if num_list.count(1)==num:
    print("Junhee is cute!")
elif num_list.count(0)==num:
    print("Junhee is not cute!")
