import multiprocessing
import time

def f(n):
    print('started')
    time.sleep(n)



p = multiprocessing.Process(target=f, args=(10,))
q = multiprocessing.Process(target=f, args=(10,))

p.start()
q.start()
print(multiprocessing.cpu_count())
#print(p.is_alive())


