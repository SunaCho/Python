import sys

def dfs(start,dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i,dic)

computer=int(sys.stdin.readline())
pair=int(sys.stdin.readline())
dic={}
visited=[]

for i in range(computer):
    dic[i+1]=set()
for i in range(pair):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

dfs(1,dic)
print(len(visited)-1)