import sys

S=sys.stdin.readline().rstrip()

suffixes=[]

for i in range(len(S)):
    suffixes.append(S[i:])

suffixes.sort()

for _ in suffixes:
    print(_)
