#函数式编程
#函数可作为参数，返回值

from functools import reduce
import functools

# map, reduce, filter, sort
def testAdvanced():
    # test map
    L = list(range(1, 11))
    print(L)
    L = map(lambda x: x*x, L) #注意，这里的返回值不是list
    print(L)
    L = list(L)
    print(L)
    # test reduce
    sum = reduce(lambda a,b: a+b, L)
    print('sum=', sum)
    # test filter
    L = list(filter(lambda item: item < 50, L))
    print(L)
    # test sorted
    L.append(10)
    L.append(20)
    L.append(30)
    L.append(-25)
    L.append(40)
    print('before sorted:', L)
    L = sorted(L, key=abs, reverse=True)
    print('after sorted:', L)

# 闭包
def lazysum(*args):
    def sum():
        total = 0
        for item in args:
            total += item
        return total
    return sum

# 装饰器
def log(func):
    @functools.wraps(func) 
    def wrapper(*args, **kw):
        print('--exec func {}'.format(func.__name__))
        func(*args, **kw)
    return wrapper

#@xxx,会把函数传进去
@log
def sayHelloWorld():
    print('hello world')

# 类装饰器
class LogWrap:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kw):
        print('--exec func {}'.format(self.func.__name__))
        self.func(*args, **kw)

@LogWrap
def sayHelloWorldToo():
    print('hello world')

if __name__ == '__main__':
    # 测试高级函数
    testAdvanced()

    # 测试闭包
    L = list(range(1, 20))
    f = lazysum(*L)
    sum = f()
    print('sum=', sum)

    # 测试装饰器
    sayHelloWorld()
    sayHelloWorldToo()
