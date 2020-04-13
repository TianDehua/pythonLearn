import json
class School(object):
    def __init__(self, name, studentCnt, address):
        self.name = name
        self.studentCnt = studentCnt
        self.address = address
    def __str__(self):
        return "shchool name:%s, studentCnt:%d, address:%s" % (self.name, self.studentCnt, self.address)

def school2dict(sch):
    return {
        'name':sch.name,
        'studentCnt': sch.studentCnt,
        'address': sch.address
    }

# School对象转化为json
sch = School('zhengZhouMiddle', 569, "zhengZhou Gaoxin")
sch2j = json.dumps(sch, default=school2dict)
print("school to Json=", sch2j)

def dict2school(d):
    return School(d['name'], d['studentCnt'], d['address'])

print('__dict__=', sch.__dict__)

#json转化为School对象
print('json to school:')
j2sch = json.loads(sch2j, object_hook=dict2school)
print(type(j2sch))
print(j2sch)
