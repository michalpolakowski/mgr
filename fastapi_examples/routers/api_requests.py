import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import aiohttp
import requests
from fastapi import APIRouter

from session_util import SingletonSession

NUMBER_OF_REQUEST = 1000
URL_TO_BE_REQUESTED = 'http://localhost:8080/'

router = APIRouter()


@router.get('/fetch-sites-async')
async def fetch_sites_asyncio():
    tasks = []
    for i in range(NUMBER_OF_REQUEST):
        tasks.append(SingletonSession.fetch_url(URL_TO_BE_REQUESTED))
    return await asyncio.gather(*tasks)


@router.get('/fetch-sites-threading')
def fetch_sites_threading():
    with ThreadPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUEST)))
    return res


@router.get('/fetch-sites-processing')
def fetch_sites_processing():
    with ProcessPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUEST)))
    return res


@router.get('/fetch-sites-sync')
def fetch_sites_sync():
    responses = []
    for i in range(NUMBER_OF_REQUEST):
        responses.append(requests.get(URL_TO_BE_REQUESTED).content)
    return responses


async def get_site(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        return await response.read()


def get_response_body(url):
    return requests.get(url).content
