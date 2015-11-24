class A(object):
    def foo(self):
        print 'A has foo'

class B(A):
    def foo(self):
        print 'B has foo'
        super(B,self).foo()

class C(A):
    def foo(self):
        print 'C has foo'
        super(C,self).foo()

class D(B,C):
    def foo(self):
        print 'D has foo'
        super(D,self).foo()

d = D()
d.foo()
