import asyncio


async def my_async_func():
    print("I'm dooin someth")
    await asyncio.sleep(0)
    print("Continue doin someth")


coroutine = my_async_func()


while True:
    try:
        coroutine.send(None)
    except StopIteration:
        break
