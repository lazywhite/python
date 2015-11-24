import time
import threading
from queue import PriorityQueue

def do_this(n):
    print('do this started')
#    started_event.set()
    time.sleep(n)

thread_name_list = [ 'thread_'+str(i) for i in range(1,11) ]
priority_list = range(0,100,10)

thread_queue = PriorityQueue(maxsize=15)

class MyThread(threading.Thread):
    def __init__(self, priority, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.priority = -priority

for item in zip(priority_list, thread_name_list):
    thread = MyThread(*item, target=do_this, args=(2,),daemon=False)
    thread_queue.put((thread.priority, thread))

while not thread_queue.empty():
    thread_item = thread_queue.get()
    thread_item[1].run()
    print(thread_item[0])

    
# =================================================
#thread = MyThread('haha', 20, target=do_this, args=(10,))

#thread_1 = threading.Thread(target=do_this,args=(10,))
#thread_1.daemon = True

#started_event = threading.Event()

#thread_1.start()

#started_event.wait(timeout=5)
#print('do this is running')
#thread_1.join() # wait until this thread end , will not execute following phases
#print(thread_1.is_alive())
#print(threading.current_thread())
#print(threading.enumerate())

