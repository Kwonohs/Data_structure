'''
union-find 자료구조
python : Set
a = set() #a = {}
b = {3,5,1,3} => b = { 3,5,1 } #중복은 제거됨

'''
'''
red-black tree : 가장 유명하고 많이 사용되는 균형이진탐색트리
1. 노드 <- red/black으로 이루어져있다.
2. root노드는 black이다.
3. leef node(None)은 black이다.
4. red 노드의 child 노드는 black이다.
5. 각 노드 -> leef node까지 경로의 black노드의 갯수는 다 같아야한다.

'''
'''
AVL트리 : BST트리에 특징을 상속받으면서, 자식부트리의 높이차 <=1인 트리
class Node : BST 동일하다.

'''