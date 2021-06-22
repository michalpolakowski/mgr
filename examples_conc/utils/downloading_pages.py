import asyncio
from typing import Tuple

import aiohttp
import requests
import time

URLS_TO_BE_FETCHED = [
    "https://www.python.org",
    "https://www.google.com/",
]


def download_site(url: str, session: requests.Session) -> None:
    with session.get(url):
        pass


def download_all_sites(identification: int) -> Tuple[float, float]:
    print(f'Identification: {identification}')
    sites = URLS_TO_BE_FETCHED * 80
    start = time.time()
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)
    stop = time.time()
    print(f"Downloaded {len(sites)} in {stop - start} seconds")
    return start, stop


async def asyncio_download_site(session: aiohttp.ClientSession, url: str) -> None:
    async with session.get(url) as response:
        await response.read()


async def asyncio_download_all_sites(i, session) -> Tuple[float, float]:
    print(f'Identification: {i}')
    start = time.time()
    urls = URLS_TO_BE_FETCHED * 80
    tasks = []
    for url in urls:
        tasks.append(asyncio_download_site(session, url))
    await asyncio.gather(*tasks)
    stop = time.time()
    print(f"Downloaded {len(urls)} in {stop - start} seconds")
    return start, stop
