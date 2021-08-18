# 어떻게 압축되는지 모르겠어서 헤멨다. 0이나 1로 묶일 수 있을 때까지 사각형을 분할하는 게 아이디어.


n=int(input())
lst=[list(map(int,input())) for _ in range(n)]

def quadtree(x,y,n):
    if n==1:
        return str(lst[x][y])
    res=[]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j]!=lst[x][y]:
                res.append('(')
                res.extend(quadtree(x,y,n//2))
                res.extend(quadtree(x,y+n//2,n//2))
                res.extend(quadtree(x+n//2,y,n//2))
                res.extend(quadtree(x+n//2,y+n//2,n//2))
                res.append(')')
                return res
    return str(lst[x][y])

print(''.join(quadtree(0, 0, n)))