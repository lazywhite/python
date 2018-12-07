import multiprocessing



def f(l, i):
    p_name = multiprocessing.current_process().name
    l.acquire()
    try:
        print('hello from %s' % p_name, i)
    finally:
        l.release()


if __name__ == '__main__':
    print(multiprocessing.get_all_start_methods())
    print(multiprocessing.get_start_method())
    '''
    multiprocessing.set_start_method('fork')
    '''
    lock = multiprocessing.Lock()
    for i in range(10):
        multiprocessing.Process(target=f, args=(lock, i)).start()
