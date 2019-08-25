import asyncio


async def do_work(number):
    print('Number:', number)
    return number


coroutine = do_work(1)
print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print('Task:', task)
loop.run_until_complete(task)
print('task.result:', task.result())
print('Task:', task)
print('After calling loop')

