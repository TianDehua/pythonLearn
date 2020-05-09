#集合

# 测试列表，增删改查，遍历
def testList():
    # 定义一个列表
    L1 = [1, 2, 3, 4]
    L2 = list()

    print(L1)
    # 删
    L1.pop()
    print(L1)
    # 增
    L1.append(5)
    # 删
    L1.pop(2)
    # 改查
    L1[-1] = 5
    print(L1)
    print("第一个元素", L1[0], "最后一个元素", L1[-1])
    # 遍历
    for item in L1:
        print(item)
    # 索引遍历
    for index, item in enumerate(L1):
        print('({}, {})'.format(index, item))

    L2.append(1)
    L2.append(2)
    print(L2)

# 测试set, 增删查
def testSet():
    # 定义一个set
    S1 = {1, 2, 3, 4}
    S2 = set()

    S1.add('a')
    print(S1)
    S1.remove(4)
    print(S1)
    if 2 in S1:
        print('2 in S1')
    else:
        print('2 not in S1')
    for item in S1:
        print(item)
    
    S2.add('a')
    S2.add('b')
    print(S2)

# 测试dict，
def testDict():
    # 定义一个dict
    D1 = {'a':1, 'b':2, 'c':3}
    D2 = dict()

    print(D1)
    #增
    D1['d'] = 4
    #改
    D1['a'] = 0
    print(D1)
    #查
    if 'a' in D1:
        print('a in D1')
    else:
        print('a not in D1')
    #删
    D1.pop('b')
    #查
    d = D1.get('m', None)
    print('d=', d)
    #遍历
    for item in D1:
        print(item)
    for value in D1.values():
        print(value)
    for k, v in D1.items():
        print('{}, {}'.format(k, v))

    D2['a'] = 1
    D2['b'] = 2
    print(D2)


if __name__ == "__main__":
    #testList()
    #testSet()
    testDict()