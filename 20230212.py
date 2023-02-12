'''class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

        #yield yield는 return이라고 생각하면 되는 iterator 도구이다.

    def pushFromt(self,key):
        new_node = Node(key)
        new_node.next = L.head
        self.head = new.node
        self.size += 1
    def pushBack(self,key):
        v = Node(key)
        if len(self) == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size += 1
'''
'''class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Q is empty")
            return False
        else :
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def priqueue(self,index):
        return(self.items[index])

q = Queue()
for i in range(9):
    q.enqueue(i)
    print(q.priqueue(i))
'''

'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)


S = Stack()
k = input("괄호 맞추기")
for p in k:
    print(p)
    if p == '(':
        S.push(p)

    elif p == ')':
        S.pop
    else :
        print("입력 제대로 해라")

if len(S) > 0: print("False")
else: print("True")
'''

