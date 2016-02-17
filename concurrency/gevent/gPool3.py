import gevent
from gevent.pool import Pool
'''pool size'''
pool = Pool(2)
def hello_from(n):
    print("size of pool %s" % len(pool))

pool.map(hello_from, xrange(3))


class SocketPool(object):
    def __init__(self):
        self.pool = Pool(10000)
        self.pool.start()

    def listen(self, socket):
        while True:
            socket.recv()


    def add_handler(self, socket):
        if self.pool.full():
            raise Exception("At maxium pool size")
        else:
            self.pool.spawn(self.listen, socket)

    def shutdown(self):
        self.pool.shutdown()
