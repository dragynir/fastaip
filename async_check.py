import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)



async def main2():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")


async def main():
    task1 = asyncio.create_task(
        say_after(4, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    task3 = asyncio.create_task(say_after(5, "what"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    time.sleep(10)

    # Запускаем таски
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")


async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i*i


async def main():
    async for i in async_generator():
        print(i)



class async_generator:
    def __init__(self, stop):
        self.i = 0
        self.stop = stop

    async def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        self.i += 1
        if self.i <= self.stop:
            await asyncio.sleep(1)
            return i * i
        else:
            raise StopAsyncIteration


async def main():
    async for i in async_generator(3):
        print(i)


if __name__ == '__main__':
    asyncio.run(main())
    print('Cat')

    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(main())
    # finally:
    #     loop.run_until_complete(
    #         loop.shutdown_asyncgens())  # see: https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens
    #     loop.close()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
