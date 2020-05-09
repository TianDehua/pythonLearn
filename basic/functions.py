# 函数

#常规函数
def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    return a + b

#默认参数
def sumWithdefault(a, b=1):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    return a + b

#可变参数
def sumArgs(*args):
    sum = 0
    for item in args:
        if isinstance(item, (int, float)):
            sum += item
    return sum

#关键字参数
def sumKw(a, b, **kw):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    sum = a + b
    print("sum=", sum, "kw=", kw)

#命名关键字参数
def sumWithMul(a, b, *, sub, mul):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(sub, (int, float)) or not isinstance(mul, (int, float)):
        raise TypeError('bad operand type')
    sum = a + b
    sum -=  sub
    sum *= mul
    return sum

if __name__ == '__main__':
    s = sum(1, 2)
    print('s=', s)
    s = sumWithdefault(1, 2) #默认参数的使用
    print('s=', s)
    s = sumWithdefault(1) #默认参数的使用
    print('s=', s)
    s = sumArgs(1, 2, 3, 4) #可变参数
    print('s=', s)
    s = sumArgs(1, 2) #可变参数
    print('s=', s)
    l = list(range(1, 11))
    s = sumArgs(*l) #可变参数, 结合list
    print('s=', s)
    sumKw(1, 2, user='tdh', pwd='admin') #关键字参数
    d = {'user':'tdh', 'pwd':'admin'}
    sumKw(1, 2, **d) #关键字参数，结合dict
    s = sumWithMul(1, 2, sub=1, mul=3) #命名关键字参数
    print('s=', s)
    # sum('a', 'b')


