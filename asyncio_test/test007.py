import asyncio
import requests
import time

start = time.time()


async def do_work():
    start_do_work = time.time()
    url = 'https://stormsha.com/'
    print('Waiting for', url)
    response = requests.get(url)
    print('Get response from', url, 'Result:', response)
    print('当前请求耗时：', time.time() - start_do_work)


tasks = [asyncio.ensure_future(do_work()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时:', end - start)

