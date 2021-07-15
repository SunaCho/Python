import sys

def square(A,P):
    a=str(A)
    result=0
    for i in a:
        result+=pow(int(i),P)
    return result

def DFS(A,P,iteration,visit_list):
    if visit_list[A]!=0:
        return visit_list[A]-1
    visit_list[A]=iteration
    Sq=square(A,P)
    iteration+=1
    return DFS(Sq,P,iteration,visit_list)

A,P=map(int,sys.stdin.readline().split())

visit_list=[0]*(9**5)*5
iteration=1

print(DFS(A,P,iteration,visit_list))