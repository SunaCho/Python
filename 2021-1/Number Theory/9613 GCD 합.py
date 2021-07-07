import itertools
import sys

def find_GCD(a,b): #Euclid 호제법
    while True:
        if a==0:
            return b
        tmp=a
        a=b%a
        b=tmp

testcase=int(sys.stdin.readline().rstrip())

for i in range(testcase):
    seq=list(map(int,sys.stdin.readline().rstrip().split()))
    pair=list(itertools.combinations(seq[1:],2))
    result=0
    for i in pair:
        temp=find_GCD(max(i),min(i))
        result+=temp
    print(result)