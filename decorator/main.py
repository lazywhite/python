# -*- coding: utf-8 -*-
#
# Copyright © 2018 white <white@Whites-Mac-Air.local>
#
# Distributed under terms of the MIT license.


def deco1(func):
    def _wrapper():
        print("inside deco1")
        func()
    return _wrapper

def deco2(func):
    def _wrapper():
        print("inside deco2")
        func()
    return _wrapper

# 多重修饰器, 相当于deco1(deco2(func))
@deco1
@deco2
def func():
    print("test")


# 带参数的修饰器
def deco3(arg):
    def _wrapper(func):
        print("deco arg:",  arg)
        def __wrapper(*args, **kwargs):
            print("inside deco3")
            func(*args)
        return __wrapper
    return _wrapper


@deco3(100)
def fun(*args, **kwargs):
    print(args)
    print(kwargs)



# 修饰类方法
class Test:
    @deco3(200)
    def run(self, arg1, arg2):
        print(arg1, arg2)


Test().run(10, 20)
