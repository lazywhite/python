class MyClass(object):
    def __init__(self):
        self._secret_thing = 1


    def _i_get(self):
        print "getter"
        return self._secret_thing

    def _i_set(self, value):
        print "setter"
        self._secret_thing = value

    def _i_delete(self):
        print "deleter"

    my_thing = property(_i_get, _i_set, _i_delete, 'property description')


class C(object):
    def __init__(self,name,age):
        self.name = name
        self._x = age

    @property
    def x(self): 
        print 'x getter'
        return self._x

    @x.setter
    def x(self, value): 
        print 'x setter'
        self._x = value

    @x.deleter
    def x(self):
        print 'x deleter'
        del self._x

a = MyClass()
print a.my_thing
a.my_thing = 10
print a.my_thing
del(a.my_thing)

c=C('mary',20)
print(c.x)
c.x = 100
print(c.x)
del(c.x)
