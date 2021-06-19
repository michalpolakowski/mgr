import asyncio
import time

import aiohttp


async def asyncio_downloading(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return await response.read()


async def asyncio_example(length=10):
    start = time.time()
    urls = [
                "https://www.python.org",
                "https://www.google.com/",
            ] * 80
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(length):
            print(f'id: {i}')
            for url in urls:
                tasks.append(asyncio.create_task(asyncio_downloading(session, url)))
            await asyncio.gather(*tasks)
    stop = time.time()
    return start, stop

