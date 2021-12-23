#pypy3


N = int(input())
row = [0]*15
res = 0

def check_True(n): #행에 열을 넣으면서 들어갈 수 있는지 판단
    for i in range(n):
        if row[n] == row[i] or abs(row[i]-row[n]) == n-i:
            return False
    return True
        
def dfs(n):
    global res
    if n == N: #n개 모두가 들어갔다.
        res += 1
        return
    
    for i in range(N):
        row[n] = i
        if check_True(n):
            dfs(n+1)


dfs(0)
print(res)
