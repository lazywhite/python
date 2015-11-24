#class Pair:
#    '''
#        keyword string substitude need a object , not a dict
#    '''
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def __repr__(self):
#        return 'Pair({0.x!r},{0.y!r})'.format(self)

#    def __str__(self):
#        return 'Pair({0.x!s},{0.y!s})'.format(self)

#p = Pair(3,4)

#p # invoke __repr__
#print(p) # invoke __str__
# __format__
# ==============================
# context management protocol
#from socket import socket, AF_INET, SOCK_STREAM
#from functools import partial
#import pdb

#class LazyConnection:
#    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
#        self.address = address
#        self.family = family
#        self.type = type
#        self.sock = None

#    def __enter__(self):
#        print('entering')
#        if self.sock is not None:
#            raise RuntimeError('Already connected')
#        self.sock = socket(self.family, self.type)
#        self.sock.connect(self.address)
#        return self.sock

#    def __exit__(self, a, b, c):
#        self.sock.close()
#        self.sock = None
#        print('leaving')

#pdb.set_trace()
#conn = LazyConnection(('www.python.org', 80))

#with conn as s: #__enter__ invoked at this line
#    s.send(b'GET /index.html HTTP/1.0\r\n')
#    s.send(b'HOST: www.python.org\r\n')
#    s.send(b'\r\n')
#    resp = b''.join(iter(partial(s.recv, 8192), b''))
#    print(resp)
#================================
# property add extra processing to the getting or setting
# attribute of an instance

#import math

#class Circle:
#    def __init__(self, radius):
#        self.radius = radius

#    @property
#    def area(self):
#        return math.pi * self.radius ** 2

#    @property
#    def perimeter(self):
#        return math.pi * self.radius * 2

#c = Circle(10)
#print(c.area)
#print(Circle.area.fget(c))

# ==========================
#class A:
#    def spam(self):
#        print('A.spam')

#class B(A):
#    def spam(self):
#        print('B.spam')
#        super().spam()

#b=B()
#b.spam()
# ========================
# simplify the initializing of Data Structures
#class Structure:
#    _fields = []
#    def __init__(self,*args):
#        if len(self._fields) != len(args):
#            raise TypeError('Except {} arguments'.format(len(self._fields)))
#        for name, value in zip(self._fields, args):
#            setattr(self, name, value)

#if __name__ == '__main__':
#    class Stock(Structure):
#        _fields = ['name', 'share', 'price']

#    class Points(Structure):
#        _fields = ['x', 'y']

#    a = Stock(1,2,3) 
#    print(a.name, a.share, a.price)
#    b = Points(1,2)
#    print(b.x, b.y)
# ================================
# delegating attribute access (proxy)
#class A:
#    def spam(self, x):
#        print(x)

#class B:
#    def __init__(self):
#        self._a = A()

#    #def spam(self, x):
#    #    return self._a.spam(x)
#    def __getattr__(self, name):
#        ''' if there are many methods to delegete, 
#        alternative approach is define this method
#        get called if code tried to access an attribute
#        that doesn't exist
#        '''
#        return getattr(self._a, name)

#b = B()
#b.spam(10)
# ==================================
#class Proxy:
#    def __init__(self, obj):
#        self._obj = obj

#    def __getattr__(self, name):
#        return getattr(self._obj, name)

#    def __setattr__(self, name, value):
#        if name.startswith('_'):
#            super().__setattr__(name, value)
#        else:
#            setattr(self._obj, name, value)

#    def __delattr__(self, name):
#        if name.startswith('_'):
#            super().__delattr__(name)
#        else:
#            delattr(self._obj, name)

#class Spam:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def bar(self):
#        print(self.x, self.y)

#s = Spam(2,3)

#p = Proxy(s)
#p.bar()
# ================================
# create instances in more than one way provided by __init__
# use classmethod
# one of the primary use of class method is to define alternate
# constructer 
#import time

#class Date:
#    def __init__(self, year, month, day):
#        self.year = year
#        self.month = month
#        self.day = day

