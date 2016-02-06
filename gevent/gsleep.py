import gevent
from gevent.event import AsyncResult
a = AsyncResult()
b = AsyncResult()
def asetter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    a.set('Hello!')

def awaiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(a.get())

def bsetter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    b.set('Hello!')

def bwaiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(b.get())
     
gevent.joinall([
    gevent.spawn(asetter),
    gevent.spawn(awaiter),
    gevent.spawn(bsetter),
    gevent.spawn(bwaiter),
])
