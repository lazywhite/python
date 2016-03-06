class UpperString(object):
    def __init__(self):
        self._value = ''
        
    def __get__(self,instance,cls):
        print 'value accessed'
        return self._value

    def __set__(self,instance,value):
        print 'value setted'
        self._value = str(value).upper()

    def __delete__(self, instance):
        print 'deleted'


class MyClass(object):
    attribute = UpperString()


a = MyClass()
a.attribute = 'he'
print a.attribute
del a.attribute
