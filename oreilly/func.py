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
