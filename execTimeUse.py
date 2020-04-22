#使用装饰器， 来计算一个函数的执行时间
import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper
    
@log_execution_time
def calculate_tuple():
    x=(1,2,3,4,5,6)
    return x[3]

@log_execution_time
def calculate_list():
    x=[1,2,3,4,5,6]
    return x[3]


if __name__ == '__main__':
    calculate_tuple()
    calculate_list()