#이걸 분할해서 풀 수 있나? 싶어서 찾아봤는데 리스트 합하는 게 제일 빠른 것 같다.

import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
nmlist = list(map(int, input().split())) + list(map(int, input().split()))
nmlist.sort()
print(' '.join(map(str, nmlist)))
