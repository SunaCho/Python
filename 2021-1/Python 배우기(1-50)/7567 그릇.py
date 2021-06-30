dish=str(input())
dish_list=[]
dish_list.extend(list(dish))

height=10

for i in range(len(dish_list)-1):
    if dish_list[i]==dish_list[i+1]:
        height+=5
    else:
        height+=10

print(height)
