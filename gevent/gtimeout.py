import gevent

seconds = 3
timeout = gevent.Timeout(seconds)


def wait(tmout):
    print('running in greenlet')
    tmout.start()
    gevent.sleep(20)

try:
    gevent.spawn(wait, timeout).join()
    gevent.spawn(wait, timeout).join()

except gevent.Timeout:
    print('could not complete')


