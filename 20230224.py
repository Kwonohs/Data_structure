
'''
DFS(길이우선탐색)
BFS(너비우선탐색)
DAG(Directed Acyclic Graph):사이클이 없는 방향 그래프
'''
'''
class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self
        self.rank = 0

    def makeset(self,x):
        return Node(x)
    def find(self,x):
        while x.parent != x.parent:
            x = x.parent
        return x
    def union(self,x,y):
        v, w = find(x), find(y)
        if v.rank > w.rank:
            v.parent = w
        elif v.rank < w.rank:
            w.parent = v
        else:
            w.parent = v
            v.rank += 1
'''
'''
union-find 자료구조
python : Set
a = set() #a = {}
b = {3,5,1,3} => b = { 3,5,1 } #중복은 제거됨

union-find 결합
if v.height > w.height:
    w.parent = v
elif v.height < w.height:
    v.parent = w
else: #v.height = w.height
    상관없이 연결

'''