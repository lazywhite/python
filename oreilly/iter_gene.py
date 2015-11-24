#import sys
#with open('/etc/passwd', 'r') as f:
#    while True:
#        line = next(f, None)
#        if line is None:
#            sys.exit(0)
#        elif line.startswith('#'):
#            pass
#        else:
#            print(line, end='')
# ==========================
#class Node:
#    def __init__(self, value):
#        self._value = value
#        self._children = []
#    def __repr__(self):
#        return 'Node({!r})'.format(self._value)

#    def add_child(self, node):
#        self._children.append(node)

#    def __iter__(self):
#        return iter(self._children)

#root = Node(0)
#child1 = Node(1)
#child2 = Node(2)

#root.add_child(child1)
#root.add_child(child2)
#b=iter(root)
#print(next(b))
#print(next(b))
#for x in iter(root):
#    print(x)
# ==================
with open('test.txt', 'wt', encoding='utf-8') as f:
    print('hello', file=f)
