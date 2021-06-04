import asyncio

import aiohttp


async def asyncio_downloading(session: aiohttp.ClientSession, url: str):
    async with session.get(url):
        pass


async def asyncio_example(length=10):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(length):
            task = asyncio.ensure_future(asyncio_downloading(session, ))