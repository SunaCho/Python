N=list(int(input()) for _ in range(5))

def list_edit():
    i=0
    for i in range(5):
        if N[i]<=40:
            N[i]=40

list_edit()
S=sum(N)
print("%.0f"%(S/5))
