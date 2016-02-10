from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore()

def worker1(n):
    sem.acquire()
    print('worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print('worker %i released semaphore' % n)


def worker2(n):
    with sem:
        print('worker %i acquired semaphore' % n)
        sleep(0)
    print('worker %i released semaphore' % n)


pool = Pool()
pool.map(worker1, xrange(0, 2))
pool.map(worker2, xrange(3, 6))

