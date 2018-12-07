import multiprocessing
#print(multiprocessing.get_all_start_methods())
multiprocessing.set_start_method('spawn')

def f(l, i):
    l.acquire()
    try:
        print('hello', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(10):
        multiprocessing.Process(target=f, args=(lock, i)).start()
