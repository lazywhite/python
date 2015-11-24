import select 
'''
/proc/sys/fs/aio-nr 文件提供了系统范围异步 I/O 请求现在的数目。
/proc/sys/fs/aio-max-nr 文件是所允许的并发请求的最大个数
'''

class EventHandler(object):
    def fileno(self):
        'return the associated file descriptor'
        raise NotImplemented('must implement')

    def wants_to_recv(self):
        'return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'return True if sending is requested'
        return False

    def handle_send(self):
        'send outgoing data'
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_recv()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv , can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()
