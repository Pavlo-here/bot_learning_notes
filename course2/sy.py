import asyncio

async def send_one() -> None:
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        print(f'Пройшло {n} секунд')


async def main() -> None:
    task_1 = asyncio.create_task(send_one())
    await task_1

if __name__ == "__main__":
    asyncio.run(main())