#    @classmethod
#    def today(cls):
#        t = time.localtime()
#        return cls(t.tm_year, t.tm_mon, t.tm_mday)

#a = Date(2012,3,5)
#b = Date.today() #this will also create a Date instance

# ====================
# state machine
# split the individual states into their own class
#class Connection:
#    def __init__(self):
#        self.new_state(ClosedConnectionState)

#    def new_state(self, newstate):
#        self._state =  newstate
#    
#    def read(self):
#        return self._state.read(self)

#    def write(self, data):
#        return self._state.write(self, data)

#    def open(self):
#        return self._state.open(self)

#    def close(self):
#        return self._state.close(self)

#class ConnectionState:
#    @staticmethod
#    def read(conn):
#        raise NotImplementedError()

#    @staticmethod
#    def write(conn, data):
#        raise NotImplementedError()

#    @staticmethod
#    def open(conn):
#        raise NotImplementedError()

#    @staticmethod
#    def close(conn):
#        raise NotImplementedError()

#class ClosedConnectionState(ConnectionState):
#    @staticmethod
#    def read(conn):
#        raise RuntimeError('Not open')

#    @staticmethod
#    def write(conn, data):
#        raise RuntimeError('Not open')

#    @staticmethod 
#    def open(conn):
#        conn.new_state(OpenConnectionState)

#    @staticmethod
#    def close(conn):
#        raise RuntimeError('Already closed')

#class OpenConnectionState(ConnectionState):
#    @staticmethod
#    def read(conn):
#        print('reading')

#    @staticmethod
#    def write(conn, data):
#        print('writing')

#    @staticmethod
#    def open(conn):
#        raise RuntimeError('Already open')

#    @staticmethod
#    def close(conn):
#        conn.new_state(ClosedConnectionState)

#c = Connection()
#print(c._state)
#c.read()
#c.open()
#print(c._state)
#c.read()
#c.write('hello')
#c.close()
#print(c._state)
# =======================================
#import math

#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def __repr__(self):
#        return 'Point({0.x},{0.y})'.format(self)

#    def distance_to(self, x, y):
#        return math.hypot(self.x - x, self.y - y)

#p = Point(2,3)
#method_name = 'distance_to'
#d = getattr(p, method_name)(0,0)
#print(d)

#from operator import methodcaller
#f = methodcaller(method_name, *args, **kwargs))
#f(p) = p.method_name(*args, **kwargs)
#points = [
#        Point(1, 2),
#        Point(3, 0),
#        Point(10, -3),
#        Point(-5, -7),
#        Point(-1, 8),
#        Point(3, 2)
#        ]

#points.sort(key=methodcaller(method_name, 0, 0))
#print(points)
# =========================
# create a data structure with lots of types, and 
#visit this data structure, process each data with 
#correspond function
#class Node:
#    pass
#class UnaryOperator(Node):
#    def __init__(self, operand):
#        self.operand = operand
#class BinaryOperator(Node):
#    def __init__(self, left, right):
#        self.left = left
#        self.right = right
#class Add(BinaryOperator):
#    pass
#class Sub(BinaryOperator):
#    pass
#class Mul(BinaryOperator):
#    pass
#class Div(BinaryOperator):
#    pass
#class Negate(UnaryOperator):
#    pass
#class Number(Node):
#    def __init__(self, value):
#        self.value = value
# Representation of 1 + 2 * (3 - 4) / 5
#t1 = Sub(Number(3), Number(4))
#t2 = Mul(Number(2), t1)
#t3 = Div(t2, Number(5))
#t4 = Add(Number(1), t3)

#class NodeVisitor:
#    def visit(self, node):
#        methname = 'visit_' + type(node).__name__
#        meth = getattr(self, methname, None)
#        if meth is None:
#            meth = self.generic_visit
#        return meth(node)

#    def generic_visit(self, node):
#        raise RuntimeError('No {} method'.format('visit_'+type(node).__name__))

