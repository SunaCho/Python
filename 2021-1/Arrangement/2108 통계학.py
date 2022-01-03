from collections import Counter
import sys

lst=[]
for _ in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    lst.append(num)
lst.sort()
cnt=Counter(lst).most_common(2)

print(round(sum(lst)/len(lst)))
print(lst[len(lst)//2])

if len(lst)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(lst)-min(lst))