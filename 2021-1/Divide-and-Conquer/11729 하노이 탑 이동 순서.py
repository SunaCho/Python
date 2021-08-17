import sys

def hanoi(n,frm,to,otr):
    if n<2:
        print(frm,to) #판이 하나일 때, from에서 to로 이동 후 종료
        return
    hanoi(n-1,frm,otr,to) #마지막 판 제외 나머지를 목적지가 아닌 다른 판에 재귀적으로 쌓는다
    print(frm,to) #마지막 판을 to로 이동
    hanoi(n-1,otr,to,frm) #목적지가 아닌 다른 원반에 옮긴 판들을 재귀적으로 to로 이동

n=int(sys.stdin.readline())
print((2**n)-1)
hanoi(n,1,3,2)