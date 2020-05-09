# 高级特性

#切片
def testSlice():
    L = list(range(10))
    L1 = L[2:]
    L2 = L[2:-1]
    print(L)
    print(L1)
    print(L2)

#列表生成式
def getgenList():
    L = [x*x for x in range(1, 11)]
    return L
def getgenList2():
    L = [x*x for x in range(1, 11) if x > 5]
    return L
def getgenList3():
    L = [x*x if x > 5 else -x for x in range(1, 11)]
    return L
#generator 有两种方式，见gen1(), gen2()
def gen1():
    L = (x*x for x in range(1, 11))
    return L

def gen2():
    base = 1
    while(True):
        yield base * base
        base += 1
    return 'done'

if __name__ == '__main__':
    #测试切片
    testSlice()

    #测试列表生成式
    print(getgenList())
    print(getgenList2())
    print(getgenList3())

    #测试generator
    g1 = gen1()
    while(True):
        try: 
            print(next(g1))
        except StopIteration:
            print('g1 next stop')
            break 

    g2 =gen1()
    for item in g2:
        print(item)
    print('g2 next stop')

    g3 = gen2()
    for i in range(10):
        print(next(g3))
