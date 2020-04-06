# -*- coding: utf-8 -*-

# 斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a,b = b, a+b
        n += 1
    return 'done'

#调用生成器，有两种方式：
#1. 通过next,越界会抛出异常
g = fib(6)
# for x in range(6): #超过6就会越界
#     print('next=', next(g))
#2. 通过迭代器
for x in g:
    print('x=', x)

#杨辉三角
def triangles():
    L=[]
    while True:
        if len(L)<2:
            L.append(1)
        else:
            L=[L[x]+L[x+1] for x in range(len(L)-1)]
            L.insert(0, 1)
            L.append(1)
        yield L

g=triangles()
for x in range(10):
    print('L=',next(g))
