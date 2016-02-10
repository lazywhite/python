import gevent

def foo():
    print('running in foo')
    gevent.sleep(10)
    print('explicit switching to foo')

def bar():
    print('running in bar')
    gevent.sleep(5)
    print('explicit switching to bar')



gevent.joinall([
    gevent.spawn(bar),
    gevent.spawn(foo),
    ])

