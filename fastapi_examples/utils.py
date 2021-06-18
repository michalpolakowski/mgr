from typing import Optional

import aiohttp
import requests


class SingletonSession:
    session: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_session(cls) -> aiohttp.ClientSession:
        if not cls.session:
            cls.session = aiohttp.ClientSession()
        return cls.session

    @classmethod
    async def fetch_url(cls, url: str) -> bytes:
        session = cls.get_session()

        async with session.get(url) as res:
            return await res.read()

    @classmethod
    async def destroy_session(cls) -> None:
        if cls.session:
            await cls.session.close()
            cls.session = None


def create_aiohttp_session():
    SingletonSession.get_session()


async def destroy_aiohttp_session():
    await SingletonSession.destroy_session()


def get_response_body(url):
    return requests.get(url).content


def cpu_heavy(_: int) -> int:
    count = 0
    for i in range(50000):
        count += i
    return count


async def acpu_heavy(_: int) -> int:
    count = 0
    for i in range(50000):
        count += i
    return count
