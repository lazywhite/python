#class deduper:
#    _queue = []
#    def __init__(self,a_list):
#        self.a_list = a_list

#    def sort_list(self):
#        for i in self.a_list:
#            if i not in self._queue:
#                self._queue.append(i)
#            else:
#                pass
#        return self._queue

#a=[1,1,2,3,3,4,5,6]

#b = deduper(a)
#print(b.sort_list())
# ======================

#def f(n):
#    a, b = 0, 1
#    while n >=0:
#        a,b = b, a+b
#        n -= 1
#        print(b, end=',') 

#f(4)


# ===================
#class Singleton:
#    _list = {}
#    def __new__(cls, name, *args, **kwargs):
#        if name in cls._list:
#            return cls._list[name]
#        else:
#            obj = super().__new__(cls)
#            cls._list[name] = obj
#            return obj
#    def __init__(self, name, *args, **kwargs):
#        pass

#a = Singleton('bob')
#b = Singleton('bob')
#if a is b:
#    print('same')
# ==============

