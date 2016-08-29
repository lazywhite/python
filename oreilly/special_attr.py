# comparator
class A:
    def __init__(self, value):
        self.value = value
    def __ge__(self, obj):
        return self.value >= obj.value
    def __gt__(self, obj):
        return self.value > obj.value
    def __le__(self, obj):
        return self.value <= obj.value

a = A(10)
b = A(20)
print(a>=b)
print(a>b)



class Pair:
    '''
        keyword string substitude need a object , not a dict
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return 'Pair({0.x!s},{0.y!s})'.format(self)

p = Pair(3,4)
#p:  invoke __repr__
#print(p):  invoke __str__



## __slot__: save memory space when creating large number of instance
class Date:
    __slots__ = ['year', 'month', 'day'] 

    def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day

