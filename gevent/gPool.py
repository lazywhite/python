import gevent
from gevent.pool import Group


def talk(msg):
    for i in xrange(3):
        print(msg)

g1 = gevent.spawn(talk, 'foo')
g2 = gevent.spawn(talk, 'bar')
g3 = gevent.spawn(talk, 'fizz')

group = Group()
group.add(g1)
group.add(g2)
group.join()
print('#####')
group.add(g3)
group.join()
