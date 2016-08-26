# 1. iterator
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)

root.add_child(child1)
root.add_child(child2)
b=iter(root)
print(list(b))


a = list(range(10))
b = iter(a)
print(type(b)) # --> listiterator




# 2. generator

def gen(n):
    while n >= 0:
        yield n
        n -= 1


g = gen(10)
print(type(g))
print(list(g))
