import asyncio


async def do_work(number):
    print('Number:', number)
    return number


coroutine = do_work(1)
print('Coroutine:', coroutine)
print('After calling execute')

# 声明task对象
task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task.result:', task.result())
print('Task:', task)
print('After calling loop')

