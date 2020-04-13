import pickle
import json

# 序列化
d = dict(name='Bob', age=20, score=88)
bDumps = pickle.dumps(d)
print(bDumps)

# 反序列化
dLoads = pickle.loads(bDumps)
print(dLoads)

# 序列化到文件
with open('dump', 'wb') as f:
    bDump = pickle.dump(d, f)
    print('pickle dump to file:')
    print(bDump)

# 从文件反序列化
with open('dump', 'rb') as f:
    dLoad = pickle.load(f)
    print('pickle load from file:')
    print(dLoad)

# dict转化为json
print("dict to json:")
jd = json.dumps(d)
print(jd)

# json转化为dict
print('json to dict')
dj = json.loads(jd)
print(dj)
