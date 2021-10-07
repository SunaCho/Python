N=int(input())
lst=[]

for _ in range (N):
    word=str(input())
    cnt=len(word)
    lst.append((word,cnt)) 

lst=list(set(lst))
lst.sort(key=lambda word: (word[1], word[0]))

for word in lst:
    print(word[0])

# sys import하면 Indent 들어간다!