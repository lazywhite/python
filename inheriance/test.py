
class A(object):
    m = 1

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

print c.m
print b.m
print a.m

c.m = 10
print c.m
print b.m
print a.m

b.m = 20
print c.m
print b.m
print a.m
