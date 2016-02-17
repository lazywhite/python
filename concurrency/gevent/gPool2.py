import gevent
from gevent import getcurrent
from gevent.pool import Group

group = Group()
def hello_from(n):
    print('size of group: %s' % len(group))
    print('hello from Greenlet: %s' % id(getcurrent()))

group.map(hello_from, xrange(3))


def intensive(n):
    gevent.sleep(3-n)
    return 'task', n

print('Ordered')
ogroup = Group()
for i in ogroup.imap(intensive, xrange(3)):
    print(i)

print('Unordered')
ugroup = Group()
for i in ugroup.imap_unordered(intensive, xrange(3)):
    print(i)

