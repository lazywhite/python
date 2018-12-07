import gevent

def foo():
    print('running in foo')
    gevent.sleep(2)
    print('explicit switching to foo')

def bar():
    print('running in bar')
    gevent.sleep(1)
    print('explicit switching to bar')



#gevent.joinall([
#    gevent.spawn(bar),
#    gevent.spawn(foo),
#    ])

## start greenlet in cureent ioloop
gevent.spawn(bar).start()
gevent.spawn(foo).start()

## wait other greenlet finish
gevent.sleep(100)
