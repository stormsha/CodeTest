import asyncio
import aiohttp
import time

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    # 不要忘记挂起关闭请求，这里不挂起会导致请求挂起后，关闭请求无法执行
    await session.close()
    return response


async def do_work():
    start_do_work = time.time()
    url = 'https://www.baidu.com'
    print('Waiting for', url)
    result = await get(url)
    print('Get response from', url, 'Result:', result)
    print('当前请求耗时：', time.time() - start_do_work)


tasks = [asyncio.ensure_future(do_work()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时:', end - start)

