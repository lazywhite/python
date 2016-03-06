# python use Reference Counting to gc
# only if the last reference of obj is delete, __del__ will be triggered 
class Test(object):
    def __init__(self):
        print 'instance created'
    
    def __del__(self):
        print 'instance deleted'


a = Test()
b = a

del a
print id(b)
