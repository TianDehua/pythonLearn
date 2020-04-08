# -*- coding: utf-8 -*-
def trim(s):
    if len(s) == 0 :
        return s
    start=0
    while s[start]==' ' :
        start+=1
    end=len(s)
    while s[end-1]==' ' and end>start :
        end-=1
    return s[start:end]
	
print(trim('hello  '))

# 关键字参数
def person(name, age, **kw):
    print("name=", name, "age=", age, "other=", kw)

person('zhangSan', 18)
person('liSi', 23, city='shangHai', job="soft")
person('Tian', 30, city='zhengZhou')

extra = {'city':'shangHai', 'job':"soft"}
person('liSi', 23, **extra)

# 命名关键字参数
def city(name, range, *, peopleCnt, where):
    print("name=", name, "range=", range, "peopleCnt=", peopleCnt, "where=",where)

city("zhengZhou", 15, where="heNan", peopleCnt=100)