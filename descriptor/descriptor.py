class UpperString(object):
    def __init__(self):
        self._value = ''
        
    def __get__(self,instance,cls):
        return self._value

    def __set__(self,instance,value):
        self._value = str(value).upper()

    def __delete__(self, instance):
        print 'deleted'


class MyClass(object):
    attribute = UpperString()


a = MyClass()
print a.attribute
a.attribute = 'he'
print a.attribute
del a.attribute
