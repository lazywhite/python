import gevent

def foo():
    print 'running in foo'
    gevent.sleep(0)
    print 'explicit context switch to foo again'

def bar():
    print 'explicit context switch to bar'
    gevent.sleep(0)
    print 'implicit context switch to bar again'


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
