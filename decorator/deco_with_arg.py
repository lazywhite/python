def say(worker):
    print('I am worker %s' % worker)
    def dec(fn):
        def wraped(*argv,**kwgs):
            print('staring..')
            fn(*argv,**kwgs)
            print('end.')
        return wraped
    return dec

@say('haha')
def f():
    print('akdfj')

f()

