import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
from fastapi import APIRouter

from settings import NUMBER_OF_REQUESTS, URL_TO_BE_REQUESTED
from utils import get_response_body, SingletonSession

router = APIRouter()


@router.get('/fetch-sites-sync')
def fetch_sites_sync():
    responses = []
    for i in range(NUMBER_OF_REQUESTS):
        responses.append(requests.get(URL_TO_BE_REQUESTED).content)
    return responses


@router.get('/fetch-sites-threading')
def fetch_sites_threading():
    with ThreadPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return res


@router.get('/fetch-sites-processing')
def fetch_sites_processing():
    with ProcessPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return res


@router.get('/fetch-sites-async')
async def fetch_sites_asyncio():
    tasks = []
    for i in range(NUMBER_OF_REQUESTS):
        tasks.append(SingletonSession.fetch_url(URL_TO_BE_REQUESTED))
    return await asyncio.gather(*tasks)
