import asyncio
import requests


async def do_work():
    url = 'https://stormsha.com/'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(do_work()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
