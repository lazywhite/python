'''
    create a class as metaclass
    then define it's __new__ method
    at last use type to create and return a class
'''

from __future__ import print_function 
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    attrs = ((name, value) for name, value in future_class_attr.items() 
            if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    return type(future_class_name, future_class_parents, uppercase_attr)

#__metaclass__ = upper_attr

class Foo(metaclass=upper_attr):
    foo = 'biu'


print(dir(Foo))


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr=dict((name.upper(),value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)



class Bar(metaclass=UpperAttrMetaclass):
#    __metaclass__ = UpperAttrMetaclass
    bar = 'bar'

print(dir(Bar))
