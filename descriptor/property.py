class MyClass(object):
    def __init__(self):
        self._secret_thing = 1


    def _i_get(self):
        return self._secret_thing

    def _i_set(self, value):
        self._secret_thing = value

    def _i_delete(self):
        print('neh !!')

    my_thing = property(_i_get, _i_set, _i_delete, 'the thing')


class C(object):
    def __init__(self,name,age):
        self.name = name
        self._x = age
    @property
    def x(self): 
#        raise AttributeError #self._x
        return self._x
    @x.setter
    def x(self, value): self._x = value
    @x.deleter
    def x(self):
        del self._x

c=C('mary',20)
print(c.x)
