# -*- coding: utf-8 -*-
#
# Copyright © 2017 white <white@Whites-Mac-Air.local>
#
# Distributed under terms of the MIT license.

"""
"""

from threading import Thread
import time

def run():
    '''
    while True:
        print 'adkfj;'
        time.sleep(1)
    '''

    def hh(name):
        while True:
            print 'print by %s' % name
            time.sleep(1)
        
    t1 = Thread(target=hh, args=("t1", )) 
    t2 = Thread(target=hh, args=("t2", )) 

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def main():
    thread = Thread(target=run, args=()) 
    print dir(thread)
    print thread.isAlive()
    thread.start()
    print thread.is_alive()
    
    thread.join()

if __name__ == '__main__':
    main()
