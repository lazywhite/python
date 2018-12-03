import time
import threading
from queue import PriorityQueue

def do_this(n):
    print('do this started')
    time.sleep(n)

    
thread_1 = threading.Thread(target=do_this,args=(10,))
thread_1.daemon = True

thread_1.start()

thread_1.join() # wait until this thread end , will not execute following phases
print(thread_1.is_alive())
print(threading.current_thread())
#print(threading.enumerate())

