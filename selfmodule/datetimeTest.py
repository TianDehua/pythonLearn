from datetime import datetime, timedelta, timezone

#测试datetime
now = datetime.now()
print(now)
print('type now=', type(now))

#创建时间by数字
dt = datetime(1970, 2, 28, 20, 10, 50)
print(dt)

#时间戳
timestamp = dt.timestamp()
print(timestamp) #5055050.0 单位s，小数点后表示ms

#创建时间by时间戳
dt = datetime.fromtimestamp(timestamp)
print(dt)
print(datetime.utcfromtimestamp(timestamp))

#创建时间by string
dt = datetime.strptime('2015/06/01 18:19:59', '%Y/%m/%d %H:%M:%S')
print(dt)
print(dt.strftime('%a, %d %H:%M'))

#时间运算
print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=10))