#class Evaluator(NodeVisitor):
#    def visit_Number(self, node):
#        return node.value
#    def visit_Add(self, node):
#        return self.visit(node.left) + self.visit(node.right)
#    def visit_Sub(self, node):
#        return self.visit(node.left) - self.visit(node.right)
#    def visit_Mul(self, node):
#        return self.visit(node.left) * self.visit(node.right)
#    def visit_Div(self, node):
#        return self.visit(node.left) / self.visit(node.right)
#    def visit_Negate(self, node):
#        return -node.operand

#e = Evaluator()
#print(e.visit(t4))
# ===============================

#import weakref

#class Node:
#    def __init__(self, value):
#        self.value = value
#        self._parent = None
#        self.children = []

#    def __repr__(self):
#        return 'Node{!r:}'.format(self.value)

#    @property
#    def parent(self):
#        '''self._parent is weakref object , self_parent() return repr(node)
#        '''
#        return self._parent if self._parent is None else self._parent()

#    @parent.setter
#    def parent(self, node):
#        self._parent = weakref.ref(node) # 
#    def add_child(self, child):
#        self.children.append(child)
#        child.parent = self

#root = Node('parent')
#print(root.parent)
#c1 = Node('child')
#root.add_child(c1)
#print(c1.parent)
#del root
#print(c1.parent)

# ==================================
# ensure instance created by same arguments is individual
#import weakref
#class Spam:
#    _spam_cache = weakref.WeakValueDictionary()
#    def __new__(cls, name):
#        if name in cls._spam_cache:
#            return cls._spam_cache[name]
#        else:
#            self = super().__new__(cls)
#            cls._spam_cache[name] = self
#            return self

#    def __init__(self, name):
#        print('Initialing Spam')
#        self.name = name


#s = Spam('dave')
#t = Spam('dave')
#print(s is t)

# ==============================
#class Integer:
#    def __init__(self, name):
#        self.name = name
#    def __get__(self,instance,cls):
#        print(instance.__class__,cls.__name__)
#        if instance is None:
#            return self
#        else:
#            return instance.__dict__[self.name]
#    def __set__(self, instance, value):
#        if not isinstance(value, int):
#            raise TypeError('expect an int')
#        instance.__dict__[self.name] = value
#    def __delete__(self, instance):
#        del instance.__dict__[self.name]


#class Point:
#    x = Integer('x')
#    y = Integer('y')
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#p = Point(3,4)
#print(p.__dict__)
#p.x = 5
#print(p.__dict__)
#p.x
# ===================================
#class Integer:
#    def __init__(self, name):
#        self.name = name 
#        self._value = None
#    def __get__(self, instance, cls):
#        return self._value

#    def __set__(self, instance, value):
#        self._value = value

#    def __delete__(self, instance):
#        self._value = None

#class Pair:
#    x = Integer('x')
#    y = Integer('y')
#    def __init__(self, x, y):
#        self.x = x 
#        self.y = y

#p = Pair(2,3)
# property is invoked by __getattribute__
# ============================================
#class LazyProperty:
#    def __init__(self, func):
#        self.func = func
#    def __get__(self, instance, cls):
#        if instance is None:
#            return self
#        else:
#            value = self.func(instance) ## wtf
#            print(instance.radius)
#            setattr(instance, self.func.__name__, value)
#            return value

#import math
#class Circle:
#    def __init__(self, radius):
#        self.radius = radius

#    @LazyProperty
#    def area(self):
#        print('computing area')
#        return math.pi * self.radius ** 2


#c = Circle(3)
#print(c.area)
#print(c.area)

# =================================
#class A:
#    x=10
#    def turn(self,cls):
#        self.__class__ = cls

#class B:
#    y=10
#    def turn(self,cls):
#        self.__class__ = cls

#a = A()
#print(a.__dict__)
#a.turn(B)
#print(a.__dict__)
# ===================================

#class M(object):
#    @classmethod
#    def f(cls):
#        print cls

#class N(M):
#    pass

#M.f()
#N.f()

# ============================
