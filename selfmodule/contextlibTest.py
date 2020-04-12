from contextlib import contextmanager, closing
from urllib.request import urlopen

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

# 通过__enter__和__exit__这两个方法实现上下文管理，可以使用with简写
with Query('Bob') as q:
    q.query()

# 下面这个通过contextmanager，和with实现一样的效果，注意yield
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
