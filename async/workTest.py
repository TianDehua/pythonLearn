
import asyncio

async def worker_1():
    print('worker_1 before sleep')
    await asyncio.sleep(1)
    print('worker_1 after sleep')
    return 1

async def worker_2():
    print('worker_2 before sleep')
    await asyncio.sleep(2)
    print('worker_2 after sleep')
    return 2 / 0

async def worker_3():
    print('worker_3 before sleep')
    await asyncio.sleep(3)
    print('worker_3 after sleep')
    return 3

async def main():
    print('start main__')
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    print('main__ before sleep')
    await asyncio.sleep(2)
    print('main__ after sleep')
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)


asyncio.run(main())
