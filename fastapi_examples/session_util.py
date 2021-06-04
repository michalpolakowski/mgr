from typing import Optional

import aiohttp


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
