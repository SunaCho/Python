import sys

def preorder(node): # 전위 순회 (왼>오)
    print(node,end='')
    left,right=tree[node][0], tree[node][1]
    if left!='.':
        preorder(left)
    if right!='.':
        preorder(right)

def inorder(node): # 중위 순회 (왼>루트>오)
    left,right=tree[node][0], tree[node][1]
    if left!='.':
        inorder(left)
    print(node,end='')
    if right!='.':
        inorder(right)

def postorder(node): # 후위 순회 (왼>오>루트)
    left,right=tree[node][0], tree[node][1]
    if left!='.':
        postorder(left)
    if right!='.':
        postorder(right)
    print(node,end='')

N=int(sys.stdin.readline())
tree={}

for i in range(1,N+1):
    node,left,right=sys.stdin.readline().split()
    tree[node]=[left,right]

preorder('A'); print()
inorder('A'); print()
postorder('A'); print()