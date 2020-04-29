import asyncio
async def test1():
    print("1")
    await test2()
    print("2")
async def test2():
    print("3")
    print("4")

# 这是python3.4以前写法
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test1())

asyncio.run(test1())
