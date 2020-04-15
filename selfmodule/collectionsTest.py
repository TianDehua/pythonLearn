from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

# nametuple, 一个最精简的类实现
Point = namedtuple('Point', ['x','y'])
print(type(Point))
p = Point(1, 2)
print('x=', p.x, 'y=', p.y)
print('p=',p)

# deque, 双向列表
q = deque(['a','b','c'])
q.append('x')
print('after append, q=', q)
q.appendleft('y')
print('after appen left, q=', q)
q.popleft()
print('after popleft, q=', q)

# defaultdict, key不存在时，返回一个默认值
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print('dd key1=', dd['key1'], 'dd key2=', dd['key2'])

# OrderedDict, 有序的dict，注意这里的有序是指插入顺序
d = dict([('a', 1), ('b', 2), ('c', 3)])
print('d=', d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('od=', od)

# ChainMap
default = {'color':'red', 'user':'guest'}
args = {'key':'123345', 'color':'green'}

combined = ChainMap(args, default)

print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


# Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1
#等同于下面代码
#c.update('programming')
print(c)
c.update('hello') #增加统计源
print(c)


