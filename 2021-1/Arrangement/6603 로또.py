from itertools import combinations
import sys

while True:
    lst=sys.stdin.readline().split()
    if lst.pop(0)=='0':
        break
    for i in combinations(lst, 6):
        print(" ".join(i))
    print()