class Student(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 打印格式化
    def __str__(self):
        return "Student object (name: %s, age:%d)" % (self.name, self.age)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #往后轮动一次
        if self.a > 1000:
            raise StopIteration()
        return self.a #返回下一个值
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

def test():
    s = Student("tdh", 31)
    print(s)
    f = Fib()
    for i in f:
        print(i)
    print('f[2]=', f[2])
    print('f[0:5]=', f[:5])


if __name__ == "__main__":
    test()
