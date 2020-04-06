#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools

def now():
    print("2020-04-06")

# 打印函数的名称
print(now.__name__)

f = now
print(f.__name__)

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def time1():
    print("16:04")

#执行time看效果
time1
()

def logWithStr(text):
    def decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrappers
    return decorator

@logWithStr('exec')
def time2():
    print("16:08")

time2()
print(time.__name__)
print(time2.__name__)
