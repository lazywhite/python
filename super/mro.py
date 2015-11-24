class A(object):
    def foo(self):
        print 'a foo'


class B(A):
    def foo(self):
        print 'b foo'
        super(B,self).foo()


class C(A):
    def foo(self):
        print 'c foo'
        super(C,self).foo()

class D(B,C):
    def foo(self):
        print 'd foo'
        super(D,self).foo()


d=D()
d.foo()
