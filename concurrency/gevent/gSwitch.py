from gevent import monkey;monkey.patch_all()

import gevent


## gevent will execute one greenlet until got block operation
## then switch to another greenlet

def g1():
    for i in range(10):
        print(i)
        if i == 6:
            print('execute until block')
            gevent.sleep(0)


def g2():
    for i in range(10):
        print(i)
        if i == 3:
            print('execute until block')
            gevent.sleep(0)

gevent.joinall([
    gevent.spawn(g1),
    gevent.spawn(g2),
])
