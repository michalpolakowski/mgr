import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import aiohttp
import requests
from django.http import HttpResponse, JsonResponse

from examples.session import SingletonSession

URL_TO_BE_REQUESTED = 'http://localhost:8000/'
NUMBER_OF_REQUESTS = 100


def welcome_page(_):
    return JsonResponse({'welcome': 'Welcome to django example project'})


def fetch_sites_threading(_):
    with ThreadPoolExecutor() as executor:
        res = executor.map(requests.get, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return HttpResponse(res)


def fetch_sites_processing(_):
    with ProcessPoolExecutor() as executor:
        res = executor.map(requests.get, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return HttpResponse(res)


async def fetch_sites_async(_):
    tasks = []
    for i in range(NUMBER_OF_REQUESTS):
        task = asyncio.ensure_future(SingletonSession.fetch_url(URL_TO_BE_REQUESTED))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return HttpResponse(responses)


async def get_site(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        return await response.read()