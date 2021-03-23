T=int(input())

for _ in range(T):
    R,S=input().split()  #여기에는 왜 map으로 받을 필요가 없을까?
    for x in S:
        print(x*int(R), end='')
    print() #줄넘김

#end parameter를 사용하지 않으면 줄 넘김이 되어 나옴
