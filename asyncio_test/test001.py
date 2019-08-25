import asyncio


# 定义协程方法
async def do_work(number):
    """
    # 此方法在调用时不会立即被执行，而是返回一个协程对象
    :param number:
    :return:
    """
    print('Number:', number)


# 执行协程方法
crt = do_work(1)
# 这里返回的是一个协程对象
print('Coroutine:', crt)
print('After calling execute')

# 声明事件循环对象
loop = asyncio.get_event_loop()
# 执行协程对象
loop.run_until_complete(crt)
print('After calling loop')


