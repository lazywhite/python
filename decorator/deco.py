# -*- coding: utf-8 -*-
#!/usr/bin/env python
## 1. 将类作为装饰器
'''
func = deco(func)
func(arg) = deco(func)(arg)
'''

class Deco(object):
    def __init__(self,func):
        self.func = func
        
    def __call__(self,a_string):
        print 'deco print'
        self.func(a_string)

@Deco
def f(a_string):
    print "func print" ,a_string


f('something')

# 2. 多重装饰器
'''
@one
@two
def f():
    pass

相当于
f = deco_one(deco_two(f))  #deco_one在最外面, 附加的特性最先执行
'''
def deco_one(func):
    def _wrapper(arg):
        print 'deco one print'
        func(arg)
    return _wrapper

def deco_two(func):
    def _wrapper(arg):
        print 'deco two print'
        func(arg)
    return _wrapper

#func = deco_one(deco_two(func))

@deco_one
@deco_two
def f(a_str):
    print "func print" , a_str



f(100)


## 3. 对参数数量不确定的函数进行装饰

def deco_three(func):
    def _wrapper(*args, **kwargs):
        print "deco print"
        func(*args, **kwargs)
    return _wrapper

@deco_three
def f(name, age):
    print "func print", name, age

f("bob", 10)


## 4. 带参数的装饰器

def deco_four(deco_args):
    print "deco_args: " , deco_args
    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            print "inside deco"
            func(*args, **kwargs)
        return __wrapper    
    return _wrapper

@deco_four(100)
def f(name, age):
    print "func print", name, age

f("alice", 10)

## 5. 带类参数的装饰器
class Locker:
    lock = False
    def __init__(self):
        print "locker is initialized" 
    
    @classmethod
    def acquire(cls):
        if cls.lock is False:
            print "lock.acquire() is called"
            cls.lock = True;
        else:
            print "waiting for lock"
        
    @classmethod
    def release(cls):
        if cls.lock is True:
            print "lock.release() is called"
            cls.lock = False

def deco_five(cls):
    def _wrapper(func):
        def __wrapper():
            print "before func is called"
            cls.acquire()
            try:
                func()
            except:
                pass
            finally:
                cls.release()
        return __wrapper   
    return _wrapper

@deco_five(Locker)
def f():
    print 'func is called'

f()
