import asyncio
import aiohttp
import time
from aiomultiprocess import Pool


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    # 不要忘记挂起关闭请求，这里不挂起会导致请求挂起后，关闭请求无法执行
    await session.close()
    result = await response.text()
    print(result)
    return response


async def do_work():
    url = 'https://www.baidu.com'
    urls = [url for _ in range(5)]
    print(urls)
    async with Pool() as pool:
        result = await pool.map(get, urls)
        print(result)
        return result

start = time.time()
task = asyncio.ensure_future(do_work())
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
end = time.time()
print('总耗时:', end - start)

