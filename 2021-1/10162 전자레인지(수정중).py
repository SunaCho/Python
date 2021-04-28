time=int(input())
numA=0
numB=0
numC=0
timelist=[]

def timecheck():
    global numA, numB, numC
    if time//300!=0:
        numA+=(time//300)
        timelist.append(numA)
    if (time-numA*300)//60!=0:
        numB+=((time-numA*300)//60)
        timelist.append(numB)
    if (time-numA*300-numB*60)//10!=0:
        numC+=((time-numA*300-numB*60)//10)
        timelist.append(numC)
    if len(timelist)==0:
        print("-1")
        
timecheck()

if len(timelist)!=0:
    timelist_new=[int (i) for i in timelist]
    print(" ".join(repr(e) for e in timelist_new))