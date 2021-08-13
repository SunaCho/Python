import sys

N=int(sys.stdin.readline())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

first=0
second=0
third=0

def clip_paper(x,y,n):
    global first, second, third
    num_check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if (paper[i][j]!=num_check):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x+k*n//3, y+l*n//3, n//3)
                return

    if num_check==-1:
        first+=1
    elif num_check==0:
        second+=1
    else:
        third+=1

clip_paper(0,0,N)
print(f'{first}\n{second}\n{third}')