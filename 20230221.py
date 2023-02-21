'''
Heap성질 : 모든 부모노드의 key값은 자식노드의  key값보다 작지 않다.
'''
'''

class hash:
   def __init__(self):
        self.h = []


    def find_slot(self,key):
'''
'''
충돌회피방법(colision resolution method)
-open addressing : linear probing
                    quadratic probing
                    double hashing
- chaining
'''
'''
dictionary 는 key와 value값을 가진다.
D = {}
D['202120083"] = "권오셈"
D["202120084"] = "김한나"
위에 세개의 행은 D라는 딕셔너리에 2개의 값을 저장한다.
또 다른 딕셔너리 저장방법
D = {202120083 : "권오셈", 202120084 : "김한나"} 이런식으로 저장할 수 있다.

'''
'''
class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self.key
        self.prev = self.key

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    #def Splice(self,a,b,x):

    def search(self,key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next

        return None


    def remove(self,x):
        if x == None or x == self.head:
            return None
        x.prev.next = x.next
        x.next.prev = x.prev

        del x

    #def popFront:
    #def popBack
'''


