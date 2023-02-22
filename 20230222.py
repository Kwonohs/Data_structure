'''
#균형이진탐색트리      - avl트리
                    - red-vlack
                    - (2,3,4) - 트리
                    - splay tree

'''


'''
#이진탐색트리는 왼쪽자식은 부모노드의 값보다 작거나 같고, 오른쪽자식노드는 부모노드보다 커야한다.
def find_loc(self,key):
    if self.size == 0:
        return None

    p = None
    v = self.root

    while v != None:
        if v.key == key:
            return v
        elif v.key < key: 
            p = v
            v = v.right
        else:
            p = v
            v = v.left


def search(self, key):
    v = self.find_loc(key)
    if v == None:
        return None
    else :
        return v
'''


'''



class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        
    def search(self,key):
        r = self



a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
a.right = c
b.parent = a
c.parent = a
b.right = d
d.parent = b

#이진트리순회
#preorder : Main - Left - Right
#inorder : Left - Main - Right
#postorder : left - right - main

'''


'''
A =[~,~,~,~,~,~]
A.insert(14)
    A.append(14)
    A.heapify-up(len(A)-1)
    def heapify(k):
        while k>0 and A[(k-1)//2] < A[k]:
            A[k], A[(k-1)//2] = A[(k-1)//2], A[k]


'''