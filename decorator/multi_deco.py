#!/usr/bin/python2.6

# use class as decorator
# the apply rule of multiple decorator is up to bottom
# func = deco(func)
# func(arg) = deco(func)(arg)

#class Deco(object):
#    def __init__(self,func):
#        self.func = func
#        
#    def __call__(self,a_string):
#        print 'deco print'
#        self.func(a_string)

#@Deco
#def f(a_string):
#    print "func print" ,a_string


#f('something')


def deco_one(func):
    def _wrapper(arg):
        print 'deco one print'
        func(arg)
    return _wrapper

def deco_two(func):
    def _wrapper(arg):
        print 'deco two print'
        func(arg)
    return _wrapper


@deco_one
@deco_two
def f(a_str):
    print "func print" , a_str


f(100)
