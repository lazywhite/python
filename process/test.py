from multiprocessing import Process
import time 
import atexit
import sys
import os

running_process = []
def f(name):
    print os.getpid()
    print os.getppid()
    print __name__
    print globals()
    while True:
        print("hello " + name)
        time.sleep(10)

def terminate():
    for p in running_process:
        p.terminate()

if __name__ == '__main__':
    atexit.register(terminate)
    p = Process(target=f, args=('outer',))
    running_process.append(p)
    p.start()
    p.join()
