import itertools

# 基本的生成器，用()类似列表生成式
g = (x*x for x in range(1, 10))

# 复制两份 g, 测试用，生成器只能遍历一次(接下来，请使用g1, g2遍历)
g1, g2 = itertools.tee(g, 2)

for i in g1:
    print('for g=', i)

# 遍历, 使用next，越界会抛出StopIteration异常
try:
    for i in range(0, 20):
        print('next=', next(g2))
except StopIteration as e:
    print("next遍历，越界会抛出异常")
finally:
    print("注意迭代的个数，而且迭代器只能遍历一次")

