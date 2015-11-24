#a,*b,c=(1,2,3,4,5)
#print(type(b)) # list
#def f(a,*b):
#    print(type(b)) #tuple
# ========================
# attaching informational metadata to function
#def f(x:int, y:int) ->int:
#    return x+y
#print(f(10,20))
#print(f.__annotations__)
# =======================
#a=(1,2,3)
#b=(4,5,6)
#f= lambda x,y: x+y
#print(list(map(f,a,b)))

# ========================

#names = ['David Beazley', 'Brian Jones', 
#         'Raymond Hettinger', 'Ned Batchelder']

#b = sorted(names, key=lambda name: name.split()[-1].lower())
#print(b)

# ========================
#funcs = [lambda x: x+n for n in range(5)]
#for f in funcs:
#    print(f(0))

#funcs = [lambda x,n=n: x+n for n in range(5)]
#for f in funcs:
#    print(f(0))
# ========================
#replacing single method class with functions
#Class(int_arg).func(func_arg) =  func(outer_arg)(inner_arg)
# =================
# define keyword only args
#def f(a, *, b, c):
#    print(a,b,c)
#f(1,b=2,c=3)
# ========================
## this callback function can't carry extra state information
#def apply_async(func, args, *, callback):
#    '''callback could be a bound method in order to carrying
#    extra state information
#    '''
#    result = func(*args)
#    callback(result)

#def print_result(result):
#    print('Got: ',result)

#def add(x,y):
#    return x+y

#apply_async(add, (2,3), callback=print_result)
# ===========================
#def apply_async(func, args, *, callback):
#    '''callback could be a bound method in order to carrying
#    extra state information
#    '''
#    result = func(*args)
#    callback(result)
#def add(x,y):
#    return x+y

#def make_handler():
#    sequence = 0
#    def handler(result):
#        nonlocal sequence ## this nonlocal is important
#        sequence += 1
#        print('[{}] Got: {}'.format(sequence, result))
#    return handler
#handler = make_handler()
#apply_async(add, (2,3), callback=handler)
#apply_async(add, (2,7), callback=handler)
