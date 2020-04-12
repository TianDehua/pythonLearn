import itertools

# count 创建一个无限的迭代器，用于数字，第一参数start，第二个参数step默认1
natuals = itertools.count(1, 2)
for n in natuals:
    print(n)
    if(n > 10):
        break

# takewhile表示取出一部分
ns = itertools.takewhile(lambda x: x<=20, natuals)
print(list(ns))

print(type(natuals))

# cycle 创建一个无限循环序列， 参数是一个iterable
cs = itertools.cycle('abc')
cnt = 0
for c in cs:
    print(c)
    cnt += 1
    if cnt > 10:
        break
print(type(cs))

# repeat 创建一个不断重复的序列，第二个参数表示count，不指定则无限
ns = itertools.repeat('ab', 3)
for n in ns:
    print(n)

# chain 把一组迭代对象串联起来
for c in itertools.chain('abc', 'XYZ', '123'):
    print(c)


# groupby 把迭代器中相邻的重复元素挑出来
for key, group in itertools.groupby('aaaaAAAbbbBB'):
    print(key, list(group))

#计算圆周率 **表示乘方的意思
def pi(n):
    return 4*sum(map(lambda x: (-1)**((x-1)/2)/x, itertools.takewhile(lambda x: x < 2*n, itertools.count(1, 2))))
print(pi(10000))
