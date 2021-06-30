num=int(input())
vote=str(input())
vote_list=[]
vote_list.extend(list(vote))
vote_list.sort()
numA=vote_list.count("A")

if numA==num:
    print("A")

elif numA==0:
    print("B")

else:     
    for i in range(num-1):
        if vote_list[i]!=vote_list[i+1]:
            if (i+1)/num>0.5:
                print("A")
            elif (i+1)/num==0.5:
                print("Tie")
            else:
                print("B")
            break
