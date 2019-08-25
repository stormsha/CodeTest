import asyncio
import requests


async def do_work():
    url = 'https://stormsha.com/'
    status = requests.get(url)
    return status


coroutine = do_work()
task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('Task Result:', task.result())

