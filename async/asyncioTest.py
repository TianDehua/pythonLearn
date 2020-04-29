import asyncio

#这是python3.4和以下版本写法
# @asyncio.coroutine
# def test(i):
# 	print("test_1",i)
# 	yield from asyncio.sleep(1)
# 	print("test_2",i)
# loop=asyncio.get_event_loop()
# tasks=[test(i) for i in range(5)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#这是python3.5以后的写法
async def test(i):
	print("test_1",i)
	await asyncio.sleep(1)
	print("test_2",i)

tasks=[test(i) for i in range(5)]
asyncio.run(asyncio.wait(tasks))
