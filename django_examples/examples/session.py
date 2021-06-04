from typing import Optional

import aiohttp


class SingletonSession:
    session: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_session(cls) -> aiohttp.ClientSession:
        print(cls.session)
        if not cls.session:
            cls.session = aiohttp.ClientSession()
        return cls.session

    @classmethod
    async def fetch_url(cls, url: str) -> bytes:
        session = cls.get_session()

        async with session.get(url) as res:
            return await res.read()
