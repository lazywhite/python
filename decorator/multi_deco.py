# use class as decorator
# func = deco(func)
# func(arg) = deco(func)(arg)

class Deco(object):
    def __init__(self,func):
        self.func = func
        
    def __call__(self,a_string):
        print 'deco print'
        self.func(a_string)

@Deco
def f(a_string):
    print "func print" ,a_string


f('something')

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

#func = deco_one(deco_two(func))

@deco_one
@deco_two
def f(a_str):
    print "func print" , a_str


f(100)
