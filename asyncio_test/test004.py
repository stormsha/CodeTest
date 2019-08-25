import asyncio
import requests


async def do_work():
    url = 'https://stormsha.com/'
    status = requests.get(url)
    return status


def callback(task_result):
    print('Status:', task_result.result())


coroutine = do_work()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)

