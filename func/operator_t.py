#methodcaller
#from operator import methodcaller

#class People:
#    def call(self):
#        print('calling ...')

#p = People()

#foo = methodcaller('call')
#foo(p)
# ======================================
#itemgetter
#from operator import itemgetter

#f = itemgetter(2)
#print(f(range(10,15)))
#dct = dict(key='value')
#g = itemgetter('key')
#print(g(dct))
# ======================================
#attrgetter
#from operator import attrgetter

#class A:
#    attr = 10

#a = A()

#f = attrgetter('attr')
#print(f(a))
