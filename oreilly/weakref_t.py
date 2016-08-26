import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node{!r:}'.format(self.value)

    @property
    def parent(self):
        '''self._parent is weakref object , self_parent() return repr(node)
        '''
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node) # 

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

root = Node('parent')
print(root.parent)
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root
print(c1.parent)




# ensure instance created by same arguments is individual
# Singleton
class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initialing Spam')
        self.name = name


s = Spam('dave')
t = Spam('dave')
print(s is t)
